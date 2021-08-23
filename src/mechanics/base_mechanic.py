from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.car as car_module


# Medium-long term task which may include maneuvers or even other mechanics!
class BaseMechanic:
    def __init__(self, car: car_module.Car, packet: GameTickPacket) -> None:
        self.car = car
        self.finished = False
        self.controls = PlayerInput()
        self.maneuver = None
        self.mechanic = None

    def update(self, packet: GameTickPacket) -> PlayerInput:
        if self.maneuver and not self.maneuver.finished:
            return self.maneuver.update(self, packet)
        elif self.mechanic and not self.mechanic.finished:
            return self.mechanic.update(self, packet)
        else:
            return self.controls
