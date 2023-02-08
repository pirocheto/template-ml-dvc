from pathlib import Path
from typing import Union

import joblib
import pandas as pd
import typer
from sklearn.linear_model import LogisticRegression


def train_model(
    model_path: str,
    train_path: str,
    penalty: str = "l2",
    dual: bool = False,
    tol: float = 1e-4,
    C: float = 100.0,
    multi_class: str = "auto",
    max_iter: int = 100,
    class_weight: Union[None, str] = None,
):
    model = LogisticRegression(
        penalty=penalty,
        dual=dual,
        tol=tol,
        C=C,
        multi_class=multi_class,
        max_iter=max_iter,
        class_weight=class_weight,
    )

    df_train = pd.read_csv(train_path)

    X_train = df_train.drop(["target"], axis=1)

    y_train = df_train["target"]

    model.fit(X_train, y_train)

    Path(model_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    joblib.dump(model, model_path)


if __name__ == "__main__":
    typer.run(train_model)
