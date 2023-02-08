from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import typer
from ruamel.yaml import YAML
from sklearn.metrics import matthews_corrcoef, precision_recall_fscore_support


def _compute_metrics(y_test, y_pred, ndigits=2):
    mcc = matthews_corrcoef(y_test, y_pred)
    pre, rec, f1_score, _ = precision_recall_fscore_support(
        y_test,
        y_pred,
        average="macro",
    )

    metrics = {
        "precision": round(pre, ndigits),
        "recall": round(rec, ndigits),
        "f1": round(f1_score, ndigits),
        "mcc": round(mcc, ndigits),
    }
    metrics = {key: float(value) for key, value in metrics.items()}
    return metrics


def test_model(
    test_path: str,
    model_path: str,
    predicted_path: str,
    metrics_path: str,
    ndigits: int = 2,
):
    df_test = pd.read_csv(test_path)

    model = joblib.load(model_path)

    X_test = df_test.drop(["target"], axis=1)

    y_test = df_test["target"]
    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)
    y_prob = np.amax(y_prob, axis=1)

    X_test["true"] = y_test
    X_test["pred"] = y_pred
    X_test["prob"] = y_prob

    Path(predicted_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    X_test.to_csv(predicted_path, index=False)

    metrics = _compute_metrics(y_test, y_pred, ndigits)

    Path(metrics_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    yaml = YAML()

    with open(metrics_path, "w", encoding="utf8") as fp:
        yaml.dump(metrics, fp)


if __name__ == "__main__":
    typer.run(test_model)
