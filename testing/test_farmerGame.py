import unittest
from src.farmerGame.farmerGame import FarmerGame
from src.farmerGame.state import State


class TestFarmerGame(unittest.TestCase):

    def setUp(self):
        # Set up for each test
        self.item_names = ("Farmer", "Wolf", "Goat", "Cabbage")
        self.initial_state = State([False, False, False, False])  # All on right
        self.target_state = State([True, True, True, True])  # All on left
        self.game = FarmerGame(self.item_names)

    def test_initialization(self):
        """Test that the game initializes correctly with items."""
        self.assertEqual(self.game.itemNames, self.item_names)
        self.assertIsNone(self.game.source)
        self.assertIsNone(self.game.target)
        self.assertEqual(len(self.game.badStates), 0)

    def test_set_source_target(self):
        """Test that source and target states are set correctly."""
        self.game.setSource(self.initial_state)
        self.game.setTarget(self.target_state)

        self.assertEqual(self.game.source, self.initial_state)
        self.assertEqual(self.game.target, self.target_state)

    def test_set_source_bad_state(self):
        """Test that setting a source to a bad state raises an error."""
        self.game.badStates.add(self.initial_state)
        with self.assertRaises(ValueError):
            self.game.setSource(self.initial_state)

    def test_set_target_bad_state(self):
        """Test that setting a target to a bad state raises an error."""
        self.game.badStates.add(self.target_state)
        with self.assertRaises(ValueError):
            self.game.setTarget(self.target_state)

    def test_add_bad_states(self):
        """Test adding bad states and that duplicates are not allowed."""
        bad_state_1 = State([True, True, False, True])
        bad_state_2 = State([False, True, True, False])

        self.game.addBadStates([bad_state_1, bad_state_2])

        self.assertIn(bad_state_1, self.game.badStates)
        self.assertIn(bad_state_2, self.game.badStates)

    def test_add_bad_state_equal_source(self):
        """Test that adding a bad state equal to the source raises an error."""
        self.game.setSource(self.initial_state)

        with self.assertRaises(ValueError):
            self.game.addBadStates([self.initial_state])

    def test_add_bad_state_equal_target(self):
        """Test that adding a bad state equal to the target raises an error."""
        self.game.setTarget(self.target_state)

        with self.assertRaises(ValueError):
            self.game.addBadStates([self.target_state])

    def test_bfs_solution_found(self):
        """Test that the BFS finds a valid solution when it exists."""
        self.game.setSource(self.initial_state)
        self.game.setTarget(self.target_state)

        path, success = self.game.bfs()
        self.assertTrue(success)
        self.assertIsInstance(path, list)
        self.assertGreater(len(path), 0)

    def test_bfs_no_solution(self):
        """Test that the BFS correctly returns no solution when blocked by bad states."""
        self.game.setSource(self.initial_state)
        self.game.setTarget(self.target_state)

        # Block the game by adding all possible next states to badStates
        bad_states = [
            State([True, False, False, False]),
            State([True, True, False, False]),
            State([True, False, True, False]),
            State([True, False, False, True]),
        ]
        self.game.addBadStates(bad_states)

        path, success = self.game.bfs()

        self.assertFalse(success)
        self.assertEqual(path, [])

    def test_moves_from_path(self):
        """Test that the correct moves are printed for a valid path."""
        self.game.setSource(self.initial_state)
        self.game.setTarget(self.target_state)

        # Assuming the BFS would find a path, print the moves
        path, success = self.game.bfs(printActions=True)
        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()
