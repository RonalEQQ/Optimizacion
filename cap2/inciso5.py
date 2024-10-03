import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# v) Secuencia E
def sequence_e(n):
    return 1 + (-1)**n / n
# Generar los primeros términos para observar comportamiento
E_values = [sequence_e(n) for n in range(1, 101)]
max_E = max(E_values)
min_E = min(E_values)
# Resultado
results = {
    "E": {"max": max_E, "min": min_E},
}
print(results)
# Graficar intervalo E
n_vals = np.arange(1, 100)
y_vals_e = 1 + (-1)**n_vals / n_vals
plt.figure(figsize=(6,4))
plt.plot(n_vals, y_vals_e, 'bo-', label='E = 1 + (-1)^n/n')
plt.axhline(y=2, color='g', linestyle='--', label='Sup: 2')
plt.axhline(y=0, color='r', linestyle='--', label='Inf: 0')
plt.title('Secuencia E = 1 + (-1)^n/n')
plt.xlabel('n')
plt.ylabel('E(n)')
plt.legend()
plt.grid(True)
plt.show()