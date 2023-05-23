# input user
n = int(input("Masukkan n: "))
bilangan_input = set() # siapkan set kosong

# minta input bilangan
for i in range(n):
    bilangan = int(input("Masukkan bilangan: "))
    bilangan_input.add(bilangan)

print(f"Input anda memiliki {len(bilangan_input)} bilangan unik")
print(f"Bilangan unik yang anda masukkan adalah {bilangan_input}")
print(f"Bilangan terbesar adalah {max(bilangan_input)}")
print(f"Bilangan terkecil adalah {min(bilangan_input)}")