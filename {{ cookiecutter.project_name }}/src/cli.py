"""This module contains a CLI application for training and testing a machine learning model."""

import typer

from scripts.split_data import _split_data
from scripts.test_model import _test_model
from scripts.train_model import _train_model

app = typer.Typer()
data_app = typer.Typer()
model_app = typer.Typer()

app.add_typer(data_app, name="data", help="Commands for data processing.")
app.add_typer(model_app, name="model", help="Commands for training and testing a machine learning model.")


@data_app.command("split")
def split_data(
    data_path: str,
    train_path: str,
    test_path: str,
    test_size: float = 0.3,
    random_state: int = 42,
    stratify: bool = True,
):
    """
    Split the data into training and testing sets and saves them into separate files.

    Args:
        data_path (str): File path for the input data.
        train_path (str): File path to save the training data.
        test_path (str): File path to save the testing data.
        test_size (float, optional): Proportion of the dataset to include in the test split. Defaults to 0.3.
        random_state (int, optional): Seed value for the random number generator used in the split. Defaults to 42.
        stratify (bool, optional): Whether or not to perform stratified sampling on the target variable.
            If True, the proportion of the target variable in the train and test sets will be the same as the
        proportion of the target variable in the input data. Defaults to True.

    Returns:
        None
    """

    _split_data(
        data_path=data_path,
        train_path=train_path,
        test_path=test_path,
        test_size=test_size,
        random_state=random_state,
        stratify=stratify,
    )


@model_app.command("train", help="Train a machine learning model and save the resulting model to a file.")
def train_model(
    train_path: str,
    model_path: str,
    penalty: str = "l2",
    dual: bool = False,
    tol: float = 1e-4,
    C: float = 100.0,
    multi_class: str = "auto",
    max_iter: int = 100,
    class_weight: None | str = None,
):
    """
    Train a machine learning model and save the resulting model to a file.

    Args:
        model_path (str): The path to save the resulting trained model.
        train_path (str): The path to the training data to be used for training the model.
        penalty (str, optional): The type of regularization penalty to use (default: "l2").
        dual (bool, optional): Whether to use dual or primal optimization (default: False).
        tol (float, optional): The tolerance for stopping criterion (default: 1e-4).
        C (float, optional): The regularization parameter (default: 100.0).
        multi_class (str, optional): The strategy to use for multi-class classification (default: "auto").
        max_iter (int, optional): The maximum number of iterations (default: 100).
        class_weight (None or str, optional): The weights associated with classes in the form {class_label: weight}
            (default: None).

    Returns:
        None: This function saves the trained model to the specified path and does not return anything.
    """

    _train_model(
        train_path=train_path,
        model_path=model_path,
        penalty=penalty,
        dual=dual,
        tol=tol,
        C=C,
        multi_class=multi_class,
        max_iter=max_iter,
        class_weight=class_weight,
    )


@model_app.command(
    "test",
    help=(
        "Runs a test on the trained model using the provided test data \n"
        "and saves the predicted results and evaluation metrics."
    ),
)
def test_model(
    test_path: str,
    model_path: str,
    predicted_path: str,
    metrics_path: str,
):
    """
    Runs a test on the trained model using the provided test data\
    and saves the predicted results and evaluation metrics.

    Args:
        test_path (str): File path for the test data.
        model_path (str): File path for the trained model.
        predicted_path (str): File path to save the predicted results.
        metrics_path (str): File path to save the evaluation metrics.

    Returns:
        None
    """

    _test_model(
        test_path=test_path,
        model_path=model_path,
        predicted_path=predicted_path,
        metrics_path=metrics_path,
    )


if __name__ == "__main__":
    app()
