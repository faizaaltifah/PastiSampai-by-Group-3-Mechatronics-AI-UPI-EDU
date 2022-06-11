CREATE DATABASE pasti_sampai;
USE pasti_sampai;
CREATE TABLE data_pengiriman (
`id_pengiriman` int(10) auto_increment NOT NULL, 
`tanggal_pengiriman` DATE NOT NULL, 
`jenis_pengiriman` VARCHAR(10) NOT NULL, 
`jenis_barang_dikirim` VARCHAR(50) NOT NULL ,
`asal_pengiriman` VARCHAR(255) NOT NULL ,
`tujuan_pengiriman` VARCHAR(255) NOT NULL ,
`status_pengiriman` VARCHAR(20) NOT NULL);
select * from data_pengiriman
