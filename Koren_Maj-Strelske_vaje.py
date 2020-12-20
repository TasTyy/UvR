import math

v = float(input("Vpiši hitrost krogle: "))
k = int(input("Vpiši kot pod katerim je krogla izstreljena: "))
print("Korgla bo letela", (v * v * math.sin(math.radians(2 * k)) / 10), "m.")