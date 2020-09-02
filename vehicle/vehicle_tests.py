import unittest
import vehicle

class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
    # Add code here.
      testVehicle = vehicle.Vehicle(4, 100, 2, False)
      testVehicle2 = vehicle.Vehicle(0, -99999999999999999, 10000000000000000000, False)
      testVehicle3 = vehicle.Vehicle(-10, 999, 0, True)
      self.assertEqual(testVehicle.wheels, 4)
      self.assertEqual(testVehicle.fuel, 100)
      self.assertEqual(testVehicle.doors, 2)
      self.assertEqual(testVehicle.roof, False)
      self.assertEqual(testVehicle2.wheels, 0)
      self.assertEqual(testVehicle2.fuel, -99999999999999999)
      self.assertEqual(testVehicle2.doors, 10000000000000000000)
      self.assertEqual(testVehicle2.roof, False)
      self.assertEqual(testVehicle3.wheels, -10)
      self.assertEqual(testVehicle3.fuel, 999)
      self.assertEqual(testVehicle3.doors, 0)
      self.assertEqual(testVehicle3.roof, True)
# Run the unit tests.
if __name__ == '__main__':
  unittest.main()

