import json
from planner import cauta_ruta_directa, cauta_ruta_cu_schimbare
from validator import valideaza_date

with open("routes.json", "r", encoding="utf-8") as file:
    routes = json.load(file)

# dictionar pentru litere mici/mari
toate_statiile = {}

for route in routes:
    for statie in route["statii"]:
        toate_statiile[statie.lower()] = statie

print("=== Planificator Transport Studenti ===\n")

# input utilizator
plecare = input("Introdu statia de plecare: ").strip().lower()
destinatie = input("Introdu statia destinatie: ").strip().lower()

# transformam in forma corecta
if plecare in toate_statiile:
    plecare = toate_statiile[plecare]

if destinatie in toate_statiile:
    destinatie = toate_statiile[destinatie]

# validare
eroare = valideaza_date(plecare, destinatie, toate_statiile.values())

if eroare:
    print("\n" + eroare)
    exit()

# ruta directa
ruta_directa = cauta_ruta_directa(routes, plecare, destinatie)

if ruta_directa:
    print("\n=== Ruta Directa Gasita ===")
    print("Linie:", ruta_directa["linie"])
    print("Traseu:", " -> ".join(ruta_directa["traseu"]))
    print("Durata:", ruta_directa["durata"], "minute")
    print("Cost:", ruta_directa["cost"], "lei")

else:
    ruta_schimbare = cauta_ruta_cu_schimbare(routes, plecare, destinatie)

    if ruta_schimbare:
        print("\n=== Ruta cu Schimbare Gasita ===")

        print("\nLinia 1:", ruta_schimbare["linie1"])
        print("Traseu:", " -> ".join(ruta_schimbare["traseu1"]))

        print("\nSchimbare la:", ruta_schimbare["schimbare_la"])

        print("\nLinia 2:", ruta_schimbare["linie2"])
        print("Traseu:", " -> ".join(ruta_schimbare["traseu2"]))

        print("\nDurata totala:", ruta_schimbare["durata"], "minute")
        print("Cost total:", ruta_schimbare["cost"], "lei")

    else:
        print("\nNu exista ruta disponibila.")