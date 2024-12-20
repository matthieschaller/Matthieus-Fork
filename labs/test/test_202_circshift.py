from unittest.mock import patch, MagicMock
import unittest
from numpy.testing import assert_array_almost_equal
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
with patch('builtins.input', side_effect=['1', '0']):
    import lab.lab_202_circshift as lab

shift_lr_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 9, 9, 0, 0, 9, 9, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 9, 9, 9, 9, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

shift_lr_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 9, 9, 0, 0, 9, 9, 7, 9, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 9, 9, 9, 9, 7, 7, 7, 9, 9, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

shift_tb_1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 9, 9, 0, 0, 9, 9, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 9, 9, 9, 9, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

shift_tb_3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 9, 7, 9, 9, 0, 0, 9, 9, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 9, 9, 9, 9, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 9, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 7, 7, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


class Test202_circshift(unittest.TestCase):
    def test_reset(self):
        lab.heart = [['Not a heart']]
        lab.reset()
        reset_heart = lab.heart
        if callable(getattr(reset_heart, 'tolist', None)):
            reset_heart = reset_heart.tolist()
        assert_array_almost_equal(lab.HEART, reset_heart)

    def test_circshift_left_to_right(self):
        lab.reset()
        lab.circshift_left_to_right()
        assert_array_almost_equal(shift_lr_1, lab.heart)
        lab.circshift_left_to_right()
        lab.circshift_left_to_right()
        assert_array_almost_equal(shift_lr_3, lab.heart)

    def test_circshift_top_to_bottom(self):
        lab.reset()
        lab.circshift_top_to_bottom()
        assert_array_almost_equal(shift_tb_1, lab.heart)
        lab.circshift_top_to_bottom()
        lab.circshift_top_to_bottom()
        assert_array_almost_equal(shift_tb_3, lab.heart)


if __name__ == '__main__':
    unittest.main()
