from __future__ import annotations
import numpy as np
import utils.physics_data_object as physics_data_object
import utils.car as car_module
from math import cos, sin


def rotator_to_matrix(
    car_object: car_module.Car,
) -> [physics_data_object.PDO, physics_data_object.PDO, physics_data_object.PDO]:
    r = car_object.rotation
    CR = cos(r[2])
    SR = sin(r[2])
    CP = cos(r[0])
    SP = sin(r[0])
    CY = cos(r[1])
    SY = sin(r[1])

    matrix = [
        physics_data_object.PDO(np.array([CP * CY, CP * SY, SP])),
        physics_data_object.PDO(
            np.array([CY * SP * SR - CR * SY, SY * SP * SR + CR * CY, -CP * SR])
        ),
        physics_data_object.PDO(
            np.array([-CR * CY * SP - SR * SY, -CR * SY * SP + SR * CY, CP * CR])
        ),
    ]

    return matrix


def matrix_dot(
    _matrix: [
        physics_data_object.PDO,
        physics_data_object.PDO,
        physics_data_object.PDO,
    ],
    PO: physics_data_object.PDO,
) -> np.array:
    return physics_data_object.PDO(
        np.array(
            [
                _matrix[0].dot(PO),
                _matrix[1].dot(PO),
                _matrix[2].dot(PO),
            ]
        )
    )


def localize_vector(
    target_object: physics_data_object.PDO, our_object: car_module.Car
) -> physics_data_object.PDO:
    x = (target_object - our_object.location).dot(our_object.matrix[0])
    y = (target_object - our_object.location).dot(our_object.matrix[1])
    z = (target_object - our_object.location).dot(our_object.matrix[2])
    return physics_data_object.PDO(np.array([x, y, z]))


def localize_rotation(
    target_rotation: physics_data_object.PDO, car: car_module.Car
) -> physics_data_object.PDO:
    return physics_data_object.PDO(
        np.array(
            [
                target_rotation.dot(car.forward),
                target_rotation.dot(car.left),
                target_rotation.dot(car.up),
            ]
        )
    )


def to_local(
    target: physics_data_object.PDO, car: car_module.Car
) -> physics_data_object.PDO:
    return localizeVector(target, car)


if __name__ == "__main__":
    pass
