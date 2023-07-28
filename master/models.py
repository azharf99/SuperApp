from django.db import models
from django.contrib.auth.models import User
from master.compress_image import CompressedImageField

# Create your models here.

jenis_kelamin = (
    (None, "Pilih Jenis Kelamin"),
    ("L", "Laki-laki"),
    ("P", "Perempuan")
)
hari_mengajar = (
    (None, "Pilih Hari Mengajar"),
    ("Senin", "Senin"),
    ("Selasa", "Selasa"),
    ("Rabu", "Rabu"),
    ("Kamis", "Kamis"),
    ("Sabtu", "Sabtu"),
    ("Ahad", "Ahad"),
)

jam_mengajar = (
    (None, "Pilih Jam Mengajar"),
    ("Jam ke-1", "Jam ke-1 07.00 - 07.30 (Normal)"),
    ("Jam ke-2", "Jam ke-2 07.30 - 08.10 (Normal)"),
    ("Jam ke-3", "Jam ke-3 08.10 - 08.50 (Normal)"),
    ("Jam ke-4", "Jam ke-4 08.55 - 09.35 (Normal)"),
    ("Jam ke-5", "Jam ke-5 09.35 - 10.15 (Normal)"),
    ("Jam ke-6", "Jam ke-6 10.45 - 11.25 (Normal)"),
    ("Jam ke-7", "Jam ke-7 11.25 - 12.10 (Normal)"),
    ("Jam ke-8", "Jam ke-8 13.40 - 14.20 (Normal)"),
    ("Jam ke-9", "Jam ke-9 14.20 - 15.00 (Normal)")
)


jenis_mapel = (
    (None, "Pilih Jenis Mapel"),
    ("Umum", "Umum (Diknas)"),
    ("Syar'i", "Syar'i (Pesantren)"),
)

kelompok_mapel = (
    (None, "Pilih Kelompok Mapel"),
    ("Kelompok A", "Kelompok A (Umum)"),
    ("Kelompok B", "Kelompok B (Umum)"),
    ("Kelompok C", "Kelompok C (Peminatan)"),
)


class Guru(models.Model):
    niy = models.CharField(max_length=21, primary_key=True, auto_created=True)
    nama_guru = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=1, choices=jenis_kelamin)
    alamat = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nomor_hp = models.CharField(max_length=15)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="Nonaktif", blank=True, null=True, )
    foto = CompressedImageField(upload_to='profile', blank=True, null=True, default='avatar.png', quality=50,
                                help_text="Format foto disarankan .jpg/.jpeg")

    def __str__(self):
        return self.nama_guru

    class Meta:
        indexes = [
            models.Index(fields=["niy", ]),
        ]


class Siswa(models.Model):
    nis = models.CharField(max_length=30, primary_key=True)
    nisn = models.CharField(max_length=30)
    nama_siswa = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=10, choices=jenis_kelamin)
    alamat = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    email = models.EmailField(max_length=50)
    nomor_hp = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    foto = CompressedImageField(upload_to='student', blank=True, null=True, default='avatar.png', quality=50,
                                help_text="Format foto disarankan .jpg/.jpeg")

    def __str__(self):
        return self.nama_siswa

    class Meta:
        indexes = [
            models.Index(fields=["nis", "nisn", ]),
        ]


class Jurusan(models.Model):
    kode_jurusan = models.CharField(max_length=10, primary_key=True)
    nama_jurusan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_jurusan

    class Meta:
        indexes = [
            models.Index(fields=["kode_jurusan", ]),
        ]


class MataPelajaran(models.Model):
    kode_mapel = models.CharField(max_length=10, primary_key=True)
    nama_mapel = models.CharField(max_length=40)
    jenis_mapel = models.CharField(max_length=20, choices=jenis_mapel)
    kelompok_mapel = models.CharField(max_length=20, choices=kelompok_mapel)
    jurusan = models.ForeignKey('Jurusan', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kode_mapel} | {self.jurusan.nama_jurusan}"

    class Meta:
        indexes = [
            models.Index(fields=["kode_mapel", ]),
        ]


class Kelas(models.Model):
    kode_kelas = models.CharField(max_length=10, primary_key=True)
    nama_kelas = models.CharField(max_length=20)
    jurusan = models.ForeignKey('Jurusan', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_kelas

    class Meta:
        indexes = [
            models.Index(fields=["kode_kelas", ]),
        ]


class Mengajar(models.Model):
    guru = models.ForeignKey('Guru', on_delete=models.SET_NULL, null=True)
    mapel = models.ForeignKey('MataPelajaran', on_delete=models.CASCADE)
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    file_nilai_pts = models.FileField(upload_to='pts', blank=True, null=True)
    file_nilai_pas = models.FileField(upload_to='pas', blank=True, null=True)
    tahun_ajaran = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.mapel.nama_mapel} | {self.guru.nama_guru}"


class WaliKelas(models.Model):
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    guru = models.ForeignKey('Guru', on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=20)

    def __str__(self):
        return f"Walikelas {self.kelas} : {self.guru.nama_guru}"


class BelajarSiswa(models.Model):
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    kelas = models.ForeignKey('Kelas', on_delete=models.CASCADE)
    tahun_ajaran = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.siswa} | {self.kelas} | {self.tahun_ajaran} | {self.semester}"

class JadwalMengajar(models.Model):
    hari = models.CharField(max_length=20, choices=hari_mengajar)
    jam = models.CharField(max_length=50, choices=jam_mengajar)
    pelajaran = models.ForeignKey('Mengajar', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hari} | {self.jam} | {self.pelajaran}"

