import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

korisnicko_ime = input("Unesite korisničko ime: ")
lozinka = input("Unesite lozinku: ")

client.send(korisnicko_ime.encode())
client.send(lozinka.encode())

odgovor = client.recv(1024).decode()
print("Odgovor servera:", odgovor)

client.close()