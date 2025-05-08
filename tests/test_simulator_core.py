import unittest
from SentAI_Simulator_Core import simulate_sentai_pulse

class TestSentAISimulatorCore(unittest.TestCase):

    def test_simulation_baseline(self):
        result = simulate_sentai_pulse(input_vector="HELIX", iterations=3)
        self.assertIn("response_path", result)
        self.assertEqual(result["status"], "ok")

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            simulate_sentai_pulse(input_vector="", iterations=1)

if __name__ == "__main__":
    unittest.main()
