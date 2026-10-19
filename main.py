from library import welcum_message, exit_message
from games import pybert
from tools import warung
import sys

def menu():
    user_option = int(input("Menu program:\n1. PYBERT GAMES\n2. Warung Kecil\n3. Exit\n\nSilahkan dipilih masseeh!: "))
    if user_option == 1:
        pybert.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_message()
    else:
        print("Silahkan pilih dari menu diatas atuh mas!")
def main():
    welcum_message()
    menu()

if __name__ == "__main__":
    main()