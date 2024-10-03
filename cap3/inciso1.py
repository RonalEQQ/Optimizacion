import matplotlib.pyplot as plt
import numpy as np

# Función para G(n)
def G(n):
    return (4*n**3 + 9*n**2 - 13*n) / 6

# Cálculo para n = 412
n = 412
G_412 = G(n)
print(f"Inciso i: El número exacto de operaciones para G(412) es {G_412:.2f}")

# Gráfico de G(n) para un rango de n
n_values = np.arange(1, 500)
G_values = G(n_values)

plt.figure(figsize=(8, 6))
plt.plot(n_values, G_values, label='G(n)', color='blue')
plt.scatter(n, G_412, color='red', label=f'G(412) = {G_412:.2f}')
plt.title('Número exacto de operaciones G(n)')
plt.xlabel('n')
plt.ylabel('Operaciones G(n)')
plt.legend()
plt.grid(True)
plt.show()
