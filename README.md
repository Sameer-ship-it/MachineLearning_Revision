# Machine Learning Revision

A set of Jupyter notebooks and Python exercises for revisiting core data preparation, model evaluation, and supervised/unsupervised learning concepts.

## Learning index

| Path | Topics |
| --- | --- |
| `Data_Processing.ipynb` | Label encoding, one-hot encoding, and feature scaling |
| `EvaluatingModel.ipynb` | Classification metrics, confusion matrix, and regression error metrics |
| `Regression.ipynb` | Linear and logistic regression, K-nearest neighbors, and decision trees |
| `MlRevision/` | Additional revision notebooks |
| `ML Project 1/` | Project and unsupervised-learning notebooks |
| `panadas.py` | Python practice file |

The examples are learning notes rather than a packaged library or end-to-end application. Some notebook cells are exercises in progress and may need edits before they run.

## Getting started

```bash
git clone https://github.com/Sameer-ship-it/MachineLearning_Revision.git
cd MachineLearning_Revision
python -m venv .venv
```

Activate the environment and install the common notebook libraries:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

```bash
python -m pip install jupyter pandas numpy scikit-learn matplotlib
jupyter notebook
```

Open a notebook from the index above. Some cells refer to datasets stored on a local machine; provide an appropriate dataset and update those paths before running the cells.

## Notes

- Metrics from small examples are instructional and should not be treated as benchmark results.
- For real model evaluation, use reproducible splits, suitable baselines, and metrics that reflect the class balance and cost of errors.
- The repository does not currently include a dependency lockfile or a single project-wide training pipeline.

## Author

[Sameer Raza](https://github.com/Sameer-ship-it)
