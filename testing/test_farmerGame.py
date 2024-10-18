from src.farmerGame.farmerGame import FarmerGame
from src.farmerGame.state import State
import unittest


class TestState(unittest.TestCase):

    def setUp(self):
        self.game = FarmerGame(
            ("Farmer", "Wolf", "Goat", "Cabbage"), {State((1, 1, 1, 1))}
        )

    def test_init(self):
        self.assertTrue(self.game.itemNames == ("Farmer", "Wolf", "Goat", "Cabbage"))

    def test_init_badStates(self):
        self.assertTrue(self.game.badStates == {State((1, 1, 1, 1))})


if __name__ == "__main__":
    unittest.main()
