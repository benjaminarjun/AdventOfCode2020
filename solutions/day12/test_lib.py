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

    def test_position_addition(self):
        p1 = Position(1, 2)
        p2 = Position(3, 4)

        self.assertEqual(Position(4, 6), p1 + p2)


class TestShipNavigation(unittest.TestCase):
    @property
    def nav_instructions(self):
        return [NavInstruction.from_str(z) for z in (
            'F10',
            'N3',
            'F7',
            'R90',
            'F11',
        )]

    def test_ship_navigation(self):
        ship = Ship()
        ship.navigate(self.nav_instructions)
        
        expected = Position(17, -8)
        self.assertEqual(expected, ship.position)

    def test_ship_waypoint_navigation(self):
        init_wpt = Position(10, 1)
        ship = Ship(wpt_nav=True, init_wpt=init_wpt)
        ship.navigate(self.nav_instructions)

        expected = Position(214, -72)
        self.assertEqual(expected, ship.position)
