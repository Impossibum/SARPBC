from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.car as car_module
import utils.game_data as game_data


# short term maneuver intended to be called from within mechanics classes
class Maneuver:
    def __init__(self, car: car_module.Car, gd: game_data.GameData) -> None:
        self.car = car
        self.gd = gd
        self.finished = False
        self.controls = PlayerInput()

    def update(self, *args, **kwargs) -> PlayerInput:
        self.finished = True
        return self.controls
