from django.test import TestCase
from master.models import *


# Create your tests here.

class TestModels(TestCase):

    def test_model_guru(self):
        user = User.objects.create(
            username='azharfa',
            password='Azhar1995',
            email='azharfaturohman29@gmail.com'
        )

        Guru.objects.create(
            niy='1',
            nama_guru="Azhar Faturohman Ahidin, S.Si",
            jenis_kelamin="L",
            alamat='Subang',
            jabatan='Guru Biologi',
            email='azharfaturohman29@gmail.com',
            nomor_hp='08501570100',
            username=user,
            status='aktif',
        )
        data = Guru.objects.get(niy='1')
        self.assertEqual(data.nama_guru, "Azhar Faturohman Ahidin, S.Si")

    def test_model_siswa(self):
        data = Siswa.objects.create(
            nis='1',
            nisn='1',
            nama_siswa="Rakeyan Cakra Wicaksana",
            jenis_kelamin="L",
            alamat='Garut',
            tempat_lahir='Garut',
            tanggal_lahir='2023-07-08',
            email='rakeyan@gmail.com',
            nomor_hp='08501570101',
            status='aktif',
        )
        self.assertEqual(data.nama_siswa, "Rakeyan Cakra Wicaksana")

    def test_model_jurusan(self):
        data = Jurusan.objects.create(
            kode_jurusan='UMUM',
            nama_jurusan='ASHRI'
        )

        self.assertEqual(data.kode_jurusan, "UMUM", "Ini Test Jurusan")

    def test_model_matapelajaran(self):
        jurusan = Jurusan.objects.create(
            kode_jurusan='UMUM',
            nama_jurusan='ASHRI'
        )
        data = MataPelajaran.objects.create(
            kode_mapel='Bio',
            nama_mapel='Biologi',
            jenis_mapel='Umum',
            kelompok_mapel='Kelompok A',
            jurusan=jurusan
        )

        self.assertEqual(data.nama_mapel, 'Biologi')

