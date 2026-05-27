import tkinter as tk


def arata_harta(root, ruta=None):
    harta = tk.Toplevel(root)
    harta.title("🗺 Harta Transport")
    harta.geometry("1000x650")
    harta.configure(bg="#121212")

    canvas = tk.Canvas(
        harta,
        width=1000,
        height=650,
        bg="#1e1e1e",
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)

    canvas.create_text(
        500, 30,
        text="🗺 Harta Transport Studenti",
        fill="white",
        font=("Segoe UI", 22, "bold")
    )

    def statie(x, y, nume):
        canvas.create_oval(x-8, y-8, x+8, y+8, fill="white", outline="")
        canvas.create_text(
            x, y+20,
            text = nume,
            fill="white",
            font=("Segoe UI", 10)
        )

    def traseu_segmente(statii, coord, culoare, traseu_activ=None):
        # linie gri de baza
        for i in range(len(statii)-1):
            x1, y1 = coord[statii[i]]
            x2, y2 = coord[statii[i+1]]
            canvas.create_line(x1, y1, x2, y2, fill="#555555", width=3)

        # highlight activ
        if traseu_activ:
            for i in range(len(traseu_activ)-1):
                a = traseu_activ[i]
                b = traseu_activ[i+1]

                x1, y1 = coord[a]
                x2, y2 = coord[b]

                canvas.create_line(x1, y1, x2, y2, fill=culoare, width=7)

    # =========================
    # TRAMVAI
    # =========================
    tramvai = ["Complex", "Piata Maria", "Centru", "UPT"]
    coord_t = {
        "Complex": (120,130),
        "Piata Maria": (260,130),
        "Centru": (420,130),
        "UPT": (580,130)
    }

    active = None
    if ruta:
        if ruta["tip"] == "directa" and ruta["linie"] == "Tramvai 4":
            active = ruta["traseu"]
        elif ruta["tip"] == "schimbare":
            if ruta["linie1"] == "Tramvai 4":
                active = ruta["traseu1"]
            if ruta["linie2"] == "Tramvai 4":
                active = ruta["traseu2"]

    canvas.create_text(260,90,text="🚋 Tramvai 4",fill="#00C853",
                       font=("Segoe UI",14,"bold"))

    traseu_segmente(tramvai, coord_t, "#00C853", active)

    for s in tramvai:
        statie(*coord_t[s], s)

    # =========================
    # EXPRESS
    # =========================
    exp = ["Camin 4", "Complex", "UPT"]
    coord_e = {
        "Camin 4": (120,250),
        "Complex": (300,250),
        "UPT": (580,250)
    }

    active = None
    if ruta:
        if ruta["tip"] == "directa" and ruta["linie"] == "Express E2":
            active = ruta["traseu"]
        elif ruta["tip"] == "schimbare":
            if ruta["linie1"] == "Express E2":
                active = ruta["traseu1"]
            if ruta["linie2"] == "Express E2":
                active = ruta["traseu2"]

    canvas.create_text(260,210,text="🚍 Express E2",fill="#E53935",
                       font=("Segoe UI",14,"bold"))

    traseu_segmente(exp, coord_e, "#E53935", active)

    for s in exp:
        statie(*coord_e[s], s)

    # =========================
    # AUTOBUZ
    # =========================
    bus = ["Gara", "Complex", "Centru", "UPT"]
    coord_b = {
        "Gara": (120,370),
        "Complex": (300,370),
        "Centru": (420,370),
        "UPT": (580,370)
    }

    active = None
    if ruta:
        if ruta["tip"] == "directa" and ruta["linie"] == "Autobuz 33":
            active = ruta["traseu"]
        elif ruta["tip"] == "schimbare":
            if ruta["linie1"] == "Autobuz 33":
                active = ruta["traseu1"]
            if ruta["linie2"] == "Autobuz 33":
                active = ruta["traseu2"]

    canvas.create_text(260,330,text="🚌 Autobuz 33",fill="#1E88E5",
                       font=("Segoe UI",14,"bold"))

    traseu_segmente(bus, coord_b, "#1E88E5", active)

    for s in bus:
        statie(*coord_b[s], s)

    # =========================
    # TROLEIBUZ
    # =========================
    tro = ["Iulius Town", "Libertatii", "Centru", "Medicina"]
    coord_tr = {
        "Iulius Town": (120,510),
        "Libertatii": (280,510),
        "Centru": (430,510),
        "Medicina": (580,510)
    }

    active = None
    if ruta:
        if ruta["tip"] == "directa" and ruta["linie"] == "Troleibuz 15":
            active = ruta["traseu"]
        elif ruta["tip"] == "schimbare":
            if ruta["linie1"] == "Troleibuz 15":
                active = ruta["traseu1"]
            if ruta["linie2"] == "Troleibuz 15":
                active = ruta["traseu2"]

    canvas.create_text(260,470,text="🚎 Troleibuz 15",fill="#8E24AA",
                       font=("Segoe UI",14,"bold"))

    traseu_segmente(tro, coord_tr, "#8E24AA", active)

    for s in tro:
        statie(*coord_tr[s], s)
