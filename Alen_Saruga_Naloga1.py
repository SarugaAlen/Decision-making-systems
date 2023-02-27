import csv
import matplotlib.pyplot as plt

print("Izračun osnovnih metod odločanja.\n")

def Pesimist(dict):
    largest_value = float('-inf')
    largest_key = None
    for key, value in dict.items():
        if value[0] > largest_value:
            largest_value = value[0]
            largest_key = key
    return f"{largest_key} ({largest_value})"


def Optimist(dict):
    largest_value = float('-inf')
    largest_key = None
    for key, value in dict.items():
        if value[1] > largest_value:
            largest_value = value[1]
            largest_key = key
    return f"{largest_key} ({largest_value})"


def Laplas(dict):
    largest_average = float('-inf')
    largest_key = None
    for key, value in dict.items():
        average = sum(value) / len(value)
        if average > largest_average:
            largest_average = average
            largest_key = key
    return f"{largest_key} ({int(largest_average)})"


def Savage(dict, header):

    v1 = float('-inf') #najslabsi izid najvecji
    v2 = float('-inf') #najboljsi izid najvecji

    for key, value in dict.items():
        if value[0] > v1:
            v1 = value[0]  #dobis najvecji value iz prve
    for key, value in dict.items():
        if value[1] > v2:
            v2 = value[1]  #dobis najvecji value iz druge

    data = [[],[]]  #2D list
    for key, value in dict.items():
        data[0].append(v1-value[0]) #appendas stevila odstete od najvecjega
        data[1].append(v2-value[1]) #appendas stevila odstete od najvecjega

    novDict = {header[i]: [int(data[0][i]), int(data[1][i])] for i in range(len(header))} #vse podatke vneses v nov dictionary

    najvecji = []
    for key, value in novDict.items():
        najvecji.append(max(value[0],value[1]))  #v list appendas najvecje value od obeh
        
        
    dictFinal = {header[i]: [int(najvecji[i])] for i in range(len(header))} #najvecje rezultate zapises v nov dictionary

    obzalovanje = float('inf')
    kljuc = None
    for key, value in dictFinal.items():  #dobis kljuc in vrednost obzalovanja
        if value[0] < obzalovanje:
           obzalovanje = value[0]
           kljuc = key
    return f"{kljuc} ({obzalovanje})"

def Herwitz(dict):
    list = []
    for key, value in dict.items():
        herwtiz = []
        for i in range(0, 11):
            h = i / 10
            herwtiz.append(round(h * value[0] + (1-h) * value[1], 2))
        list.append(herwtiz)
    return list











file = open("prodaja.csv")
csvreader = csv.reader(file)
print(f"Prebrana je bila datoteka {file.name}\n")
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
savage = Savage(dict, header)
print(f"Optimist:       {optimist}")
print(f"Pesimist:       {pesimist}")
print(f"Laplace:        {laplas}")
print(f"Savage:         {savage}")


print("\nHurwitzev kriterij:")
print("\n")

heading = header
heading.insert(0, "h")
head = (' '.join(heading))

herwitz = Herwitz(dict)
for row in herwitz:
    row.reverse()

print(head)
for i in range(0, 11):
    izpis = " "
    h = i / 10
    vrsta = " "
    for row in herwitz:
         vrsta += str(row[i]) + "\t"
    izpis = str(h) + "\t" + vrsta
    print(izpis)

for row in herwitz:
     plt.plot(row, [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

plt.show()

print(f"\nGraf Hurwitzovega kriterija je bil shranjen v datoteko graf.png.")
file.close()
