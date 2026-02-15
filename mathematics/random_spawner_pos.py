from random import randint
from mathematics.vector import Vector2Int, Vector2

def random_spawner_position() -> Vector2:
    x = randint(-1000, 1000)
    y = randint(-1000, 1000)
    return Vector2Int(x, y).as_vector2