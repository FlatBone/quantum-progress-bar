"""
Quantum Progress Bar - A quantum mechanics-inspired progress bar library.

This package provides tools to create progress bars with quantum behavior,
including random state collapses, uncertainty estimates, and entanglement.
"""

from .quantum_progress_bar import (
    QuantumProgressBar,
    quantum_progress,
    uncertainty_estimate,
    quantum_loading,
    quantum_tqdm,
)

__all__ = [
    "QuantumProgressBar",
    "quantum_progress",
    "uncertainty_estimate",
    "quantum_loading",
    "quantum_tqdm",
]
__version__ = "0.1.0"