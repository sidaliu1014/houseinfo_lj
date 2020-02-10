__author__ = 'starstar'

import unittest
from tools.preprocess import splittitle, splitfloor, splitdealcycle, splitaddress
from tools.house import House


class TestPreprocess(unittest.TestCase):

    def test_splittitle(self):
        house = House()
        title = "shanghai zhengda homeland"
        title2 = "shanghai zhengda "
        splittitle(house, title)
        self.assertTrue(hasattr(house, 'name'))
        self.assertEqual(house.name, 'shanghai')
        self.assertTrue(hasattr(house, 'type'))
        self.assertEqual(house.type, 'zhengda')
        self.assertTrue(hasattr(house, 'size'))
        self.assertEqual(house.size, 'homeland')
        splittitle(house, title2)
        self.assertRaises(Exception)

    def test_splitaddress(self):

        house = House()
        address = "shanghai|zhengda"
        address2 = "shanghai"
        splitaddress(house, address)
        self.assertTrue(hasattr(house, 'direction'))
        self.assertEqual(house.direction, 'shanghai')
        self.assertTrue(hasattr(house, 'decoration'))
        self.assertEqual(house.decoration, 'zhengda')


if __name__ == "__main__":
    unittest.main()
