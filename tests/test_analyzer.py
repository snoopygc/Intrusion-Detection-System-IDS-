import unittest
from src.analyzer import analyze_packet

class TestAnalyzer(unittest.TestCase):
    def test_analyze_packet(self):
        packet_data = {"payload": "malicious_payload"}
        rules = [
            {"id": 1, "pattern": "malicious_payload", "description": "Test rule"}
        ]
        result, rule = analyze_packet(packet_data, rules)
        self.assertTrue(result)
        self.assertEqual(rule["id"], 1)

if __name__ == "__main__":
    unittest.main()
