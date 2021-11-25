print("Welcome to the Binary/Hexadecimal")
nums = input("Compute binary and hexadecimal values up to the following decimal number:  ")
print("Generating lists....complete!\n")
print("Using slices, we will now show a portion of each list.")

start_num = int(input("What decimal number would you like to start at:  "))
stop_num = int(input("What decimal number would you like to stop at:  "))
lista_nums = range(1,int(nums)+1)

# Creación listas
bin_list = []
hex_list = []

for num in lista_nums:
    bin_list.append(bin(num))
    hex_list.append(hex(num))

# Valores decimales
print(f"\nDecimal values from {start_num} to {stop_num}")
for dec_num in range(start_num-1,stop_num):
    print(f"{lista_nums[dec_num]}")

# Valores binarios
print(f"\nBinary values from {start_num} to {stop_num}")
for bin_num in range(start_num-1,stop_num):
    print(f"{bin_list[bin_num]}")

# Valores Hexadecimales
print(f"\nHexadecimal values from {start_num} to {stop_num}")
for hex_num in range(start_num-1,stop_num):
    print(f"{hex_list[hex_num]}")

stop = input(f"\nPress Enter to see values from 1 to {nums}")

print("\n Decimal---Binary---Hexadecimal\n------------------------------")
for nums in range(0,int(nums)):
    print(f" {lista_nums[nums]} ---- {bin_list[nums]} ---- {hex_list[nums]}")