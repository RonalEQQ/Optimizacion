import matplotlib.pyplot as plt
import numpy as np

# Función para G(n)
def G(n):
    return (4*n**3 + 9*n**2 - 13*n) / 6

# Función para la aproximación A(n)
def A(n):
    return (2/3) * n**3

# Cálculo para n = 412
n = 412
G_412 = G(n)
A_412 = A(n)
error_percentual = abs((G_412 - A_412) / G_412) * 100

print(f"Inciso ii: La aproximación A(412) es {A_412:.2f}")
print(f"Error porcentual entre G(412) y A(412) es {error_percentual:.4f}%")

# Gráfico de G(n) y A(n) para un rango de n
n_values = np.arange(1, 500)
G_values = G(n_values)
A_values = A(n_values)

plt.figure(figsize=(8, 6))
plt.plot(n_values, G_values, label='G(n) - Exacto', color='blue')
plt.plot(n_values, A_values, label=r'A(n) - Aproximación $\frac{2}{3}n^3$', color='green')
plt.scatter(n, G_412, color='red', label=f'G(412) = {G_412:.2f}')
plt.scatter(n, A_412, color='orange', label=f'A(412) = {A_412:.2f}')
plt.title('Comparación de G(n) y A(n)')
plt.xlabel('n')
plt.ylabel('Operaciones')
plt.legend()
plt.grid(True)
plt.show()
