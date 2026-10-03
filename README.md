# Near-Earth Object (NEO) Hazard Prediction System

An educational machine learning project that explores whether an asteroid is labeled hazardous in the included dataset. It includes an exploratory notebook and an interactive Streamlit app powered by a Random Forest classifier.

🚀 **Live app:** [Open the NEO Hazard Prediction System](https://near-earth-object-hazard-prediction-system-9hrjhdcqt9tquvlzjpn.streamlit.app/)

> **Note:** This project predicts the dataset's `hazardous` label. It does not estimate the probability of an Earth impact or provide an official NASA risk assessment.

## Project contents

- `app.py` — interactive Streamlit application
- `neo.csv` — dataset used by the app and notebook
- `nb.ipynb` — data exploration, model comparison, and preliminary evaluation
- `requirements.txt` — Python dependencies

## Model inputs

The classifier uses four numeric features:

- Estimated minimum diameter (km)
- Relative velocity (km/h)
- Miss distance (km)
- Absolute magnitude

The app trains a 200-tree Random Forest from `neo.csv` when a prediction is first requested. The asteroid ID and name are not used as model inputs. A probability threshold slider controls whether the app displays the hazardous or non-hazardous label; the default threshold of `0.25` is exploratory.

## Preliminary notebook results

The notebook reports the following results for its tuned Random Forest:

| Threshold | Accuracy | Precision | Recall | F1 score |  ROC AUC |
| --------: | -------: | --------: | -----: | -------: | -------: |
|      0.50 |   91.63% |    61.74% | 36.88% |   46.18% |   0.9331 |
|      0.25 |   88.21% |    43.81% | 74.89% |   55.28% | 0.9331\* |

At the lower threshold, the model catches more hazardous-labeled examples, with more false positives. These results are **preliminary**: the notebook used a random row split even though asteroid IDs repeat, and it used the test set while exploring thresholds. A stronger evaluation should split by asteroid ID, choose the threshold on validation data, and report results on an untouched test set.

## Run locally

From the project folder, create and activate a virtual environment, then install the dependencies and start the app:

```bash
python -m venv neo_venv
```

On Windows PowerShell:

```powershell
.\neo_venv\Scripts\Activate.bat
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

On macOS or Linux:

```bash
source neo_venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Keep `neo.csv` in the same folder as `app.py`. Streamlit will print a local address, usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `neo.csv`, and `requirements.txt` to a GitHub repository. Include this README and `nb.ipynb` to show the project and analysis.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub and choose **Create app**.
3. Select your repository, the `main` branch, and `app.py` as the app file.
4. Deploy. Once the app is live, add its URL here if you want visitors to find it from the repository page.

## Tools

Python, pandas, scikit-learn, Jupyter Notebook, and Streamlit.
