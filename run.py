from quantum_progress_bar import QuantumProgressBar, quantum_progress, quantum_loading, qqdm
import time


print("🔬 Quantum Progress Bar Demo 🔬")
print("=" * 50)

print("\n1. 基本的な量子プログレスバー")
print("-" * 30)
# Display a quantum progress bar
quantum_progress(total=100, width=50, delay=0.1)

print("\n2. 量子プログレスバークラスの直接使用")
print("-" * 30)
# Initialize a quantum progress bar
pb = QuantumProgressBar(total_steps=100, collapse_factor=0.3, uncertainty_level=0.9)

# Display progress
for _ in range(5):
    progress = pb.quantum_progress(width=50)
    print(f" Estimated time: {pb.uncertainty_estimate()}")
    time.sleep(0.1)

print("\n3. 量子エンタングルメント")
print("-" * 30)
# Entangle with another progress bar
pb2 = QuantumProgressBar(total_steps=100)
pb.entangle(pb2)
pb.update(steps=10)  # Affects both bars due to entanglement
pb.quantum_progress(width=50)
print()
pb2.quantum_progress(width=50)
print()

print("\n4. 量子ローディングアニメーション")
print("-" * 30)
quantum_loading(message="Loading quantum state", duration=2, width=50)

print("\n5. tqdm風の使い方")
print("-" * 30)
print("イテレータをラップする例:")
for i in qqdm(range(20)):
    # Some processing
    time.sleep(0.05)

print("\nコンテキストマネージャとして使用する例:")
with qqdm(total_steps=20) as qbar:
    for i in range(20):
        # Some processing
        time.sleep(0.05)
        qbar.update(1)

print("\n量子力学的進捗表示をお楽しみいただきありがとうございました！")
