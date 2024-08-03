maxTemp = 102.5
temp = float(input("Temp: "))

while temp > maxTemp:
    print("turunkan termostat, menunggu selama 5 menit, dan memasukkan suhu baru.")
    temp = float(input("Temp: "))

print("suhu dapat diterima dan untuk memeriksa lagi dalam 15 menit.")