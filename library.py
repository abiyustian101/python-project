from time import sleep
import socket

PC_NAME = socket.gethostname()
def welcum_message():
    star = "*" * (len(PC_NAME) + 6)
    print(star)
    print(f"** {PC_NAME} **")
    print(star)
    
def exit_message():
    print("WARNING!!! PROGRAM AKAN SEGERA SHUTDOWN!!!")
    for i in range(1,4):
        print(f"{i}...")
        sleep(1)
    print("UNIVERSE PYBERT HAS BEEN SHUTDOWN! THANKS FOR PLAYING!")
    

if __name__ == "__main__":
    welcum_message()
    exit_message()