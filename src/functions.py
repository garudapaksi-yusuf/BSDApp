from datetime import datetime
from itertools import zip_longest
import os
import pwinput
from re import match
from tabulate import tabulate

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main_menu():
    print('''
1. Tampilkan Data Entitas Anak
2. Tambah Data Entitas Anak
3. Ubah Data Entitas Anak
4. Hapus Data Entitas Anak
5. Keluar
        '''
        )

def database_to_table(data, columns, title):
    print(title)
    print(tabulate(data, headers = columns, tablefmt = "grid"))

def authorization():
    while True:
        username = input('Silahkan masukkan Username anda: ')
        password = pwinput.pwinput(prompt = 'Silahkan masukkan Password anda: ', mask = '*')
        if username == 'admin' and password == '1234':
            clear_screen()
            print('''Anda berhasil masuk.
Saat ini anda sedang mengakses Database Entitas Anak PT Bumi Serpong Damai Tbk.\n''')
            break
        else:
            print('''Username/Password anda salah.
Silahkan masukkan Username/Password yang sesuai''')
            continue

def regex_validation(prompt):
    while True:
        name = input(prompt)
        if match("[a-zA-Z. -]", name):
            break
        else:
            print('Silahkan masukkan nama sesuai ketentuan yang berlaku.')
            continue
    return name

def percentage_validation(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print('Silahkan masukkan bilangan positif.')
                number = abs(number)
            elif number > 100:
                print('Nilai Kepemilikan maksimal adalah 100(%).')
            else:
                break
        except:
            print('Silahkan masukkan nilai berdasarkan angka.')
            continue
    return number

def datetime_validation(prompt):
    while True:
        try:
            year = int(input(prompt))
            if year < 1984 or year > datetime.now().year:
                print('Silahkan masukkan tahun yang sesuai.')
                continue
            else:
                break
        except:
            print('Silahkan masukkan tahun berdasarkan angka.')
            continue
    return year  

def set_validation(prompt):
    status_set = ('Belum Beroperasi', 'Praoperasi', 'Beroperasi')
    while True:
        state = input(prompt)
        if state.title() in status_set:
            break
        else:
            print('Silahkan masukkan status yang sesuai.')
            continue
    return state

def integer_validation(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print('Silahkan masukkan bilangan positif.')
                continue
            else:
                break
        except:
            print('Silahkan masukkan nilai berdasarkan angka.')
            continue
    return number

def thousands_separator(value):
    separator = '.'
    decimal_places = 3
    arguments = [iter(str(value)[::-1])] * decimal_places
    value_separated = separator.join(''.join(digit) for digit in zip_longest(*arguments, fillvalue = ''))[::-1]
    return value_separated

def update_menu():

    print(
    '''Update Menu Options

    1. Kepemilikan
    2. Status
    3. Total Aset
    '''
    )

def update_submenu(table, index, choice):
    if choice == 1:
        newOwnership = integer_validation('Silahkan masukkan Nilai Kepemilikan: ')
        for value in table.values():
            if index == value[0]:
                value[5] = f"{newOwnership}{'%'}"
    elif choice == 2:
        newstatus = set_validation('Silahkan masukkan Status Perusahaan: ')
        for value in table.values():
            if index == value[0]:
                value[7] = newstatus.title()
    elif choice == 3:
        newTotalAssets = integer_validation('Silahkan masukkan Jumlah Aset: ')
        for value in table.values():
            if index == value[0]:
                value[8] = thousands_separator(newTotalAssets)

# code = input('Silahkan masukkan Kode Perusahaan yang hendak diubah: ')
# if code.upper() not in db.keys():
#     print('Perusahaan tersebut tidak ada di database.')
#     print('Silahkan masukkan Kode Perusahaan yang sesuai.')
#     continue