"""
PJP - cvičení číslo 2
"""
import math


def is_convex(a, b, c, d):
    """
    Druhým úkolem je vytvořit funkci, která ze čtyř zadaných bodů určí,
    zda tvoří konvexní čtyřúhelník.

    Body na vstupu jsou zadávány jako tuple (x, y) kde x a y mohou být
    libovolná reálná čísla, tedy i záporná. Body mohou vytvořit čtyřúhelník,
    ale není to pravidlem.

    Je potřeba aby funkce hlídala i extrémní situace, jako například,
    že body čtyřúhelník vůbec nevytváří.
    """
    points = (a, b, c, d)

    if len({a, b, c, d}) != 4:
        return False

    for i, origin in enumerate(points):
        if get_angle(points[i + 1 if i < 3 else 0], origin, points[i - 1]) > 180:
            return False

    return True


def get_angle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    return ang + 360 if ang < 0 else ang


if __name__ == '__main__':
    is_convex((0.0, 0.0), (1.0, 0.0), (1.31, 0.79), (0.45, 0.66))
