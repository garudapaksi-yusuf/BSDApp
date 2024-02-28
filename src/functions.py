from datetime import datetime
from itertools import zip_longest
import os
from tabulate import tabulate

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def main_menu():
    print('''1. Tampilkan Data Entitas Anak
2. Tambah Data Entitas Anak
3. Ubah Data Entitas Anak
4. Hapus Data Entitas Anak
5. Keluar
        '''
        )

def database_to_table(data, columns, title):
    print(title)
    print(tabulate(data, headers = columns, tablefmt = 'grid'))

def string_validation(prompt):
    while True:
        string = input(prompt)
        if string.isalpha() or string.replace(' ', '').replace('.', '').replace('-', '').isalpha():
            break
        else:
            print('''Masukkan nama berdasarkan huruf alfabet.
Dipersilahkan menggunakan karakter spasi, titik, dan tanda hubung sebagai pemisah kata.\n''')
            continue
    return string

def percentage_validation(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print('Silahkan masukkan bilangan positif.\n')
                number = abs(number)
            elif number > 100:
                print('Nilai Kepemilikan maksimal adalah 100(%).\n')
            else:
                break
        except:
            print('Masukkan nilai berdasarkan angka.\n')
            continue
    return number

def datetime_validation(prompt):
    while True:
        try:
            year = int(input(prompt))
            if year < 1984 or year > datetime.now().year:
                print('''Silahkan masukkan tahun yang sesuai.
Dimulai sejak awal PT Bumi Serpong Damai Tbk didirikan hingga saat ini.\n''')
                continue
            else:
                break
        except:
            print('Masukkan tahun berdasarkan angka.\n')
            continue
    return year  

def set_validation(prompt):
    status_set = ('Belum Beroperasi', 'Praoperasi', 'Beroperasi')
    while True:
        state = input(prompt)
        if state.title() in status_set:
            break
        else:
            print('Silahkan masukkan status yang sesuai (Belum Beroperasi/Praoperasi/Beroperasi).\n')
            continue
    return state

def integer_validation(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print('Silahkan masukkan bilangan positif.\n')
                continue
            else:
                return number
        except:
            print('Silahkan masukkan nilai berdasarkan angka.\n')
            continue

def thousands_separator(value):
    separator = '.'
    decimal_places = 3
    arguments = [iter(str(value)[::-1])] * decimal_places
    value_separated = separator.join(''.join(digit) for digit in zip_longest(*arguments, fillvalue = ''))[::-1]
    return value_separated

def update_menu(index):
    print(f'''Ubah Data Entitas Anak PT Bumi Serpong Damai Tbk
Nomor Indeks Perusahaan: {index}

    1. Nilai Kepemilikan
    2. Status
    3. Total Aset
    4. Keluar
    '''
    )

def update_submenu(table, index, choice):
    if choice == 1:
        newOwnership = integer_validation('\nSilahkan masukkan Nilai Kepemilikan: ')
        for value in table.values():
            if str(index) == value[0]:
                value[5] = f"{newOwnership}{'%'}"
                print('Data berhasil diubah\n')
    elif choice == 2:
        newstatus = set_validation('\nSilahkan masukkan Status Perusahaan: ')
        for value in table.values():
            if str(index) == value[0]:
                value[7] = newstatus.title()
                print('Data berhasil diubah\n')
    elif choice == 3:
        newTotalAssets = integer_validation('\nSilahkan masukkan Jumlah Aset: ')
        for value in table.values():
            if str(index) == value[0]:
                value[8] = thousands_separator(newTotalAssets)
                print('Data berhasil diubah\n')