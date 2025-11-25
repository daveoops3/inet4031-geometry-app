import unittest
import sphere

class sphereTest(unittest.TestCase):

    #these need to be updated for a sphere
    def test_surfaceArea1(self):
        assert(sphere.surfaceArea(10) == 1256.6370614359173)
    
    def test_surfaceArea2(self):
        assert(sphere.surfaceArea(5) == 314.1592653589793)
        
    def test_surfaceArea3(self):
        assert(sphere.surfaceArea(0) == 0.0)

    def test_volume1(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_volume2(self):
        assert(sphere.volume(10) == 4188.790204786391)

    def test_volume3(self):
        assert(sphere.volume(0) == 0.0)

    #failing test
    #def test_volume3(self):
        #assert(sphere.volume(10,1000) == ??)


if __name__ == '__main__':
    unittest.main()
