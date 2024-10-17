import unittest
from ..src.state import State


class TestState(unittest.TestCase):

    def test_state_initialization(self):
        state = State([True, False, True])
        self.assertTrue(state.itemsLeft == [True, False, True])

    def test_init_Prev(self):
        with self.assertRaises(TypeError):
            State(tuple(1, 1, 1, 1), None)

        with self.assertRaises(TypeError):
            State(list(1, 1, 1, 1), 1)

        with self.assertRaises(TypeError):
            State(tuple(1, 1, 1, 1))

    def test_add_item_names(self):
        State.addItemNames(("farmer", "Wolf", "Goat", "Cabbage"))
        state = State((1, 1, 1, 1))
        self.assertTrue(state.itemNames == ("farmer", "Wolf", "Goat", "Cabbage"))

    def test_default_item_names(self):
        self.assertTrue(State.itemNames == tuple("Itemnames not set"))

    def test_str(self):
        state = State([1, 1, 1, 1])
        State.addItemNames(("Farmer", "Wolf", "Goat", "Cabbage"))
        self.assertTrue(str(state) == "[Farmer, Wolf, Goat, Cabbage]")

    # intended behaviour
    def test_eq_within_diff_prev(self):
        state = State([1, 1, 1, 1])
        state2 = State([1, 1, 1, 1], state)
        self.assertTrue(state == state2)

    def test_eq_within_diff_prev(self):
        state = State([1, 1, 1, 1])
        state2 = State([1, 1, 1, 1])
        self.assertTrue(state == state2)

    def test_eq_outide(self):
        state = State([1, 1, 1, 1])
        self.assertFalse(state == 1)

    def test_hash(self):
        state = State([1, 1, 1, 1])
        self.assertTrue(hash(state) == hash(tuple(state.itemsLeft)))

    def tearDown(self) -> None:
        State.itemNames = tuple("Itemnames not set")


if __name__ == "__main__":
    unittest.main()
