print("Bienvenidos a el concierto de Zion & Lennox")
print("El precio de cada seccion es lo sigueinte: VIP = $170, Nivel Principal = $110, Club Seat = $70, Nivel Superior = $50")

VIP = int(input("¿Cuantos voletos vendidos en VIP?: "))
nivel_principal = int(input("¿Cuantos voletos vendidos en Nivel Principal?: "))
club_seat = int(input("¿Cuantos voletos vendidos en Club Seat?: "))
nivel_superior = int(input("¿Cuantos voletos vendidos en Nivel Superior?: "))

def VentasDeSecciones(VIP, nivel_principal, club_seat, nivel_superior):
    print(f"El precio de VIP es: {int(VIP) * 170}")
    print(f"El precio de Nive Principal es: {int(nivel_principal) * 110}")
    print(f"El precio de Club Seat es: {int(club_seat) * 70}")
    print(f"El precio de Nivel Superior es: {int(nivel_superior) * 50}")
print()
VentasDeSecciones(VIP, nivel_principal, club_seat, nivel_superior)
Ventas_VIP = VIP * 170
Ventas_NP = nivel_principal * 110
Ventas_CS = club_seat * 70
Ventas_NS = nivel_superior * 50
def TotalDeTickets(Ventas_VIP, Ventas_NP, Ventas_CS, Ventas_NS):
    print(f"El total de ventas de taquillas fue: ${int(Ventas_VIP) + int(Ventas_NP) + int(Ventas_CS) + int(Ventas_NS)}")
print()
TotalDeTickets(Ventas_VIP, Ventas_NP, Ventas_CS, Ventas_NS)