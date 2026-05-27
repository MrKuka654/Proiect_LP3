import tkinter as tk


def arata_harta_generala(root):
    fereastra = tk.Toplevel(root)
    fereastra.title("🌍 Vizualizare Retea Transport")
    fereastra.geometry("1000x650")
    fereastra.configure(bg="#121212")

    canvas = tk.Canvas(
        fereastra,
        width=1000,
        height=650,
        bg="#1e1e1e",
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)

    # TITLU
    canvas.create_text(
        500, 30,
        text="🌍 Vizualizare Generala Transport Studenti",
        fill="white",
        font=("Segoe UI", 22, "bold")
    )

    # LEGENDA
    canvas.create_text(
        850, 80,
        text="LEGENDA",
        fill="white",
        font=("Segoe UI", 14, "bold")
    )

    def legenda(y, culoare, text):
        canvas.create_rectangle(780, y-10, 800, y+10, fill=culoare, outline="")
        canvas.create_text(
            880, y,
            text=text,
            fill="white",
            font=("Segoe UI", 11)
        )

    legenda(120, "#00C853", "🚋 Tramvai")
    legenda(160, "#E53935", "🚍 Express")
    legenda(200, "#1E88E5", "🚌 Autobuz")
    legenda(240, "#8E24AA", "🚎 Troleibuz")

    def statie(x, y, nume):
        canvas.create_oval(x-8, y-8, x+8, y+8, fill="white", outline="")
        canvas.create_text(
            x,
            y+20,
            text=nume,
            fill="white",
            font=("Segoe UI", 10)
        )

    # =========================
    # Tramvai
    # =========================
    canvas.create_text(
        260, 90,
        text="🚋 Tramvai 4",
        fill="#00C853",
        font=("Segoe UI", 14, "bold")
    )

    canvas.create_line(120,130,580,130, fill="#00C853", width=6)

    statie(120,130,"Complex")
    statie(260,130,"Piata Maria")
    statie(420,130,"Centru")
    statie(580,130,"UPT")

    # =========================
    # Express
    # =========================
    canvas.create_text(
        260, 220,
        text="🚍 Express E2",
        fill="#E53935",
        font=("Segoe UI", 14, "bold")
    )

    canvas.create_line(120,260,580,260, fill="#E53935", width=6)

    statie(120,260,"Camin 4")
    statie(300,260,"Complex")
    statie(580,260,"UPT")

    # =========================
    # Autobuz
    # =========================
    canvas.create_text(
        260, 360,
        text="🚌 Autobuz 33",
        fill="#1E88E5",
        font=("Segoe UI", 14, "bold")
    )

    canvas.create_line(120,400,580,400, fill="#1E88E5", width=6)

    statie(120,400,"Gara")
    statie(300,400,"Complex")
    statie(420,400,"Centru")
    statie(580,400,"UPT")

    # =========================
    # Troleibuz
    # =========================
    canvas.create_text(
        260, 510,
        text="🚎 Troleibuz 15",
        fill="#8E24AA",
        font=("Segoe UI", 14, "bold")
    )

    canvas.create_line(120,550,580,550, fill="#8E24AA", width=6)

    statie(120,550,"Iulius Town")
    statie(280,550,"Libertatii")
    statie(430,550,"Centru")
    statie(580,550,"Medicina")