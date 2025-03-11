from quantum_progress_bar.quantum_progress_bar import quantum_progress, uncertainty_estimate

# プログレスバーを表示（状態は観測するたびに変化する）
quantum_progress(total=100, width=50, delay=0.2)

# 不確かな残り時間予測を取得
estimate = uncertainty_estimate()
print(f"Estimated time: {estimate}")
# 出力例: "Estimated time: 42 seconds (probably between 10 seconds - 2 minutes)"