import unittest
from .results import NavInstruction, Ship


class TestNavInstruction(unittest.TestCase):
    def test_nav_instruction_from_str(self):
        instr_str = 'F10'
        instr = NavInstruction.from_str(instr_str)

        self.assertEqual('F', instr.direction)
        self.assertEqual(10, instr.magnitude)

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
        
        expected = [17, -8]
        self.assertEqual(expected, ship.position)
