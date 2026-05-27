import json
import tkinter as tk
from tkinter import ttk, messagebox

from planner import cauta_ruta_directa, cauta_ruta_cu_schimbare
from validator import valideaza_date
from harta import arata_harta
from vizualizare_harta import arata_harta_generala

# =====================================
# MEMORARE ULTIMA RUTA
# =====================================
ultima_ruta = None

# =====================================
# CITIRE DATE
# =====================================
with open("routes.json", "r", encoding="utf-8") as file:
    routes = json.load(file)

toate_statiile = {}

for route in routes:
    for statie in route["statii"]:
        toate_statiile[statie.lower()] = statie


# =====================================
# FUNCTII
# =====================================
def calculeaza_ruta():
    global ultima_ruta

    plecare = combo_plecare.get().strip().lower()
    destinatie = combo_destinatie.get().strip().lower()

    if plecare in toate_statiile:
        plecare = toate_statiile[plecare]

    if destinatie in toate_statiile:
        destinatie = toate_statiile[destinatie]

    eroare = valideaza_date(plecare, destinatie, toate_statiile.values())

    if eroare:
        messagebox.showerror("Eroare", eroare)
        return

    rezultat.delete("1.0", tk.END)

    # =====================================
    # RUTA DIRECTA
    # =====================================
    ruta_directa = cauta_ruta_directa(routes, plecare, destinatie)

    if ruta_directa:
        ultima_ruta = {
            "tip": "directa",
            "linie": ruta_directa["linie"],
            "traseu": ruta_directa["traseu"]
        }

        text = f"""
✔ RUTA OPTIMA

Tip: Directa
Linie: {ruta_directa["linie"]}

Traseu:
{" -> ".join(ruta_directa["traseu"])}

Durata: {ruta_directa["durata"]} minute
Cost: {ruta_directa["cost"]} lei
"""
        rezultat.insert(tk.END, text)
        rezultat.tag_config("center", justify="center")
        rezultat.tag_add("center", "1.0", "end")
        return

    # =====================================
    # RUTA CU SCHIMBARE
    # =====================================
    ruta_schimbare = cauta_ruta_cu_schimbare(routes, plecare, destinatie)

    if ruta_schimbare:
        ultima_ruta = {
            "tip": "schimbare",
            "linie1": ruta_schimbare["linie1"],
            "traseu1": ruta_schimbare["traseu1"],
            "linie2": ruta_schimbare["linie2"],
            "traseu2": ruta_schimbare["traseu2"]
        }

        text = f"""
✔ RUTA OPTIMA

Tip: Cu schimbare

Linia 1: {ruta_schimbare["linie1"]}
{" -> ".join(ruta_schimbare["traseu1"])}

Schimbare la:
{ruta_schimbare["schimbare_la"]}

Linia 2: {ruta_schimbare["linie2"]}
{" -> ".join(ruta_schimbare["traseu2"])}

Durata Totala: {ruta_schimbare["durata"]} minute
Cost Total: {ruta_schimbare["cost"]} lei
"""
        rezultat.insert(tk.END, text)
        rezultat.tag_config("center", justify="center")
        rezultat.tag_add("center", "1.0", "end")
        return

    ultima_ruta = None

    messagebox.showwarning(
        "Ruta indisponibila",
        "Nu exista ruta directa sau cu schimbare intre statiile selectate."
    )


def reset():
    global ultima_ruta

    ultima_ruta = None

    combo_plecare.set("Selecteaza plecarea")
    combo_destinatie.set("Selecteaza destinatia")

    rezultat.delete("1.0", tk.END)

    rezultat.insert(
        tk.END ,
        "\n\nSelecteaza statiile dorite\nsi apasa 'Calculeaza Ruta'"
    )

    rezultat.tag_config(
        "center",
        justify="center",
        foreground="#888888"
    )

    rezultat.tag_add("center", "1.0", "end")


def inverseaza():
    p = combo_plecare.get()
    d = combo_destinatie.get()

    combo_plecare.set(d)
    combo_destinatie.set(p)


# =====================================
# HOVER EFFECT
# =====================================
def hover_in(widget, color):
    widget.config(bg=color)


def hover_out(widget, color):
    widget.config(bg=color)


# =====================================
# UI PRINCIPAL
# =====================================
root = tk.Tk()
root.title("🚌 Planificator Transport Studenti")
root.geometry("980x700")
root.configure(bg="#121212")
root.resizable(False, False)

# CARD CENTRAL
frame = tk.Frame(root, bg="#1e1e1e")
frame.place(relx=0.5, rely=0.5, anchor="center", width=900, height=630)

