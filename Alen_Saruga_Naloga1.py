import csv

print("Izračun osnovnih metod odločanja.")


def Pesimist(dict):
    largest_value = float('-inf')
    largest_key = None
    for key, value in dict.items():
        if value[0] > largest_value:
            largest_value = value[0]
            largest_key = key
    key_and_value = f"{largest_key} ({largest_value})"
    return key_and_value


def Optimist(dict):
    largest_value = float('-inf')
    largest_key = None
    for key, value in dict.items():
        if value[1] > largest_value:
            largest_value = value[1]
            largest_key = key
    key_and_value = f"{largest_key} ({largest_value})"
    return key_and_value


def Laplas(dict):
    largest_average = float('-inf')
    largest_key = None
    for key, value in dict.items():
        average = sum(value) / len(value)
        if average > largest_average:
            largest_average = average
            largest_key = key
    return f"{largest_key} ({int(largest_average)})"


def Savage(dict):
    return 0


file = open("prodaja.csv")
csvreader = csv.reader(file)
print(f"Prebrana je bila datoteka {file.name}")
data = []
for i,row in enumerate(csvreader):
    if i >= 3:
        break
    data.append(row[1:])

header = data[0]
alternativa1 = data[1]
alternativa2 = data[2]

dict = {header[i]: [int(alternativa1[i]), int(alternativa2[i])] for i in range(len(header))}

optimist = Optimist(dict)
pesimist = Pesimist(dict)
laplas = Laplas(dict)
savage = Savage(dict)
print(f"Optimist:       {optimist}")
print(f"Pesimist:        {pesimist}")
print(f"Laplace:           {laplas}")
print(f"Savage:             {savage}")

file.close()
