from rlbot.utils.structures.bot_input_struct import PlayerInput
import utils.car as car_module
import utils.matrix_utils as matrix_utils
import utils.physics_data_object as physics_data_object
from math import atan2
import utils.misc_tools as misc_tools


def drive(target: physics_data_object.PDO, car: car_module.Car) -> PlayerInput:
    controls = PlayerInput(throttle=1)
    relative_target = matrix_utils.localize_vector(target, car)
    target_angle = atan2(relative_target.y, relative_target.x)
    steer_value = misc_tools.clamp(1, -1, target_angle * 5)
    controls.steer = steer_value
    return controls
