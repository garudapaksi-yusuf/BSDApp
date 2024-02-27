import functions as fn

def read(table):
    fn.database_to_table(
        data = table.values(),
        columns = ['No.', 'Nama Perusahaan', 'Bidang Usaha', 'Proyek', 'Domisili Hukum', 'Kepemilikan', 'Tahun Penyertaan', 'Status', 
                   'Jumlah Aset (Dalam Jutaan Rp)'],
        title = 'Entitas Anak Di Bawah PT Bumi Serpong Damai Tbk\n')
    
def create(table):
    fn.authorization()
    companyName = fn.regex_validation('Silahkan masukkan Nama Perusahaan: ')
    businessNature = fn.regex_validation('Silahkan masukkan Bidang Usaha Perusahaan: ')
    project = fn.regex_validation('Silahkan masukkan Nama Proyek: ')
    domicile = fn.regex_validation('Silahkan masukkan Domisili Perusahaan: ')
    ownership = fn.percentage_validation('Silahkan masukkan Nilai Kepemilikan: ')
    yearAcquired = fn.datetime_validation('Silahkan masukkan Tahun Penyertaan: ')
    status = fn.set_validation('Silahkan masukkan Status Perusahaan: ')
    totalAssets = fn.integer_validation('Silahkan masukkan Jumlah Aset: ')

    table.update({len(table) + 1: [len(table) + 1, companyName, businessNature.title(), project.title(), domicile.title(), 
                                   f"{ownership}{'%'}", yearAcquired, status.title(), fn.thousands_separator(totalAssets)]})
    
def update(table):
    fn.authorization()
    read(table)
    while True:
        index = input('Silahkan masukkan Nomor Indeks Perusahaan yang akan diubah: ')    
        if index not in table.keys():
            print('''Nomor tersebut tidak ada di database.
Silahkan masukkan Nomor Indeks Perusahaan yang sesuai.''')
            continue
        else:
            fn.update_menu()
            choice = fn.integer_validation('Silahkan masukkan nomor pilihan: ')
            if choice == 1:
                fn.update_submenu(table, index, choice = 1)
            elif choice == 2:
                fn.update_submenu(table, index, choice = 2)
            elif choice == 3:
                fn.update_submenu(table, index, choice = 3)
            else:
                print('Silahkan masukkan nomor pilihan yang sesuai.')
            break

def delete(table):
    fn.authorization()
    read(table)
    while True:
        index = fn.integer_validation('Silahkan masukkan Nomor Indeks Perusahaan yang akan diubah: ')
        if index > len(table):
            print('''Nomor tersebut tidak tersedia. 
Silahkan masukkan Nomor Indeks Perusahaan yang sesuai.''')
            continue
        else:
            del table[str(index)]

        for index_, value in enumerate(table.values()):
            if index_ < int(value[0]):
                value[0] = int(value[0])
                value[0] -= 1
        else:
            break