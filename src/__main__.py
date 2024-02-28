import csv
import functions as fn
import os
import program as prog
import pwinput
import sys
import time
    
def initialize_database():
    with open(PATH, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        database_init = {}
        for row in reader:
            index, companyName, businessNature, project, domicile, ownership, yearAcquired, status, totalAssets = row
            database_init.update({index: [index, companyName, businessNature, project, domicile, 
                                     ownership, yearAcquired, status, totalAssets]})
    return database_init

def update_database(table):
    with open(PATH, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";", lineterminator='\n')
        writer.writerows(table.values())

def main():
    global database
    while True:
        fn.main_menu()
        choice = fn.integer_validation('Silahkan masukkan nomor pilihan: ')
        if choice == 1:
            prog.read(database)
        elif choice == 2:
            authorization()
            prog.create(database)
        elif choice == 3:
            authorization()
            prog.update(database)
        elif choice == 4:
            authorization()
            prog.delete(database)
        elif choice == 5:
            break
        else:
            print('Masukkan pilihan yang sesuai.\n')
            continue
        update_database(database)

def authorization():
    fn.clear_screen()
    attempt = 0
    while attempt < 3:
        username = input('Silahkan masukkan Username anda: ')
        password = pwinput.pwinput(prompt = 'Silahkan masukkan Password anda: ', mask = '*')
        if username == 'admin' and password == '1234':
            fn.clear_screen()
            print('''Anda berhasil masuk.
Saat ini anda sedang mengakses Database Entitas Anak PT Bumi Serpong Damai Tbk.\n''')
            break
        else:
            attempt += 1
            print(f'''Username/Password anda salah.
Masukkan Username/Password yang sesuai. (Percobaan ke-{attempt})\n''')
            continue
    else:
        print(f'''Username/Password anda salah.
Tampilan akan beralih ke menu utama.''')
        time.sleep(4)
        fn.clear_screen()
        main()

if __name__ == '__main__':
    fn.clear_screen()

    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/db.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/db.csv') 

    database = initialize_database()
    print('Selamat datang di BSDApp\n')
    main()