from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.car as car_module
import utils.game_data as game_data


# Medium-long term task which may include maneuvers or even other routines!
class BaseRoutine:
    def __init__(self, car: car_module.Car, gd: game_data.GameData) -> None:
        self.car = car
        self.finished = False
        self.controls = PlayerInput()
        self.maneuver = None
        self.routine = None
        self.gd = gd

    def update(self) -> PlayerInput:
        if self.maneuver and not self.maneuver.finished:
            return self.maneuver.update(self)
        elif self.routine and not self.routine.finished:
            return self.routine.update(self)
        else:
            return self.controls
