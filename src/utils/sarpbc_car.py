from dataclasses import dataclass
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.car as car
from typing import Type
from routines.base_routine import BaseRoutine
from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.agents.hivemind.python_hivemind import PythonHivemind


@dataclass
class BattleCar:
    def __init__(self, team: int, index: int, hivemind: Type[PythonHivemind]) -> None:
        self.index = index
        self.team = team
        self.hivemind = hivemind
        self.car = car.Car(team, index)
        self.routine = None

    def update_car(self, packet: GameTickPacket) -> None:
        self.car.update(packet)

    def get_controls(self) -> PlayerInput:
        return self.routine.update(self.hivemind.current_packet)
