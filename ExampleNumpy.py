import numpy as np

try:
    x1 = int(input("Nhập tọa độ x cho vecto 1: "))
    y1 = int(input("Nhập tọa độ x cho vecto 1: "))
    z1 = int(input("Nhập tọa độ x cho vecto 1: "))
    x2 = int(input("Nhập tọa độ x cho vecto 1: "))
    y2 = int(input("Nhập tọa độ x cho vecto 1: "))
    z2 = int(input("Nhập tọa độ x cho vecto 1: "))

except :
    pass


A = np.array([x1, y1, z1])
B = np.array([x2, y2, z2])

tichVoHuong = np.dot(A, B)

daiA = np.linalg.norm(A)
daiB = np.linalg.norm(B)

cosin = tichVoHuong / (daiA * daiB)

print(f"Cosin góc tạo bởi 2 vecto A và B là {cosin}")

