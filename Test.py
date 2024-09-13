import numpy as np

# Tạo hai vector A và B
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# Tính tích vô hướng (dot product)
dot_product = np.dot(A, B)

# Tính độ dài (norm) của từng vector
norm_A = np.linalg.norm(A)
norm_B = np.linalg.norm(B)

# Tính độ tương đồng cosine
cosine_similarity = dot_product / (norm_A * norm_B)

print(f"Độ tương đồng Cosine giữa A và B là: {cosine_similarity}")
