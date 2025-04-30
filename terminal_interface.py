from calculateDebtFreeTime import calculate_debt_free_time_with_interest

def start():
    """Funktion til at starte beregningen."""
    print("\n--- Start Beregning ---")
    try:
        loan_amount = int(input("Indtast lånebeløb (kr): "))
        interest_rate = float(input("Indtast rente (%): ")) / 100  # Konverter procent til decimal
        monthly_payment = int(input("Indtast månedlig betaling (kr): "))

        # Kald funktionen fra calculateDebtFreeTime.py
        months = calculate_debt_free_time_with_interest(loan_amount, monthly_payment, interest_rate)
        print(f"\nDu vil være gældfri om {months /12} år.\n")
    except ValueError as e:
        print(f"Fejl: {e}")
    except Exception as e:
        print(f"Der opstod en uventet fejl: {e}")

def om_programmet():
    """Funktion til at vise information om programmet."""
    print("\n--- Om Programmet ---")
    print("Dette program beregner, hvor lang tid det vil tage at blive gældfri.")
    print("Du skal indtaste lånebeløb, rente og månedlig betaling.")
    print("Programmet bruger en simpel algoritme til at beregne antallet af måneder.\n")

def luk():
    """Funktion til at lukke programmet."""
    print("\nProgrammet lukkes. Tak for at bruge det!")
    exit()

def main():
    """Hovedmenuen for programmet."""
    while True:
        print("Velkommen til Gældsberegneren!")
        print("1. Start")
        print("2. Om Programmet")
        print("3. Luk")
        choice = input("Vælg en funktion (1-3): ")

        if choice == "1":
            start()
        elif choice == "2":
            om_programmet()
        elif choice == "3":
            luk()
        else:
            print("\nUgyldigt valg. Prøv igen.\n")

if __name__ == "__main__":
    main()