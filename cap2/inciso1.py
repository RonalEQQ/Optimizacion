import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# i) Conjunto A
A = [8, 6, 7, 5, 3, 0, 9]
max_A = max(A)
min_A = min(A)

# Resultados
results = {
    "A": {"max": max_A, "min": min_A},
}
print(results)

# Graficar el conjunto A
plt.figure(figsize=(6,4))
plt.plot(A, 'ro-', label='Conjunto A')
plt.axhline(y=max_A, color='g', linestyle='--', label=f'Max: {max_A}')
plt.axhline(y=min_A, color='b', linestyle='--', label=f'Min: {min_A}')
plt.title('Conjunto A')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

