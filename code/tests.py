import unittest

from player import Player

from map.map import Map

from map.tile import Tile

import settings
class CreationError(Exception):
    def __init__(self, message):
        super(CreationError, self).__init__(message)

class Test(unittest.TestCase):

    def correct_tile(self):
        tile = Tile(0,640, settings.TILE_FLOOR)
        walkable = True
        self.assertEqual(walkable, tile.is_walkable())



    def map_file_load(self):
        
        try:
           Map.readMap('y2_2022_05868_platformer\code\map\mapSetting.txt')
        except CreationError:
            self.fail("Unable to load map")


    def player_created(self):
        pass
    