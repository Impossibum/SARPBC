from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.car as car_module


# short term maneuver intended to be called from within mechanics classes
class Maneuver:
    def __init__(self, car: car_module.Car, packet: GameTickPacket) -> None:
        self.car = car
        self.finished = False
        self.controls = PlayerInput()

    def update(self, *args, **kwargs) -> PlayerInput:
        self.finished = True
        return self.controls
