from __future__ import annotations
from rlbot.utils.structures.game_data_struct import GameTickPacket


class BallTouch:
    def __init__(self, packet: GameTickPacket) -> None:
        touch_info = packet.game_ball.latest_touch
        self.player_name = touch_info.player_name
        self.hit_location = touch_info.hit_location
        self.team = touch_info.team
        self.player_index = touch_info.player_index
        self.time_seconds = touch_info.time_seconds

    def __repr__(self) -> str:
        return f"""
        player_name = {self.player_name}
        hit_location = {self.hit_location}
        team = {self.team}
        player_index = {self.player_index}
        time_seconds = {self.time_seconds}
        """

    def __eq__(self, other: BallTouch) -> bool:
        if (
            type(other) != BallTouch
            or self.player_name != other.player_name
            or self.hit_location != other.hit_location
            or self.team != other.team
            or self.player_index != other.player_index
            or self.time_seconds != other.time_seconds
        ):
            return False

        return True
