import random
import time
import main
def start():
    while True:
        pybert_choices = random.randint(1,4)

        bentuk_lobang = '|_|' # INI TEMPLATE DARI SONO
        lobang_kosong = [bentuk_lobang] * 4

        lobang_kosong_asli = ' '.join(lobang_kosong)

        lobang = lobang_kosong.copy() # INI YANG ADA PYBERTNYA 
        lobang[pybert_choices - 1] = "|>_<|"

        lobang_asli = ' '.join(lobang)

        print("Halo! Nama saya pybert! program yang terjebak di PYCUY universe ini!")

        print(f"Halo Pengembara! apakah kamu sudah siap untuk bermain PYCUY GAMES HOLES GUESS YANG SPEKTAKULER INI!?")

        print(f'BERIKUT ADA 4 LOBANG YANG SALAH SATUNYA TERDAPAT TIKUS YANG HARUS DIBASMI! \nPerhatikan dengan detail! \n{lobang_kosong_asli}')

        input_user = int(input("Ada di lobang manakah tikusnya berada? "))

        while input_user not in [1,2,3,4]:
            input_user = int(input("Masukkan terlebih dahulu nomor yang anda pilih!: "))

        if input_user == pybert_choices:
            print(f"{lobang_asli} \n SELAMAT Pengembara! RUPANYA KAMU SEORANG PERAMAL TIKUS! TIKUSNYA BERADA DI LOBANG {pybert_choices} dan kamu menebak tikusnya ada di {input_user}!")
        else:
            print(f"{lobang_asli} \n HAHAHAHAHAAHAAAA! CUPU KAMU!!! GITU AJA NDK TAU KALAU SI TIKUS ADA DI LOBANG {pybert_choices}! MALAH KAMU PILIH {input_user}! LAIN KALI OTAK DIPAKAI DEK!!")
            
        main_lagi = input("Apakah kamu mau pergi dari universe ini? [y/n]: ")
        if main_lagi == "y":
            # print("SAMPAI JUMPA DI UNIVERSE LAINNYA! PYBERT AKAN SELALU MENUNGGU MU!")
            # return
            main.menu()
        
    

if __name__ == "__main__":
    start()