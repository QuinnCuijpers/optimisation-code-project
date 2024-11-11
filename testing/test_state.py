import unittest
from src.farmerGame.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        # Setup method to initialize default test variables
        self.items_left1 = [True, False, False, True]
        self.items_left2 = [False, True, True, False]
        self.prev_state = State([True, True, False, False])
        self.state1 = State(self.items_left1, self.prev_state)
        self.state2 = State(self.items_left2)

    def test_initialization(self):
        """Test that State objects initialize correctly"""
        self.assertEqual(self.state1.itemsLeft, self.items_left1)
        self.assertEqual(self.state1.prev, self.prev_state)

    def test_add_item_names(self):
        """Test that addItemNames sets the class-level item_names correctly"""
        State.add_item_names(("Farmer", "Wolf", "Goat", "Cabbage"))
        self.assertEqual(State.itemNames, ("Farmer", "Wolf", "Goat", "Cabbage"))

    def test_eq_method(self):
        """Test equality comparison between two State objects"""
        state3 = State([False, True, True, False])
        self.assertEqual(self.state2, state3)
        self.assertNotEqual(self.state1, state3)

    def test_hash_method(self):
        """Test that States can be used as dictionary keys (hashable)"""
        state_dict = {self.state1: "Start state", self.state2: "Another state"}
        self.assertEqual(state_dict[self.state1], "Start state")
        self.assertEqual(state_dict[self.state2], "Another state")

    def test_neighboring_states(self):
        """Test that neighbors are generated correctly"""
        State.add_item_names(("Farmer", "Wolf", "Goat", "Cabbage"))
        neighbors = self.state1.get_neighbours()
        self.assertTrue(isinstance(neighbors, list))
        for neighbor in neighbors:
            self.assertIsInstance(neighbor, State)
        # Optionally: More specific tests can be written here depending on your neighbors logic

    def test_backtracking(self):
        """Test backtracking by checking the previous state"""
        self.assertEqual(self.state1.prev, self.prev_state)

    def test_invalid_neighbors(self):
        """Test that invalid neighbor states are not generated"""
        # Assuming your logic prevents certain illegal moves
        State.add_item_names(("Farmer", "Wolf", "Goat", "Cabbage"))
        neighbors = self.state1.get_neighbours()
        # Ensure no invalid neighbor exists (for example, a state with an illegal configuration)
        invalid_state = State([False, False, True, True])  # Example invalid state
        self.assertNotIn(invalid_state, neighbors)


if __name__ == "__main__":
    unittest.main()
