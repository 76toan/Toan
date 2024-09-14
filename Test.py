import numpy as np

def nhap_toa_do(diem):
    try:
        x = input(f"Nhập tọa độ x của điểm {diem}: ")
        y = input(f"Nhập tọa độ y của điểm {diem}: ")
        z = input(f"Nhập tọa độ z của điểm {diem}: ")
        diem = np.array([x, y, z])
        return diem
    except ValueError:
        print("Vui lòng nhập số hợp lệ cho tọa độ!")

a = nhap_toa_do("A")
b = nhap_toa_do("B")
print(f"Tọa độ điểm A là: {a}")
print(f"Tọa độ điểm B là: {b}")

tich_vo_huong = np.dot(a, b)
print(f"Tích vô hướng của 2 vecto {a}, và {b} là: {tich_vo_huong}")

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)
print(f"Độ dài vecto a là: {norm_a}")
print(f"Độ dài vecto b là: {norm_b}")

cosin = tich_vo_huong / (norm_a * norm_b)

print(f"Cosin giữa 2 góc tạo bởi 2 vecto a và b là: {cosin}")