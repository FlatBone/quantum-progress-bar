from quantum_progress_bar.quantum_progress_bar import QuantumProgressBar, quantum_progress, quantum_loading
import time


# Display a quantum progress bar
quantum_progress(total=100, width=50, delay=0.2)

# Initialize a quantum progress bar
pb = QuantumProgressBar(total_steps=100, collapse_factor=0.3, uncertainty_level=0.9)

# Display progress
for _ in range(10):
    progress = pb.quantum_progress(width=50)
    print(f" Estimated time: {pb.uncertainty_estimate()}")
    time.sleep(0.2)

# Entangle with another progress bar
pb2 = QuantumProgressBar(total_steps=100)
pb.entangle(pb2)
pb.update(steps=10)  # Affects both bars due to entanglement

quantum_loading(message="Loading quantum state", duration=3, width=50)