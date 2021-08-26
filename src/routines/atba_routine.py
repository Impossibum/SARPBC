import numpy as np
from routines.base_routine import BaseRoutine
from maneuvers.front_flip_maneuver import FrontFlip
from utils.physics_data_object import PDO
from utils.simple_drive import drive
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.utils.structures.bot_input_struct import PlayerInput
import utils.car as car_module
import utils.game_data as game_data


class ATBA(BaseRoutine):
    def __init__(self, car: car_module.Car, gd: game_data.GameData) -> None:
        super().__init__(car, gd)

    def update(self) -> PlayerInput:
        if self.maneuver and not self.maneuver.finished:
            return self.maneuver.update()
        target = PDO(
            np.array(
                [
                    self.gd.packet.game_ball.physics.location.x,
                    self.gd.packet.game_ball.physics.location.y,
                    self.gd.packet.game_ball.physics.location.z,
                ]
            )
        )
        controls = drive(target, self.car)
        if not self.car.super_sonic and self.car.on_surface and abs(controls.steer) < 0.1:

            if self.car.boost_level > 0:
                controls.boost = True
            elif self.car.current_speed > 1000:
                self.maneuver = FrontFlip(self.car, self.gd)
        return controls
