
import unittest

from main import *

from map.tile import Tile

from map.map import Map

import settings

app = QApplication(sys.argv)
class CreationError(Exception):
    def __init__(self, message):
        super(CreationError, self).__init__(message)

class Test(unittest.TestCase):

    def test_correct_tile(self):
        tile = Tile(0,640, settings.TILE_FLOOR)
        self.assertTrue(tile.is_walkable())


    def test_map_file_load(self):
       
        self.assertIsInstance(Map(settings.MAP_FILES[0]), Map)
        
        self.assertRaises(Exception, Map('y2_2022_05868_platformer\code\scores.txt'))
    

if __name__ == '__main__':
    unittest.main()