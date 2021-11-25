print(f"Bienvenido a la aplicación Calculadora de Fibonacci\n")
fibo = int(input(f"¿Cuántos dígitos de la secuencia de Fibonacci le gustaría calcular?  "))
print(f"\nLos primeros {fibo} números de la secuencia de fibonacci son:\n")

nums_fibo = [1,1]
golden_ratio = []

for i in range(1,fibo+1):
    if i == 1 or i == 2:
        print(f"{i} --> {nums_fibo[0]}")
    else:
        fibo_next = nums_fibo[len(nums_fibo)-1] + nums_fibo[len(nums_fibo)-2]
        nums_fibo.append(fibo_next)

        print(f"{i} --> {nums_fibo[len(nums_fibo)-1]}")

print(f"\nLos valores de proporción áurea correspondientes son:\n")

for i in range(0,fibo-1):
    golden_next = nums_fibo[i+1] / nums_fibo[i]
    golden_ratio.append(golden_next)
    print(f"{i+1} --> {golden_ratio[len(golden_ratio)-1]}")
    
print(f"\nLa proporción de términos de Fibonacci consecutivos se acerca a Phi; 1.618\n") 