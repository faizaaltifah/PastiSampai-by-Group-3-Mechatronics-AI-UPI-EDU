import mysql.connector
import datetime
from prettytable import PrettyTable

db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="123456alt",
	database="pasti_sampai"
)

def create_data_barang(db):
	while True:
		tanggal_pengiriman = input("Tanggal Pengiriman [YYYY-MM-DD]     = ").strip()
		try:
			datetime.datetime.strptime(tanggal_pengiriman, format_tanggal)
			break
		except ValueError:
			print("\nTanggal yang dimasukan salah atau tidak sesuai format. Silahkan masukan kembali tanggal pengiriman")
	jenis_pengiriman = input("Jenis Pengiriman [Laut/Udara/Darat] = ").capitalize()
	while jenis_pengiriman not in jenis_pengiriman_tersedia:
		print("\nJenis pengiriman tidak tersedia. Silahkan masukan kembali jenis pengiriman.")
		jenis_pengiriman = input("Jenis Pengiriman [Laut/Udara/Darat] = ").capitalize()
	jenis_barang_dikirim = input("Jenis Barang yang Dikirim           = ")
	asal_pengiriman = input("Asal Pengiriman                     = ")
	tujuan_pengiriman = input("Tujuan Pengiriman                   = ")
	status_pengiriman = input("Status Pengiriman [SUDAH/TIDAK]     = ").upper()
	while status_pengiriman not in status_barang_terkirim:
		print("\nStatus pengiriman belum ditentukan. Silahkan tentukan kembali status pengiriman.")
		status_pengiriman = input("Status Pengiriman [SUDAH/TIDAK]     = ").upper()
	
	values = (
		tanggal_pengiriman, jenis_pengiriman, jenis_barang_dikirim,
		asal_pengiriman, tujuan_pengiriman, status_pengiriman
	)

	cursor = db.cursor()
	sql = "INSERT INTO data_pengiriman (tanggal_pengiriman, jenis_pengiriman, jenis_barang_dikirim, asal_pengiriman, tujuan_pengiriman, status_pengiriman) VALUES (%s, %s, %s, %s, %s, %s)"
	cursor.execute(sql, values)
	db.commit()

	print("\n+--------------------------------+")
	print("|Data barang baru berhasil dibuat|")
	print("+--------------------------------+\n")


def read_data_barang(db):
	cursor = db.cursor()
	sql = "SELECT * FROM data_pengiriman"
	cursor.execute(sql)
	data_barang = cursor.fetchall()
	
	if cursor.rowcount <= 0:
		print("+-------------------------+")
		print("|Tidak ada data pengiriman|")
		print("+-------------------------+\n")
	else:
		tabel_data = PrettyTable(["ID", "Tanggal", "Jenis Pengiriman", "Jenis Barang", "Asal", "Tujuan", "Status"])
		for data in data_barang:
			tabel_data.add_row(data)
		
		print(tabel_data)
		print('')


