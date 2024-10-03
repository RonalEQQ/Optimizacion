import matplotlib.pyplot as plt
import numpy as np
# Función para G(n)
def G(n):
    return (4*n**3 + 9*n**2 - 13*n) / 6
# Función para la aproximación A(n)
def A(n):
    return (2/3) * n**3
# Encontrar el primer valor de n con error menor al 1%
n_min = None
n_values = np.arange(1, 1000)
error_percentual_values = []
for n in n_values:
    G_n = G(n)
    A_n = A(n)
    error_percentual = abs((G_n - A_n) / G_n) * 100
    error_percentual_values.append(error_percentual)
    if error_percentual < 1 and n_min is None:
        n_min = n
print(f"Inciso iii: El primer valor de n donde el error es menor al 1% es n = {n_min}")
# Gráfico del error porcentual
plt.figure(figsize=(8, 6))
plt.plot(n_values, error_percentual_values, label='Error porcentual', color='purple')
plt.axhline(y=1, color='red', linestyle='--', label='1% Error')
plt.scatter(n_min, error_percentual_values[n_min-1], color='orange', label=f'n = {n_min}')
plt.title('Error porcentual entre G(n) y A(n)')
plt.xlabel('n')
plt.ylabel('Error porcentual (%)')
plt.legend()
plt.grid(True)
plt.show()
