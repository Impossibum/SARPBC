from strategies.base_strategy import BaseStrategy
from routines.atba_routine import ATBA
from typing import Type
from rlbot.agents.hivemind.python_hivemind import PythonHivemind


class ATBA_Swarm(BaseStrategy):
    def __init__(self, hivemind: Type[PythonHivemind]) -> None:
        super().__init__(hivemind)
        for drone in self.hivemind.drones:
            drone.routine = ATBA(drone.car, self.hivemind.current_packet)

    def get_actions(self) -> dict:
        # This is the brains of the hivemind. Which bot should be going for the ball, getting boost?
        # Is it kickoff? Better assign the leading bot to a kickoff_maneuver! etc
        return {
            drone.index: drone.get_controls()
            for drone in self.hivemind.drones
        }
