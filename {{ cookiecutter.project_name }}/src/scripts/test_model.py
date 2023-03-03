from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from ruamel.yaml import YAML
from sklearn.metrics import matthews_corrcoef, precision_recall_fscore_support


def _compute_metrics(y_test, y_pred):
    metrics = ["precision", "recall", "f1", "support"]
    metrics_macro = precision_recall_fscore_support(
        y_test,
        y_pred,
        average="macro",
    )
    metrics_macro = np.array(metrics_macro[:-1]).tolist()
    metrics_macro = dict(zip(metrics, metrics_macro))

    mcc = float(matthews_corrcoef(y_test, y_pred))

    metrics = {
        "macro": metrics_macro,
        "mcc": mcc,
    }

    return metrics


def _test_model(
    test_path: str,
    model_path: str,
    predicted_path: str,
    metrics_path: str,
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

    metrics = _compute_metrics(y_test, y_pred)

    Path(metrics_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    yaml = YAML()

    with open(metrics_path, "w", encoding="utf8") as fp:
        yaml.dump(metrics, fp)
