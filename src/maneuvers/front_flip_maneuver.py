from maneuvers.base_maneuver import Maneuver
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.structures.bot_input_struct import PlayerInput
import utils.car as car_module
import utils.game_data as game_data


class FrontFlip(Maneuver):
    def __init__(self, car: car_module.Car, gd: game_data.GameData) -> None:
        super().__init__(car, gd)
        self.start_time = gd.current_time

    def update(self) -> PlayerInput:
        self.controls = PlayerInput(throttle=1.0)
        maneuver_time = self.gd.current_time - self.start_time
        if maneuver_time < 0.12:
            self.controls.jump = True
        elif maneuver_time < 0.2:
            self.controls.jump = False
        elif maneuver_time < 0.3:
            self.controls.jump = True
            self.controls.pitch = -1
        else:
            self.finished = True

        return self.controls
