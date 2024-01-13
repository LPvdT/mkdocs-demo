"""This module contains additional trivial filler code."""

from pathlib import Path
from typing import Literal

from mkdocs_demo.config.interfaces import ITrolling


class Trolling(ITrolling):
    """The class Trolling implements the ITrolling interface."""

    def __init__(self, x: float, n: int) -> None:
        self.x = x
        self.n = n

    @property
    def multiple(self) -> float:
        return self.x * self.n

    def __str__(self) -> str:
        return f"""x={self.x}, n={self.n}, hence the multiple={self.multiple}"""

    def __repr__(self) -> str:
        return f"""{self.x} * {self.n} = {self.multiple}"""


class TestClass(object):
    """The TestClass is a basic Python class."""

    MODEL_TYPE: str = "MLP"

    def __init__(self, num_features: int, hidden_layers: int) -> None:
        """
        Initializes the number of features and the number of hidden layers for a neural network.

        Parameters
        ----------
        num_features : int
            The `num_features` parameter represents the number of input features in your model. It
            indicates the size of the input layer of your neural network.
        hidden_layers : int
            The "hidden_layers" parameter represents the number of hidden layers in a neural network.
        """

        self.num_features: int = num_features
        self.hidden_layers: int = hidden_layers

    def _show_layers(self) -> dict[str, int]:
        """
        The private method `_show_layers` returns a dictionary containing the number of features and the
        number of hidden layers.

        Returns
        -------
        A dictionary containing the number of features and the number of hidden layers.
        """

        return {
            "num_features": self.num_features,
            "hidden_layers": self.hidden_layers,
        }

    def show_model(self) -> dict[str, str | int]:
        """
        The method `show_model` returns a dictionary containing the model type and information about
        its layers.

        Returns
        -------
        A dictionary containing the model type and the layers of the model.
        """

        model_dict: dict[str, str | int] = {"model_type": self.MODEL_TYPE}
        model_dict.update(self._show_layers())

        return model_dict

    @classmethod
    def load_model(cls, path: Path | str) -> str:
        """
        The method `load_model` loads a model from a given path and returns a string indicating the
        path from which the model was loaded.

        Parameters
        ----------
        path : Path | str
            The `path` parameter is the path to the model file that needs to be loaded. It can be either a
            string or a `Path` object.

        Returns
        -------
        A string that indicates the path from which the model was loaded.
        """

        if isinstance(path, str):
            path = Path(path)

        return f"Model loaded from: '{path}' - Type: {cls.MODEL_TYPE}"

    @staticmethod
    def get_type() -> Literal["Neural Network"]:
        """
        The method `get_type` returns the string "Neural Network".

        Returns
        -------
        The string "Neural Network".
        """

        return "Neural Network"


def create_trolling(d: dict[str, int]) -> Trolling:
    """
    The function `create_trolling` takes a dictionary `d` and returns a `Trolling` object created from
    the dictionary.

    Parameters
    ----------
    d : dict[str, int]
        A dictionary containing the data needed to create a Trolling object. The keys of the dictionary are
    strings representing the attributes of the Trolling object, and the values are integers representing
    the values of those attributes.

    Returns
    -------
        An instance of the class Trolling.
    """

    return Trolling.from_dict(d)
