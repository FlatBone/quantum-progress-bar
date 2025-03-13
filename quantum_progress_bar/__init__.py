"""
Quantum Progress Bar - A quantum mechanics-inspired progress bar library.

This package provides tools to create progress bars with quantum behavior,
including random state collapses, uncertainty estimates, and entanglement.

The library can be used in multiple ways:

1. Using the qqdm function (tqdm-like):
   ```python
   from quantum_progress_bar import qqdm
   
   # Wrap an iterable
   for i in qqdm(range(100)):
       process(i)
   ```

2. Using the QuantumProgressBar class directly:
   ```python
   from quantum_progress_bar import QuantumProgressBar
   
   # Create a progress bar
   pb = QuantumProgressBar(total_steps=100)
   pb.quantum_progress()
   pb.update(10)
   
   # Or wrap an iterable
   for item in QuantumProgressBar(range(100)):
       process(item)
   ```

3. Using the context manager:
   ```python
   with QuantumProgressBar(total_steps=100) as pb:
       for i in range(100):
           process(i)
           pb.update(1)
   ```
"""

from .quantum_progress_bar import (
    QuantumProgressBar,
    quantum_progress,
    uncertainty_estimate,
    quantum_loading,
    qqdm,
)

__all__ = [
    "QuantumProgressBar",
    "quantum_progress",
    "uncertainty_estimate",
    "quantum_loading",
    "qqdm",
]
__version__ = "0.1.0"
