from rlbot.agents.hivemind.python_hivemind import PythonHivemind
from rlbot.utils.structures.game_data_struct import GameTickPacket
from utils.ball_touch import BallTouch
from typing import Type
import numpy as np

class GameData:
    def __init__(self, hivemind: Type[PythonHivemind], packet: GameTickPacket):
        self.dtype = [
            (
                "physics",
                [
                    ("location", "<f4", 3),
                    ("rotation", [("pitch", "<f4"), ("yaw", "<f4"), ("roll", "<f4")]),
                    ("velocity", "<f4", 3),
                    ("angular_velocity", "<f4", 3),
                ],
            ),
            ("game_seconds", "<f4"),
        ]
        self.hivemind = hivemind
        self.packet = packet
        self.field_info = hivemind.get_field_info()
        self.ball_predictions = self.convert_ball_predictions()
        self.last_touch = BallTouch(packet)
        self.current_time = packet.game_info.seconds_elapsed
        self.last_time = 0
        self.delta_time = 1 / 120


    def convert_ball_predictions(self) -> np.array:
        ball_prediction_struct = self.hivemind.get_ball_prediction_struct()
        return np.ctypeslib.as_array(ball_prediction_struct.slices).view(self.dtype)[
               : ball_prediction_struct.num_slices
               ]

    def update(self, packet: GameTickPacket):
        self.packet = packet
        self.ball_predictions = self.convert_ball_predictions()
        self.last_touch = BallTouch(packet)
        self.last_time, self.current_time = self.current_time, packet.game_info.seconds_elapsed
        self.delta_time = self.current_time-self.last_time





if __name__ == "__main__":
    pass