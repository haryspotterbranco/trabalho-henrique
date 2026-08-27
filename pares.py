pares, impares, primos = [], [], []

for n in range(1, 1001):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    
    if n > 1:
        e_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                e_primo = False
                break
        if e_primo:
            primos.append(n)

# Exibe os números organizados, separados por vírgula
print("NÚMEROS ORGANIZADOS")
print("-" * 25)
print(f"Pares:   {', '.join(map(str, pares))}")
print(f"Ímpares: {', '.join(map(str, impares))}")
print(f"Primos:  {', '.join(map(str, primos))}")
