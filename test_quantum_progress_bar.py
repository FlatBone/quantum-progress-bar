import unittest
import sys
import io
import time
from quantum_progress_bar.quantum_progress_bar import QuantumProgressBar, quantum_progress, uncertainty_estimate, quantum_loading

class TestQuantumProgressBar(unittest.TestCase):
    def setUp(self):
        """各テストの前に実行されるセットアップメソッド"""
        self.pb = QuantumProgressBar(total_steps=100, collapse_factor=0.2, uncertainty_level=0.8)

    def test_init(self):
        """初期化が正しく動作するかテスト"""
        self.assertEqual(self.pb.total_steps, 100)
        self.assertTrue(0 <= self.pb.current_state <= 33)  # 初期状態は total_steps の 1/3 以内
        self.assertEqual(self.pb.collapse_factor, 0.2)
        self.assertEqual(self.pb.uncertainty_level, 0.8)
        self.assertIsNotNone(self.pb.start_time)
        self.assertEqual(len(self.pb.observed_states), 0)
        self.assertIsNone(self.pb.entangled_state)

    def test_collapse_wavefunction(self):
        """波動関数の崩壊が正しく動作するかテスト"""
        initial_state = self.pb.current_state
        self.pb._collapse_wavefunction()
        self.assertTrue(0 <= self.pb.current_state <= self.pb.total_steps)
        self.assertEqual(len(self.pb.observed_states), 1)
        self.assertEqual(self.pb.observed_states[0], initial_state)

    def test_quantum_progress(self):
        """プログレスバーの表示と量子挙動が正しく動作するかテスト"""
        # 標準出力をキャプチャ
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        progress = self.pb.quantum_progress(width=50, quantum_bars=True)
        sys.stdout = sys.__stdout__  # 元に戻す
        
        self.assertTrue(0 <= progress <= 100)
        output = captured_output.getvalue()
        self.assertTrue(len(output.strip()) > 50)  # バーとパーセンテージが含まれる
        self.assertIn("%", output)

    def test_uncertainty_estimate(self):
        """不確実な時間見積もりが正しく生成されるかテスト"""
        estimate = self.pb.uncertainty_estimate()
        self.assertIsInstance(estimate, str)
        self.assertTrue(len(estimate) > 0)
        
        # 初期状態で進捗がない場合
        pb_no_progress = QuantumProgressBar(total_steps=100)
        pb_no_progress.current_state = 0
        self.assertIn("Unknown ± ∞", pb_no_progress.uncertainty_estimate())

    def test_entangle(self):
        """エンタングルメントが正しく動作するかテスト"""
        pb2 = QuantumProgressBar(total_steps=100)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        self.pb.entangle(pb2)
        sys.stdout = sys.__stdout__
        
        self.assertEqual(self.pb.entangled_state, pb2)
        self.assertEqual(pb2.entangled_state, self.pb)
        self.assertIn("entangled", captured_output.getvalue())

    def test_update(self):
        """update メソッドが正しく動作するかテスト"""
        initial_state = self.pb.current_state
        self.pb.update(steps=10)
        self.assertEqual(self.pb.current_state, min(self.pb.total_steps, initial_state + 10))

        # エンタングルされた場合の挙動をテスト
        pb2 = QuantumProgressBar(total_steps=100)
        self.pb.entangle(pb2)
        pb2_initial = pb2.current_state
        self.pb.update(steps=5)
        self.assertTrue(0 <= pb2.current_state <= pb2.total_steps)
        self.assertNotEqual(pb2.current_state, pb2_initial)  # 変化があることを確認

    def test_quantum_progress_function(self):
        """quantum_progress 関数が正しく動作するかテスト"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        final_progress = quantum_progress(total=100, width=50, delay=0.01, iterations=10)
        sys.stdout = sys.__stdout__
        
        self.assertTrue(0 <= final_progress <= 100)
        output = captured_output.getvalue()
        self.assertTrue(len(output.strip()) > 0)

    def test_uncertainty_estimate_function(self):
        """uncertainty_estimate 関数が正しく動作するかテスト"""
        estimate = uncertainty_estimate()
        self.assertIsInstance(estimate, str)
        self.assertTrue(len(estimate) > 0)

    def test_quantum_loading(self):
        """quantum_loading 関数が正しく動作するかテスト"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        quantum_loading(message="Test loading", duration=0.5, width=50)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertTrue(len(output.strip()) > 0)
        self.assertIn("Test loading", output)

if __name__ == "__main__":
    unittest.main()