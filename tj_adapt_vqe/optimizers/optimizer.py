from abc import ABC, abstractmethod

import numpy as np
from typing_extensions import Self


class Optimizer(ABC):
    """
    Base Class that all other optimizers should inherit from
    """

    def __init__(self: Self, gradient_convergence_threshold: float = 0.01) -> None:
        """
        Initializes the Optimizer

        Args:
            gradient_convergence_threshold: float, the threshold that qualifies for is_converged. Not used if Optimizer.is_converged is overrided
        """

        self.gradient_convergence_threshold = gradient_convergence_threshold

    @abstractmethod
    def update(self: Self, param_vals: np.ndarray, gradient: np.ndarray) -> np.ndarray:
        """
        Performs a single step of optimization, returning the new param_vals,
        does NOT update either param_vals or measure in place.

        Args:
            param_vals: np.ndarray, a 1d numpy array with the current values of each param,
            gradient: np.ndarray, a numpy array which is the same dimension as param_vals and represents the gradient of each param_val
        """

    def is_converged(self: Self, gradient: np.ndarray) -> bool:
        """
        Returns whether or not the current optimizer is converged, the naive convergence criterion is whether the gradients all fall below some threshold
        """

        return bool(
            np.all(np.abs(gradient) < self.gradient_convergence_threshold)
        )
