import unittest
from ellipse import Ellipse

class TestEllipse(unittest.TestCase):

    def test_point_in_ellipse(self):
        e = Ellipse(0, 0, 1, 1)
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, 0), True, "Should be True")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, 0.5), True, "Should be True")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, -0.5), True, "Should be True")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0.5, 0), True, "Should be True")
        self.assertEqual(Ellipse.point_in_ellipse(e, -0.5, 0), True, "Should be True")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, 0), True, "Should be True")

        self.assertEqual(Ellipse.point_in_ellipse(e, 1, 0), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, -1, 0), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, 1), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, -1), False, "Should be False")

        self.assertEqual(Ellipse.point_in_ellipse(e, 2, 0), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, 2, 4), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, -1, 0.1), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, -0.5, -1.5), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, -3, 0), False, "Should be False")
        self.assertEqual(Ellipse.point_in_ellipse(e, 0, -3), False, "Should be False")

        e = Ellipse(-1, 1, 1, 2)
        
    
    def test_ellipse_in_ellipse(self):
        e = Ellipse(0, 0, 1, 1)
        e1 = Ellipse(0, 0, 2, 2)
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e1), True, "Should be True")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e1, e), False, "Should be False")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e), False, "Should be false")

        e = Ellipse(1, 1, 1, 1)
        e1 = Ellipse(1, 1, 2, 2)
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e1), True, "Should be True")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e1, e), False, "Should be False")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e), False, "Should be false")
         
        e = Ellipse(-1, -1, 1, 1)
        e1 = Ellipse(-1, -1, 2, 2)
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e1), True, "Should be True")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e1, e), False, "Should be False")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e), False, "Should be false")

        e = Ellipse(1, 0.5, 1, 1)
        e1 = Ellipse(0, 0, 1, 2)
        self.assertEqual(Ellipse.ellipse_in_ellipse(e, e1), False, "Should be False")
        self.assertEqual(Ellipse.ellipse_in_ellipse(e1, e), False, "Should be False")





if __name__ == '__main__':
    unittest.main()


