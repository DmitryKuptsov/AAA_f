from final_project_python import Margherita
from final_project_python import Pepperoni
from final_project_python import Hawaiian
from final_project_python import delivery
from final_project_python import pickup
from final_project_python import bake
import unittest


class TestCountLetters(unittest.TestCase):
    def test_margh_dict_l(self):
        actual = Margherita().dict()
        expected = {"tomato sauce": 1,
                    "mozzarella": 2,
                    "tomatoes": 5}
        self.assertEqual(actual, expected)

    def test_pepp_dict_l(self):
        actual = Pepperoni().dict()
        expected = {"tomato sauce": 1,
                    "mozzarella": 2,
                    "pepperoni": 8}
        self.assertEqual(actual, expected)

    def test_hawaii_dict_l(self):
        actual = Hawaiian().dict()
        expected = {"tomato sauce": 1,
                    "mozzarella": 2,
                    "chicken": 1,
                    "pineapples": 1}
        self.assertEqual(actual, expected)

    def test_margh_dict_xl(self):
        actual = Margherita(size="XL").dict()
        expected = {"tomato sauce": 2,
                    "mozzarella": 3,
                    "tomatoes": 10}
        self.assertEqual(actual, expected)

    def test_pepp_dict_xl(self):
        actual = Pepperoni(size="XL").dict()
        expected = {"tomato sauce": 2,
                    "mozzarella": 3,
                    "pepperoni": 12}
        self.assertEqual(actual, expected)

    def test_hawaii_dict_xl(self):
        actual = Hawaiian(size="XL").dict()
        expected = {"tomato sauce": 2,
                    "mozzarella": 3,
                    "chicken": 2,
                    "pineapples": 2}
        self.assertEqual(actual, expected)

    def test_eq_margh_l(self):
        actual_1 = Margherita()
        actual_2 = Margherita(size="L")
        self.assertFalse(actual_1 != actual_2)

    def test_eq_pepp_l(self):
        actual_1 = Pepperoni()
        actual_2 = Pepperoni(size="L")
        self.assertFalse(actual_1 != actual_2)

    def test_not_eq_margh_l_pepp_l(self):
        actual_1 = Margherita()
        actual_2 = Pepperoni(size="L")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_margh_l_xl(self):
        actual_1 = Margherita()
        actual_2 = Margherita(size="XL")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_pepp_l_xl(self):
        actual_1 = Pepperoni()
        actual_2 = Pepperoni(size="XL")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_hawaii_l_xl(self):
        actual_1 = Hawaiian()
        actual_2 = Hawaiian(size="XL")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_margh_l_hawaii_l(self):
        actual_1 = Margherita()
        actual_2 = Hawaiian(size="L")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_hawaii_l_pepp_l(self):
        actual_1 = Hawaiian()
        actual_2 = Pepperoni(size="L")
        self.assertFalse(actual_1 == actual_2)

    def test_not_eq_hawaii_xl_pepp_xl(self):
        actual_1 = Hawaiian(size="Xl")
        actual_2 = Pepperoni(size="XL")
        self.assertFalse(actual_1 == actual_2)

    def test_delivery_margh_l(self):
        actual = delivery(Margherita())
        expected = Margherita(size="L")
        self.assertEqual(actual, expected)

    def test_pickup_pepp_l(self):
        actual = pickup(Pepperoni())
        expected = Pepperoni(size="L")
        self.assertEqual(actual, expected)

    def test_bake_hawaii_l(self):
        actual = bake(Hawaiian())
        expected = Hawaiian(size="L")
        self.assertEqual(actual, expected)
