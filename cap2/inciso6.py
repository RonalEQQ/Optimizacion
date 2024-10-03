import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
# vi) Conjunto de primos
def prime_set(n):
    primes = [i for i in range(2, n) if sp.isprime(i)]
    return primes
# Probar para los primeros 100 números
primes_F = prime_set(100)
#Resultado
results = {
    "F": {"primes": primes_F}
}
print(results)
# Graficar intervalo E
primes_F = prime_set(100)
plt.figure(figsize=(6,4))
plt.plot(primes_F, 'go-', label='Primos')
plt.title('Conjunto de números primos')
plt.xlabel('Índice')
plt.ylabel('Número primo')
plt.legend()
plt.grid(True)
plt.show()