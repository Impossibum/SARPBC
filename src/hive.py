from typing import Dict
from copy import deepcopy
import numpy as np
from rlbot.utils.structures.bot_input_struct import PlayerInput
from rlbot.utils.structures.game_data_struct import GameTickPacket
from rlbot.agents.hivemind.python_hivemind import PythonHivemind
from utils.physics_data_object import PDO
from utils.car import Car
from utils.sarpbc_car import BattleCar
from strategies.atba_swarm_strategy import ATBA_Swarm
from typing import Type
import utils.game_data as game_data


class SARPBC(PythonHivemind):
    def initialize_hive(self, packet: GameTickPacket) -> None:
        self.logger.info("Initialised!")
        self.drones = []
        index = next(iter(self.drone_indices))
        self.team = packet.game_cars[index].team
        self.game_data = game_data.GameData(self, packet)

        for index in self.drone_indices:
            self.drones.append(BattleCar(self.team, index, self))

        self.update_drones()
        self.strategy = ATBA_Swarm(self)

    def update_drones(self) -> None:
        for drone in self.drones:
            drone.update_car(self.game_data)

    def convert_ball_predictions(self) -> np.array:
        ball_prediction_struct = self.get_ball_prediction_struct()
        return np.ctypeslib.as_array(ball_prediction_struct.slices).view(self.dtype)[
            : ball_prediction_struct.num_slices
        ]

    def process_packet(self, packet: GameTickPacket) -> None:
        self.game_data.update(packet)
        self.update_drones()


    def get_outputs(self, packet: GameTickPacket) -> Dict[int, PlayerInput]:
        self.process_packet(packet)
        return self.strategy.get_actions()



if __name__ == "__main__":
    pass
