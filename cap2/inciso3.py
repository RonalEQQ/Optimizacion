import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# iii) Función C = 1 / (1 - x)
x = sp.symbols('x')
f_x = 1 / (1 - x)
lim_f_inf = sp.limit(f_x, x, -sp.oo)
lim_f_sup = sp.limit(f_x, x, 1, dir='-')

# Resultado
results = {
    "C": {"infimum": lim_f_inf, "supremum": lim_f_sup},
}

print(results)

# Graficar intervalo C
x_vals = np.linspace(-5, 0.99, 400)
y_vals_f = 1 / (1 - x_vals)

plt.figure(figsize=(6,4))
plt.plot(x_vals, y_vals_f, 'b-', label='f(x) = 1/(1-x)')
plt.axhline(y=0, color='g', linestyle='--', label='Inf: 0')
plt.axvline(x=1, color='r', linestyle='--', label='Asintótica en x=1')
plt.title('Función C: f(x) = 1/(1-x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()