# TITLU
tk.Label(
    frame,
    text="Planificator Transport Studenti",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="#1e1e1e"
).pack(pady=20)

# PLECARE
tk.Label(
    frame,
    text="Statia de plecare",
    fg="#bbbbbb",
    bg="#1e1e1e",
    font=("Segoe UI", 11)
).pack()

combo_plecare = ttk.Combobox(
    frame,
    values=list(toate_statiile.values()),
    width=40,
    font=("Segoe UI", 12)
)
combo_plecare.pack(pady=8)
combo_plecare.set("Selecteaza plecarea")

# DESTINATIE
tk.Label(
    frame,
    text="Statia destinatie",
    fg="#bbbbbb",
    bg="#1e1e1e",
    font=("Segoe UI", 11)
).pack()

combo_destinatie = ttk.Combobox(
    frame,
    values=list(toate_statiile.values()),
    width=40,
    font=("Segoe UI", 12)
)
combo_destinatie.pack(pady=8)
combo_destinatie.set("Selecteaza destinatia")

# =====================================
# BUTOANE
# =====================================
buttons = tk.Frame(frame, bg="#1e1e1e")
buttons.pack(pady=20)

# CALCULEAZA
btn_calc = tk.Label(
    buttons,
    text="Calculeaza Ruta",
    bg="#00C853",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=10,
    cursor="hand2"
)
btn_calc.grid(row=0, column=0, padx=5)
btn_calc.bind("<Button-1>", lambda e: calculeaza_ruta())
btn_calc.bind("<Enter>", lambda e: hover_in(btn_calc, "#00E676"))
btn_calc.bind("<Leave>", lambda e: hover_out(btn_calc, "#00C853"))

# RESET
btn_reset = tk.Label(
    buttons,
    text="Reset",
    bg="#424242",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=10,
    cursor="hand2"
)
btn_reset.grid(row=0, column=1, padx=5)
btn_reset.bind("<Button-1>", lambda e: reset())
btn_reset.bind("<Enter>", lambda e: hover_in(btn_reset, "#616161"))
btn_reset.bind("<Leave>", lambda e: hover_out(btn_reset, "#424242"))

# INVERSEAZA
btn_swap = tk.Label(
    buttons,
    text="Inverseaza",
    bg="#1565C0",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=10,
    cursor="hand2"
)
btn_swap.grid(row=0, column=2, padx=5)
btn_swap.bind("<Button-1>", lambda e: inverseaza())
btn_swap.bind("<Enter>", lambda e: hover_in(btn_swap, "#1976D2"))
btn_swap.bind("<Leave>", lambda e: hover_out(btn_swap, "#1565C0"))

# RUTA PE HARTA
btn_harta = tk.Label(
    buttons,
    text="🧭 Ruta pe Harta",
    bg="#FF9800",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=10,
    cursor="hand2"
)
btn_harta.grid(row=0, column=3, padx=5)
btn_harta.bind("<Button-1>", lambda e: arata_harta(root, ultima_ruta))
btn_harta.bind("<Enter>", lambda e: hover_in(btn_harta, "#FFB74D"))
btn_harta.bind("<Leave>", lambda e: hover_out(btn_harta, "#FF9800"))

# RETEA GENERALA
btn_viz = tk.Label(
    buttons,
    text="🌍 Retea Transport",
    bg="#9C27B0",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=18,
    pady=10,
    cursor="hand2"
)
btn_viz.grid(row=0, column=4, padx=5)
btn_viz.bind("<Button-1>", lambda e: arata_harta_generala(root))
btn_viz.bind("<Enter>", lambda e: hover_in(btn_viz, "#BA68C8"))
btn_viz.bind("<Leave>", lambda e: hover_out(btn_viz, "#9C27B0"))

# =====================================
# REZULTAT
# =====================================
rezultat = tk.Text(
    frame,
    height=18,
    width=78,
    font=("Consolas", 11),
    bg="#2a2a2a",
    fg="white",
    bd=0,
    insertbackground="white"
)
rezultat.pack(pady=20)

rezultat.insert(
    tk.END,
    "\n\nSelecteaza statiile dorite\nsi apasa 'Calculeaza Ruta'"
)

rezultat.tag_config(
    "center",
    justify="center",
    foreground="#888888"
)

rezultat.tag_add("center", "1.0", "end")

# FOOTER
tk.Label(
    root,
    text="UPT Python Project 2026",
    fg="#777777",
    bg="#121212",
    font=("Segoe UI", 9)
).pack(side="bottom", pady=8)

# ENTER = CALCUL
root.bind("<Return>", lambda e: calculeaza_ruta())

root.mainloop()