def update_data_barang(db):
	cursor = db.cursor()
	
	read_data_barang(db)
	id_pengiriman = input("Tentukan ID Pengiriman              = ")
	while True:
		tanggal_pengiriman = input("Tanggal Pengiriman [YYYY-MM-DD]     = ").strip()
		try:
			datetime.datetime.strptime(tanggal_pengiriman, format_tanggal)
			break
		except ValueError:
			print("\nTanggal yang dimasukan salah atau tidak sesuai format. Silahkan masukan kembali tanggal pengiriman")
	jenis_pengiriman = input("Jenis Pengiriman [Laut/Udara/Darat] = ").capitalize()
	while jenis_pengiriman not in jenis_pengiriman_tersedia:
		print("\nJenis pengiriman tidak tersedia. Silahkan masukan kembali jenis pengiriman.")
		jenis_pengiriman = input("Jenis Pengiriman [Laut/Udara/Darat] = ").capitalize()
	jenis_barang_dikirim = input("Jenis Barang yang Dikirim           = ")
	asal_pengiriman = input("Asal Pengiriman                     = ")
	tujuan_pengiriman = input("Tujuan Pengiriman                   = ")
	status_pengiriman = input("Status Pengiriman [SUDAH/TIDAK]     = ").upper()
	while status_pengiriman not in status_barang_terkirim:
		print("\nStatus pengiriman belum ditentukan. Silahkan tentukan kembali status pengiriman.")
		status_pengiriman = input("Status Pengiriman [SUDAH/TIDAK]     = ").upper()

	sql = "UPDATE data_pengiriman SET tanggal_pengiriman=%s, jenis_pengiriman=%s, jenis_barang_dikirim=%s, asal_pengiriman=%s, tujuan_pengiriman=%s, status_pengiriman=%s WHERE id_pengiriman=%s"
	values = (
		tanggal_pengiriman, jenis_pengiriman, jenis_barang_dikirim, 
		asal_pengiriman, tujuan_pengiriman, status_pengiriman, id_pengiriman
	)

	cursor.execute(sql, values)
	db.commit()

	print("\n+-----------------------------+")
	print("|Data barang berhasil diupdate|")
	print("+-----------------------------+\n")


def delete_data_barang(db):
	cursor = db.cursor()
	
	read_data_barang(db)
	id_pengiriman = input("Pilih ID Pengiriman                 = ")
	sql = "DELETE FROM data_pengiriman WHERE id_pengiriman=%s"
	values = (id_pengiriman,)
	cursor.execute(sql, values)
	db.commit()
	
	print("\n+----------------------------+")
	print("|Data barang berhasil dihapus|")
	print("+----------------------------+\n")


def search_data_barang(db):
	cursor = db.cursor()

	kata_kunci = input("Cari: ")
	sql = "SELECT * FROM data_pengiriman WHERE tanggal_pengiriman LIKE %s OR jenis_pengiriman LIKE %s OR jenis_barang_dikirim LIKE %s OR asal_pengiriman LIKE %s OR tujuan_pengiriman LIKE %s OR status_pengiriman LIKE %s"
	values = ("%{}%".format(kata_kunci), "%{}%".format(kata_kunci), "%{}%".format(kata_kunci), "%{}%".format(kata_kunci), "%{}%".format(kata_kunci), "%{}%".format(kata_kunci))
	cursor.execute(sql, values)
	data_barang = cursor.fetchall()
	
	if cursor.rowcount <= 0:
		print("\n+------------------------------------+")
		print("|Data tidak ada/tidak dapat ditemukan|")
		print("+------------------------------------+\n")
	else:
		tabel_data = PrettyTable(["ID", "Tanggal", "Jenis Pengiriman", "Jenis Barang", "Asal", "Tujuan", "Status"])
		for data in data_barang:
			tabel_data.add_row(data)
		
		print('')
		print(tabel_data)
		print('')


def menu(db):
	print("1. Create Data Barang")
	print("2. Read Data Barang")
	print("3. Update Data Barang")
	print("4. Delete Data Barang")
	print("5. Cari Data Barang")
	print("0. Keluar")
	pilih_menu = int(input("Pilih menu [1/2/3/4/5/0]: "))
	print('')
	
	if pilih_menu == 1:
		create_data_barang(db)
	elif pilih_menu == 2:
		read_data_barang(db)
	elif pilih_menu == 3:
		update_data_barang(db)
	elif pilih_menu == 4:
		delete_data_barang(db)
	elif pilih_menu == 5:
		search_data_barang(db)
	elif pilih_menu == 0:
		exit()
	else:
		print("\n---------------------------")
		print("Menu yang dipilih tidak ada")
		print("---------------------------\n")

format_tanggal = "%Y-%m-%d"
jenis_pengiriman_tersedia = ["Laut", "Udara", "Darat"]
status_barang_terkirim = ["SUDAH", "TIDAK"]

print("\nLogistik PastiSampai")
while True:
	menu(db)
