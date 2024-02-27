import csv
import functions as fn
import os
import program as prog
import sys
    
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
            fn.clear_screen()
            prog.read(database)
        elif choice == 2:
            fn.clear_screen()
            prog.create(database)
        elif choice == 3:
            fn.clear_screen()
            prog.update(database)
        elif choice == 4:
            fn.clear_screen()
            prog.delete(database)
        elif choice == 5:
            break
        else:
            print('Silahkan masukkan pilihan yang sesuai.')
            continue
        update_database(database)

if __name__ == '__main__':
    fn.clear_screen()

    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/db.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/db.csv') 

    database = initialize_database()
    print('Selamat datang di BSDApp')
    main()