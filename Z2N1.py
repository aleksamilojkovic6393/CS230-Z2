import threading
import time

def download_file(filename):
    print(f"Preuzimanje fajla {filename}")

    time.sleep(3)

    print(f"Fajl {filename} je uspesno preuzet")

files = ["fajl1.txt", "fajl2.txt", "fajl3.txt"]

threads = []

for file in files:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Sva preuzimanja su zavrsena")
