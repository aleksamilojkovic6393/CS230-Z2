import socket

HOST = '127.0.0.1'
PORT = 5000

KORISNICKO_IME = "admin"
LOZINKA = "1234"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server je pokrenut i ceka klijenta")

conn, addr = server.accept()
print("Povezan klijent:", addr)

korisnicko_ime = conn.recv(1024).decode()
lozinka = conn.recv(1024).decode()

with open("audit_log.txt", "a", encoding="utf-8") as log:
    if korisnicko_ime == KORISNICKO_IME and lozinka == LOZINKA:
        conn.send("Uspesna prijava.".encode())
        log.write(f"Korisnik '{korisnicko_ime}' se uspesno prijavio.\n")
    else:
        conn.send("Neuspesna prijava.".encode())
        log.write(f"Korisnik '{korisnicko_ime}' je uneo pogrese podatke.\n")

conn.close()
server.close()