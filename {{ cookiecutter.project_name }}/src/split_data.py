from pathlib import Path

import pandas as pd
import typer
from sklearn.model_selection import train_test_split


def split_data(
    data_path: str,
    train_path: str,
    test_path: str,
    test_size: float = 0.3,
    random_state: int = 42,
    stratify: bool = True,
):
    df_data = pd.read_csv(data_path)
    df_train, df_test = train_test_split(
        df_data,
        test_size=test_size,
        random_state=random_state,
        stratify=df_data["target"] if stratify else None,
    )

    Path(train_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    Path(test_path).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df_train.to_csv(train_path, index=False)
    df_test.to_csv(test_path, index=False)


if __name__ == "__main__":
    typer.run(split_data)
