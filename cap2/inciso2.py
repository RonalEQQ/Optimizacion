import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# ii) Intervalo B
def interval_b(a, b):
    return {"min": min(a, b), "max": max(a, b)}

# Resultado
results = {
    "B": interval_b,  # Asumir valores a y b al llamar la función
}

print(results)

# Graficar intervalo B
a, b = 2, 5  # Puedes cambiar estos valores para diferentes intervalos
interval = [a, b]
plt.figure(figsize=(6,4))
plt.plot(interval, 'bo-', label=f'Intervalo [{a}, {b}]')
plt.axhline(y=max(interval), color='g', linestyle='--', label=f'Max: {max(interval)}')
plt.axhline(y=min(interval), color='r', linestyle='--', label=f'Min: {min(interval)}')
plt.title(f'Intervalo B = [{a}, {b}]')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()

