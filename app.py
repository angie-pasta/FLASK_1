"""
Pierwsza aplikacja Python w VS Code
"""

def przywitanie(imie):
    """Funkcja, która przywituje użytkownika"""
    return f"Cześć, {imie}! Witaj w Python!"


def main():
    """Główna funkcja aplikacji"""
    print("=" * 40)
    print("Moja pierwsza aplikacja Python!")
    print("=" * 40)
    
    # Wprowadzenie danych od użytkownika
    imie = input("\nJak się masz? Podaj swoje imię: ")
    
    # Wywołanie funkcji
    wiadomosc = przywitanie(imie)
    print("\n" + wiadomosc)
    
    # Prosta matematyka
    liczba1 = float(input("\nPodaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    
    suma = liczba1 + liczba2
    print(f"\nSuma: {liczba1} + {liczba2} = {suma}")


if __name__ == "__main__":
    main()
