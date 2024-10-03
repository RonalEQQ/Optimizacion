import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# iv) Función D = 1 / (1 - x^2)
x = sp.symbols('x')
g_x = 1 / (1 - x**2)
lim_g_inf = sp.limit(g_x, x, -1, dir='-')
lim_g_sup = sp.limit(g_x, x, 1, dir='-')
# Resultado
results = {
    "D": {"infimum": lim_g_inf, "supremum": lim_g_sup},
}
print(results)
# Graficar intervalo D
x_vals_g = np.linspace(-0.99, 0.99, 400)
y_vals_g = 1 / (1 - x_vals_g**2)
plt.figure(figsize=(6,4))
plt.plot(x_vals_g, y_vals_g, 'r-', label='g(x) = 1/(1-x^2)')
plt.axhline(y=0, color='g', linestyle='--', label='Inf: 0')
plt.axvline(x=-1, color='b', linestyle='--', label='Asintótica en x=-1')
plt.axvline(x=1, color='b', linestyle='--', label='Asintótica en x=1')
plt.title('Función D: g(x) = 1/(1-x^2)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.grid(True)
plt.show()