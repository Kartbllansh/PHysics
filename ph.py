import numpy as np
import math

def calc_velocity_after_collision(v1, v2, m1, m2, theta):
    """
    This function calculates the velocities of v1 and v2 after the collision using the given masses and collision angle
    :param v1: Velocity of object 1 before collision
    :param v2: Velocity of object 2 before collision
    :param m1: Mass of object 1
    :param m2: Mass of object 2
    :param theta: Collision angle in radians
    :return: tuple of velocities for v1 and v2 after collision
    """

    # Calculate the normal and tangential components of v1 and v2 before collision
    vn1 = v1 * math.cos(theta)
    vt1 = v1 * math.sin(theta)
    vn2 = v2 * math.cos(theta)
    vt2 = v2 * math.sin(theta)

    # Calculate the normal and tangential components of v1 and v2 after collision
    vn1f = ((m1 - m2) * vn1 + 2 * m2 * vn2) / (m1 + m2)
    vn2f = ((m2 - m1) * vn2 + 2 * m1 * vn1) / (m1 + m2)
    vt1f = vt1
    vt2f = vt2

    # Calculate the final velocities of v1 and v2 after collision
    v1f = math.sqrt(vn1f ** 2 + vt1f ** 2)
    v2f = math.sqrt(vn2f ** 2 + vt2f ** 2)

    # Calculate the final angle of v1 and v2 after collision
    if vn1f != 0:
        angle1_f = math.atan(vt1f / vn1f)
    else:
        angle1_f = math.pi / 2
    if vn2f != 0:
        angle2_f = math.atan(vt2f / vn2f)
    else:
        angle2_f = math.pi / 2

    return v1f, v2f, angle1_f, angle2_f

# Example usage
v1_before = 10
v2_before = 5
m1 = 2
m2 = 1
theta = math.pi / 4
v1_after, v2_after, angle1_after, angle2_after = calc_velocity_after_collision(v1_before, v2_before, m1, m2, theta)
print("Object 1 new velocity: ", v1_after)
print("Object 2 new velocity: ", v2_after)
print("Angle of Object 1 after collision:", angle1_after)
print("Angle of Object 2 after collision:", angle2_after)