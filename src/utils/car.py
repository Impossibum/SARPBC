from __future__ import annotations
import numpy as np
import utils.physics_data_object as physics_data_object
from dataclasses import dataclass
from rlbot.utils.structures.game_data_struct import GameTickPacket
import utils.matrix_utils as matrix_utils


@dataclass
class Car:
    def __init__(self, team: int, index: int) -> None:
        self.team = team
        self.index = index
        self.location = physics_data_object.PDO(np.array([0, 0, 0]))
        self.velocity = physics_data_object.PDO(np.array([0, 0, 0]))
        self.rotation = physics_data_object.PDO(np.array([0, 0, 0]))
        self.avelocity = physics_data_object.PDO(np.array([0, 0, 0]))
        self.boost_level = 0
        self.on_surface = True
        self.demolished = False
        self.super_sonic = False
        self.matrix = []
        self.current_speed = 1
        self.forward = []
        self.left = []
        self.up = []
        self.rotational_velocity = []

    def __str__(self) -> str:
        return f"""
        Car Object 
        Team: {self.team}
        Index: {self.index}
        Position: {self.location}
        Velocity: {self.velocity}
        Boost: {self.boost_level}"""

    def __repr__(self) -> str:
        return str(self)

    def update(self, packet: GameTickPacket) -> None:
        car = packet.game_cars[self.index]
        self.location = physics_data_object.PDO(
            np.array(
                [car.physics.location.x, car.physics.location.y, car.physics.location.z]
            )
        )
        self.velocity = physics_data_object.PDO(
            np.array(
                [car.physics.velocity.x, car.physics.velocity.y, car.physics.velocity.z]
            )
        )
        self.rotation = physics_data_object.PDO(
            np.array(
                [
                    car.physics.rotation.pitch,
                    car.physics.rotation.yaw,
                    car.physics.rotation.roll,
                ]
            )
        )
        self.avelocity = physics_data_object.PDO(
            np.array(
                [
                    car.physics.angular_velocity.x,
                    car.physics.angular_velocity.y,
                    car.physics.angular_velocity.z,
                ]
            )
        )
        self.boost_level = car.boost
        self.on_surface = car.has_wheel_contact
        self.super_sonic = car.is_super_sonic
        self.current_speed = self.velocity.magnitude()
        self.matrix = matrix_utils.rotator_to_matrix(self)
        self.forward, self.left, self.up = self.matrix
        self.rotational_velocity = matrix_utils.matrix_dot(self.matrix, self.avelocity)
