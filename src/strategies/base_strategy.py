from typing import Type
from rlbot.agents.hivemind.python_hivemind import PythonHivemind

# this class is the puppet master pulling all the strings, where the highest level of planning takes place.
class BaseStrategy:
    def __init__(self, hivemind: Type[PythonHivemind]) -> None:
        self.hivemind = hivemind

    def get_actions(self) -> dict:
        # This is the brains of the hivemind. Which bot should be going for the ball, getting boost?
        # Is it kickoff? Better assign the leading bot to a kickoff_maneuver! etc
        return {
            drone.index: drone.get_controls(self.hivemind.current_packet)
            for drone in self.hivemind.drones
        }
