import math


# Compute the volume of the sphere
def print_volume(radius):
    volume = (4 / 3) * (math.pi * radius**3)
    print(volume)


print_volume(2)  # 33.510321638291124
print_volume(3)  # 113.09733552923254
print_volume(4)  # 268.082573106329
