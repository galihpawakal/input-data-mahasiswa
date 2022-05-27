# membuat fungsi data mahasiswa


# memasukan data pada dictionary
def mahasiswa_input(data1, data2, nomer):
    while True:
        data1.append(input('Masukan %s mahasiswa : ' % data2))
        if len(data1[i]) == nomer:
            break
        else:
            data1.pop(i)
            continue

# variabel declaration


i = a = b = c = d = 0

# dictionary kosong
nama_mhs = []
nim_mhs = []
kelas_mhs = []
jur_mhs = []
angkatan_mhs = []


while True:
    print('Masukan data ke  -', i+1)
    nama_mhs.append(input('Masukkan nama Mahasiswa : '))
    mahasiswa_input(nim_mhs, 'NIM ( dengan jumlah kata / nomor  8 ) ', 8)
    mahasiswa_input(kelas_mhs, 'KELAS (A - E)', 1)
    mahasiswa_input(jur_mhs, 'JURUSAN (TI/EK/MN/IN)', 2)
    if jur_mhs[i] == 'TI':
        jur_mhs[i] = 'Teknik Informatika'
        a += 1
    elif jur_mhs[i] == 'EK':
        jur_mhs[i] = 'Teknik Elektronik'
        b += 1
    elif jur_mhs[i] == 'MN':
        jur_mhs[i] = 'Teknik Mesin'
        c += 1
    elif jur_mhs[i] == 'IN':
        jur_mhs[i] = 'Teknik Industri'
        d += 1
    else:
        print(" data salah ")
        jur_mhs.pop(i)
        nama_mhs.pop(i)
        kelas_mhs.pop(i)
        nim_mhs.pop(i)
        continue
    mahasiswa_input(angkatan_mhs, 'ANGKATAN (TAHUN)', 4)
    lagi = input('INPUT LAGI? [y/t] : ')
    if lagi == 'y':
        i += 1
    else:
        break


for data in range(len(nim_mhs)):
    print(data+1, "\t", nama_mhs[data], "\t", nim_mhs[data], "\t",
          kelas_mhs[data], "\t", angkatan_mhs[data], "\t", jur_mhs[data],)
    print('TOTAL JURUSAN TEKNIK INFORMATIKA = ', a, 'orang\n')
    print('TOTAL JURUSAN TEKNIK ELEKTRONIKA = ', b, 'orang\n')
    print('TOTAL JURUSAN TEKNIK MESIN       = ', c, 'orang\n')
    print('TOTAL JURUSAN TEKNIK INDUSTRI    = ', d, 'orang\n')

    tahan = ''
    while tahan != ('y' or 't'):
        tahan = input('ingin melihat hasil (y/t) ? ')
        if tahan == 'y':
            cari = input('cari berdasarkan nim : ')
            for n in range(i):
                if cari == nim_mhs[n]:
                    print('Nama : ', nama_mhs[n])
                    print('Kelas : ', kelas_mhs[n])
                    print('Angkatan : ', angkatan_mhs[n])
                    print('Jurusan :', jur_mhs[n])
                    continue
                else:
                    print('NIM tidak ada')
                    continue
        elif tahan == 't':
            break
        else:
            continue
