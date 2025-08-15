import unittest
from game import get_game_result, Outcome

class TestGetGameResult(unittest.TestCase):
    def test_tie(self):
        self.assertEqual(get_game_result("R", "R"), Outcome.TIE)
        self.assertEqual(get_game_result("P", "P"), Outcome.TIE)
        self.assertEqual(get_game_result("S", "S"), Outcome.TIE)

    def test_win(self):
        self.assertEqual(get_game_result("R", "S"), Outcome.WIN)
        self.assertEqual(get_game_result("P", "R"), Outcome.WIN)
        self.assertEqual(get_game_result("S", "P"), Outcome.WIN)

    def test_lose(self):
        self.assertEqual(get_game_result("R", "P"), Outcome.LOSE)
        self.assertEqual(get_game_result("P", "S"), Outcome.LOSE)
        self.assertEqual(get_game_result("S", "R"), Outcome.LOSE)

if __name__ == "__main__":
    unittest.main()