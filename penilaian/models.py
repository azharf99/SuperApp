from django.db import models
from django.utils import timezone

# Create your models here.
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

nilai_sikap = (
    (None, "Pilih Nilai Sikap"),
    ("A", "Sangat Baik"),
    ("B", "Baik"),
    ("C", "Cukup"),
    ("D", "Kurang Baik"),
    ("E", "Buruk"),
)

kategori_nilai = (
    (None, "Pilih Kategori Nilai"),
    ("Pengetahuan", "Pengetahuan (Kognitif)"),
    ("Keterampilan", "Keterampilan (Psikomotorik)"),
)

pilihan_presensi = (
    (None, "Pilih Kehadiran"),
    ("Hadir", "Hadir"),
    ("Sakit", "Sakit"),
    ("Izin", "Izin"),
    ("Alpha", "Tanpa Keterangan"),
)

class Nilai(models.Model):
    nama_nilai = models.CharField(max_length=10)
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    pelajaran = models.ForeignKey('Mengajar', on_delete=models.CASCADE)
    nilai = models.PositiveSmallIntegerField(default=0)
    kategori_nilai = models.CharField(max_length=20, choices=kategori_nilai)
    keterangan = models.CharField(max_length=20, blank=True, null=True)
    tahun_ajaran = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.siswa.nama_siswa} | {self.pelajaran} | {self.nama_nilai} | {self.nilai}"


class NilaiSikap(models.Model):
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    nilai_spiritual = models.CharField(max_length=1, default=nilai_sikap[1][0], choices=nilai_sikap)
    nilai_sosial = models.CharField(max_length=1, default=nilai_sikap[1][0], choices=nilai_sikap)
    keterangan = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.siswa.nama_siswa} | {self.nilai_sosial}"


class Presensi(models.Model):
    hari = models.DateField(default=timezone.localdate(timezone=timezone.get_default_timezone()))
    jam = models.CharField(max_length=50, choices=jam_mengajar)
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    presensi = models.CharField(max_length=20, choices=pilihan_presensi, default=pilihan_presensi[1][0])
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hari} | {self.jam} | {self.siswa} | {self.presensi}"

class Prestasi(models.Model):
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    jenis_prestasi = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.siswa} | {self.jenis_prestasi}"


class Ekstrakurikuler(models.Model):
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    nama_ekskul = models.CharField(max_length=100, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.siswa} | {self.nama_ekskul}"


class CatatanWalikelas(models.Model):
    siswa = models.ForeignKey('Siswa', on_delete=models.CASCADE)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.siswa} | {self.catatan}"
