from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = Path(__file__).parent / "neo.csv"
FEATURES = [
    "est_diameter_min",
    "relative_velocity",
    "miss_distance",
    "absolute_magnitude",
]


@st.cache_resource(show_spinner='Loading')#"Training the model from neo.csv…")
def load_model():
    data = pd.read_csv(DATA_PATH)
    required = FEATURES + ["hazardous"]
    missing = [column for column in required if column not in data.columns]
    if missing:
        raise ValueError(f"neo.csv is missing required columns: {', '.join(missing)}")

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=None,
        min_samples_split=5,
        random_state=42,
        n_jobs=-1,
    )
    model.fit(data[FEATURES], data["hazardous"].astype(bool))
    return model


st.set_page_config(page_title="NEO Hazard Classifier", page_icon="☄️")
st.title("☄️ Near-Earth Object Hazard Classifier")
st.write(
    "Explore how a Random Forest trained on the included NEO dataset classifies "
    "an object using its size, velocity, miss distance, and absolute magnitude."
)
# st.info(
#     "Educational demo only: this predicts the dataset's hazardous label. It is not "
#     "an impact probability or an official NASA risk assessment."
# )

with st.sidebar:
    st.header("Classification settings")
    threshold = st.slider(
        "Hazardous classification threshold",
        min_value=0.05,
        max_value=0.95,
        value=0.25,
        step=0.05,
        help="Lower values flag more objects as hazardous and usually increase recall.",
    )
    st.caption("The 0.25 default is exploratory, not a validated operational threshold.")

with st.form("neo_input"):
    st.subheader("Enter object characteristics")
    left, right = st.columns(2)
    with left:
        diameter = st.number_input(
            "Estimated minimum diameter (km)",
            min_value=0.000001,
            value=0.1,
            format="%.6f",
        )
        velocity = st.number_input(
            "Relative velocity (km/h)", min_value=0.0, value=48000.0, step=1000.0
        )
    with right:
        miss_distance = st.number_input(
            "Miss distance (km)", min_value=0.0, value=37000000.0, step=1000000.0
        )
        magnitude = st.number_input(
            "Absolute magnitude", value=23.5, step=0.1, format="%.2f"
        )
    submitted = st.form_submit_button("Classify object", type="primary")

if submitted:
    model = load_model()
    sample = pd.DataFrame(
        [[diameter, velocity, miss_distance, magnitude]], columns=FEATURES
    )
    score = float(model.predict_proba(sample)[0, 1])
    if score >= threshold:
        st.error("Classified as hazardous")
    else:
        st.success("Classified as non-hazardous")
    st.metric("Model score for hazardous class", f"{score:.1%}")
    st.caption("This score is not a calibrated probability of collision with Earth.")

# with st.expander("About this model"):
#     st.write(
#         "The app trains a 200-tree Random Forest from neo.csv. It does not use the "
#         "asteroid ID or name as model features. The notebook's metrics are preliminary: "
#         "the data contains repeated asteroid IDs, so evaluation should be redone with "
#         "an asteroid-level grouped split."
#     )
