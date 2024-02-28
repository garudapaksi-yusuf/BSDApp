import functions as fn

def read(table):
    fn.database_to_table(
        data = table.values(),
        columns = ['No.', 'Nama Perusahaan', 'Bidang Usaha', 'Proyek', 'Domisili Hukum', 'Kepemilikan', 'Tahun Penyertaan', 'Status', 
                   'Jumlah Aset (Dalam Jutaan Rp)'],
        title = 'Entitas Anak Di Bawah PT Bumi Serpong Damai Tbk\n')
    return print('\n')
    
def create(table):
    companyName = fn.string_validation('Silahkan masukkan Nama Perusahaan yang akan ditambahkan: ')
    businessNature = fn.string_validation('Silahkan masukkan Nama Bidang Usaha Perusahaan: ')
    project = fn.string_validation('Silahkan masukkan Nama Proyek: ')
    domicile = fn.string_validation('Silahkan masukkan Nama Domisili Perusahaan: ')
    ownership = fn.percentage_validation('Silahkan masukkan Nilai Kepemilikan: ')
    yearAcquired = fn.datetime_validation('Silahkan masukkan Tahun Penyertaan: ')
    status = fn.set_validation('Silahkan masukkan Status Perusahaan: ')
    totalAssets = fn.integer_validation('Silahkan masukkan Jumlah Aset: ')

    table.update({len(table) + 1: [len(table) + 1, companyName, businessNature.title(), project.title(), domicile.title(), 
                                   f"{ownership}{'%'}", yearAcquired, status.title(), fn.thousands_separator(totalAssets)]})
    fn.clear_screen()
    print('Data berhasil ditambahkan.\n')
    
def update(table):
    read(table)
    while True:
        index = fn.integer_validation('Silahkan masukkan Nomor Indeks Perusahaan yang akan diubah: ')    
        if str(index) not in table.keys():
            print('''Nomor tersebut tidak ada di database.
Masukkan Nomor Indeks Perusahaan yang sesuai.\n''')
            continue
        else:
            fn.clear_screen()
            read(table)
            while True:
                fn.update_menu(index)
                choice = fn.integer_validation('Silahkan masukkan nomor pilihan: ')
                if choice == 1:
                    fn.update_submenu(table, index, choice = 1)
                elif choice == 2:
                    fn.update_submenu(table, index, choice = 2)
                elif choice == 3:
                    fn.update_submenu(table, index, choice = 3)
                elif choice == 4:
                    fn.clear_screen()
                    return
                else:
                    print('Masukkan nomor pilihan yang sesuai.\n')
                    continue

def delete(table):
    read(table)
    while True:
        index = fn.integer_validation('Silahkan masukkan Nomor Indeks Perusahaan yang akan dihapus: ')
        if index > len(table):
            print('''Nomor tersebut tidak ada di database. 
Masukkan Nomor Indeks Perusahaan yang sesuai.\n''')
            continue
        else:
            del table[str(index)]
            fn.clear_screen()
            print('Data berhasil dihapus.\n')

        for idx, value in enumerate(table.values()):
            if idx != value[0]:
                value[0] = idx + 1
        else:
            return