import main

def menu_makanan():
    print()
def start():
    while True:
        print("Ini warung madura! Siap melayani 24 jam")
    
    
        play_again = input("Apakah kamu mau kembali ke menu? [y/n] ")
        if play_again == 'y':
            main.menu()
            
if __name__ == "__main__":
    start()