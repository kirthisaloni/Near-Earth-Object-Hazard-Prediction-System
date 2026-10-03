# Near-Earth Object Hazard Classifier

An educational Streamlit app for exploring a Random Forest classifier trained on the included `neo.csv` dataset.

## Run locally

```bash
python -m venv .venv
```

Activate the environment, then install dependencies and launch the app:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

The app trains its model from `neo.csv` the first time a prediction is requested. Keep `neo.csv` in the same repository as `app.py`.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, and `neo.csv` to a GitHub repository. You may also include the notebook and project report if you want them visible to visitors.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
3. Choose **Create app**, select the repository and branch, and set the app file path to `app.py`.
4. Deploy. Community Cloud installs the packages from `requirements.txt`.

## Interpretation and limitations

- The app predicts the dataset's `hazardous` label. It does not calculate an impact probability or provide an official NASA risk assessment.
- The app's default classification threshold of 0.25 is exploratory. Select a threshold using validation data before reporting final performance.
- The notebook's evaluation used a random row split even though asteroid IDs repeat. Re-evaluate with a grouped split by asteroid ID before claiming the reported scores generalize to unseen asteroids.
- This app trains on all included labeled rows for demonstration. It is not a validated operational warning system.
