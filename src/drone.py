from pathlib import Path

from rlbot.agents.hivemind.drone_agent import DroneAgent

# Dummy agent to call request the Python Hivemind.
class Drone(DroneAgent):
    hive_path = str(Path(__file__).parent / "hive.py")
    hive_key = "12345"
    hive_name = "SARPBC"
