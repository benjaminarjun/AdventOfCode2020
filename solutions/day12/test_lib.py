import unittest
from .results import NavInstruction, Position, Ship


class TestNavInstruction(unittest.TestCase):
    def test_nav_instruction_from_str(self):
        instr_str = 'F10'
        instr = NavInstruction.from_str(instr_str)

        self.assertEqual('F', instr.direction)
        self.assertEqual(10, instr.magnitude)


class TestPosition(unittest.TestCase):
    def _get_position(self):
        return Position(3, 5)

    def test_init(self):
        p = self._get_position()
        self.assertEqual(Position(3, 5), p)

    def test_init_default(self):
        p = Position()
        self.assertEqual(p.x, 0)
        self.assertEqual(p.y, 0)

    def test_move_sequence(self):
        p = self._get_position()

        instrs = [
            NavInstruction('N', 3),
            NavInstruction('W', 8),
        ]

        for instr in instrs:
            p.move(instr)

        self.assertEqual(Position(-5, 8), p)


class TestShipNavigation(unittest.TestCase):
    def test_ship_navigation(self):
        ship = Ship()
        nav_instructions = [NavInstruction.from_str(z) for z in (
            'F10',
            'N3',
            'F7',
            'R90',
            'F11',
        )]

        ship.navigate(nav_instructions)
        
        expected = Position(17, -8)
        self.assertEqual(expected, ship.position)
