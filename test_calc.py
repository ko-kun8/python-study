# test_calc.py (テストする側のファイル)
import unittest
from calc import add  # ①で作った関数を読み込む

class TestCalc(unittest.TestCase):
    def test_add(self):
        # add(2, 3) の結果が 「5」 になるかテストする
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()