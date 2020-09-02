import unittest
import line

class LineTests(unittest.TestCase):
    def test_line(self):
      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      testLine = line.Line(0, 1, 0, 1)
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.
      self.assertEqual(testLine.x1, 0)
      self.assertEqual(testLine.y1, 1)
      self.assertEqual(testLine.x2, 0)
      self.assertEqual(testLine.y2, 1)
    
    def test_line2(self):
      testLine2 = line.Line(-8, 2, -199999999, 1)
      self.assertEqual(testLine2.x1, -8)
      self.assertEqual(testLine2.y1, 2)
      self.assertEqual(testLine2.x2, -199999999)
      self.assertEqual(testLine2.y2, 1)
# Run the unit tests.
if __name__ == '__main__':
  unittest.main()

