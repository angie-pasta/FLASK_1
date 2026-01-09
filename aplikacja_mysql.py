"""
Aplikacja do zarządzania użytkownikami - MySQL
"""

from database import BazaDanych


def tworz_tabele(baza):
    """Utwórz tabelę użytkowników"""
    zapytanie = """
    CREATE TABLE IF NOT EXISTS uzytkownicy (
        id INT AUTO_INCREMENT PRIMARY KEY,
        imie VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        wiek INT,
        data_rejestracji TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    baza.wykonaj_operacje(zapytanie)


def dodaj_uzytkownika(baza, imie, email, wiek):
    """Dodaj nowego użytkownika"""
    zapytanie = "INSERT INTO uzytkownicy (imie, email, wiek) VALUES (%s, %s, %s)"
    return baza.wykonaj_operacje(zapytanie, (imie, email, wiek))


def wyswietl_uzytkownikow(baza):
    """Wyświetl wszystkich użytkowników"""
    zapytanie = "SELECT id, imie, email, wiek FROM uzytkownicy"
    wyniki = baza.wykonaj_zapytanie(zapytanie)
    
    if wyniki:
        print("\n" + "=" * 60)
        print("LISTA UŻYTKOWNIKÓW")
        print("=" * 60)
        for wiersz in wyniki:
            print(f"ID: {wiersz[0]} | Imię: {wiersz[1]} | Email: {wiersz[2]} | Wiek: {wiersz[3]}")
        print("=" * 60 + "\n")
    else:
        print("✗ Brak użytkowników w bazie danych.\n")


def szukaj_uzytkownika(baza, email):
    """Szukaj użytkownika po emailu"""
    zapytanie = "SELECT id, imie, email, wiek FROM uzytkownicy WHERE email = %s"
    wyniki = baza.wykonaj_zapytanie(zapytanie, (email,))
    
    if wyniki:
        wiersz = wyniki[0]
        print(f"\n✓ Znaleziono: ID: {wiersz[0]}, Imię: {wiersz[1]}, Email: {wiersz[2]}, Wiek: {wiersz[3]}\n")
    else:
        print(f"\n✗ Nie znaleziono użytkownika z emailem: {email}\n")


def usun_uzytkownika(baza, user_id):
    """Usuń użytkownika po ID"""
    zapytanie = "DELETE FROM uzytkownicy WHERE id = %s"
    return baza.wykonaj_operacje(zapytanie, (user_id,))


def menu():
    """Główne menu aplikacji"""
    baza = BazaDanych(
        host="localhost",
        user="root",
        password="",  # Tutaj wpisz hasło do MySQL
        database="aplikacja_python"
    )
    
    # Nawiąż połączenie
    if not baza.polacz():
        print("Nie mogę się połączyć z bazą danych!")
        return
    
    # Utwórz tabelę
    tworz_tabele(baza)
    
    while True:
        print("\n" + "=" * 40)
        print("MENU GŁÓWNE")
        print("=" * 40)
        print("1. Dodaj użytkownika")
        print("2. Wyświetl wszystkich użytkowników")
        print("3. Szukaj użytkownika")
        print("4. Usuń użytkownika")
        print("5. Wyjdź")
        print("=" * 40)
        
        wybor = input("Wybierz opcję (1-5): ").strip()
        
        if wybor == "1":
            print("\n--- DODAWANIE UŻYTKOWNIKA ---")
            imie = input("Podaj imię: ").strip()
            email = input("Podaj email: ").strip()
            try:
                wiek = int(input("Podaj wiek: ").strip())
                dodaj_uzytkownika(baza, imie, email, wiek)
            except ValueError:
                print("✗ Wiek musi być liczbą!")
        
        elif wybor == "2":
            wyswietl_uzytkownikow(baza)
        
        elif wybor == "3":
            email = input("\nPodaj email do wyszukania: ").strip()
            szukaj_uzytkownika(baza, email)
        
        elif wybor == "4":
            try:
                user_id = int(input("\nPodaj ID użytkownika do usunięcia: ").strip())
                usun_uzytkownika(baza, user_id)
            except ValueError:
                print("✗ ID musi być liczbą!")
        
        elif wybor == "5":
            print("\n✓ Do widzenia!")
            break
        
        else:
            print("✗ Nieprawidłowa opcja! Spróbuj ponownie.")
    
    # Zamknij połączenie
    baza.rozlacz()


if __name__ == "__main__":
    menu()
