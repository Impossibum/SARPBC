from __future__ import annotations
import numpy as np
from math import atan2, pi

try:
    import utils.misc_tools as misc_tools
except:
    import misc_tools


# Physics Data Object
class PDO:
    def __init__(self, content: np.array) -> None:
        self.data = content
        self.x = content[0]
        self.y = content[1]
        self.z = content[2]

    def __str__(self) -> str:
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        return self.data.size

    def __getitem__(self, index: int) -> float:
        return self.data[index]

    def raise_length_error(self, other: PDO, operation: str) -> None:
        raise ValueError(f"Tried to perform {operation} on 2 PDOs of differing lengths")

    def raise_cross_error(self) -> None:
        raise ValueError("Both PDOs need 3 terms for cross product")

    def __mul__(self, other: PDO) -> PDO:
        if len(self.data) == len(other.data):
            return PDO(np.multiply(self.data, other.data))
        else:
            self.raise_length_error(other, "multiplication")

    def __add__(self, other: PDO) -> PDO:
        if len(self.data) == len(other.data):
            return PDO(np.add(self.data, other.data))
        else:
            self.raise_length_error(other, "addition")

    def __sub__(self, other: PDO) -> PDO:
        if len(self.data) == len(other.data):
            return PDO(np.subtract(self.data, other.data))
        else:
            self.raise_length_error(other, "subtraction")

    def cross_product(self, other: PDO) -> PDO:
        if len(self.data) == 3 and len(other.data) == 3:
            return PDO(np.cross(self.data, other.data))

        else:
            self.raise_cross_error()

    def magnitude(self) -> float:
        return np.linalg.norm(self.data)

    def normalize(self) -> PDO:
        magnitude = self.magnitude()
        if magnitude != 0.0:
            return PDO(self.data / magnitude)
        else:
            return self

    def dot(self, other: PDO) -> np.ndarray:
        return np.dot(self.data, other.data)

    def scale(self, scalar) -> PDO:
        return PDO((self.data * scalar))

    def correction_to(self, ideal) -> float:
        current_in_radians = atan2(self[1], -self[0])
        ideal_in_radians = atan2(ideal[1], -ideal[0])

        correction = ideal_in_radians - current_in_radians
        if abs(correction) > pi:
            if correction < 0:
                correction += 2 * pi
            else:
                correction -= 2 * pi

        return correction

    def to_list(self) -> list:
        return self.data.tolist()

    def lerp(self, other_pdo: PDO, percent: float) -> PDO:
        percent = max((0, min((1, percent))))
        difference = self - other_pdo
        return self - difference.scale(percent)


def pdo_test() -> None:
    print("Running PDO unit test!\n-------------------------")
    a = PDO(np.array([1, 2, 3]))
    b = PDO(np.array([4, 5, 6]))
    print(f"Repr and str test passed?: {str(a) == 'x = 1, y = 2, z = 3'}")
    print(f"Len test passed?: {len(a) == 3}")
    print(f"Get_item test passed?: {a[1] == 2}")
    print(f"To_list test passed?: {a.to_list() == [1, 2, 3]}")
    print(f"Multiplication test passed?: {(a * b).to_list() == [4, 10, 18]}")
    print(f"Addition test passed?: {(a + b).to_list() == [5, 7, 9]}")
    print(f"Subtraction test passed?: {str(a - b) == 'x = -3, y = -3, z = -3'}")
    print(f"Cross Product test passed?: {str(a.cross_product(b)) == 'x = -3, y = 6, z = -3'}")
    print(
        f"Magnitude test passed?: {misc_tools.close_enough(a.magnitude(), 3.7416573867739413)}"
    )
    # print(
    #     f"Normalize test passed?: {a.normalize().to_list()==[0.2672612419124244, 0.5345224838248488, 0.8017837257372732]}"
    # )
    val1, val2, val3 = a.normalize().to_list()
    print(
        f"""Normalize test passed?: {misc_tools.close_enough(val1, 0.2672612419124244) and
                                     misc_tools.close_enough(val2, 0.5345224838248488) and
                                     misc_tools.close_enough(val3, 0.8017837257372732)}"""
    )
    print(f"Dot product test passed?: {a.dot(b) == 32}")
    print(
        f"Correction to test passed?: {misc_tools.close_enough(a.correction_to(b), 0.2110933332227467)}"
    )
    print(f"Scale test passed?: {a.scale(2).to_list() == [2, 4, 6]}")
    print(f"Lerp test passed?: {a.lerp(b, 0.5).to_list() == [2.5, 3.5, 4.5]}")


if __name__ == "__main__":
    pdo_test()
