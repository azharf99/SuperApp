from django.db import models
from master.models import Siswa

# Create your models here.
jam_pelanggaran = (
    ("Jam ke-1", "Jam ke-1 07.00 - 07.30 (Normal)"),
    ("Jam ke-2", "Jam ke-2 07.30 - 08.10 (Normal)"),
    ("Jam ke-3", "Jam ke-3 08.10 - 08.50 (Normal)"),
    ("Jam ke-4", "Jam ke-4 08.55 - 09.35 (Normal)"),
    ("Jam ke-5", "Jam ke-5 09.35 - 10.15 (Normal)"),
    ("Jam ke-6", "Jam ke-6 10.45 - 11.25 (Normal)"),
    ("Jam ke-7", "Jam ke-7 11.25 - 12.10 (Normal)"),
    ("Jam ke-8", "Jam ke-8 13.40 - 14.20 (Normal)"),
    ("Jam ke-9", "Jam ke-9 14.20 - 15.00 (Normal)"),
    ("Di luar jam KBM", "DI Luar Jam KBM"),
)

class Pelanggaran(models.Model):
    hari = models.DateField()
    jam_pelanggaran = models.CharField(max_length=50, choices=jam_pelanggaran)
    pelanggar = models.ForeignKey(Siswa, on_delete=models.CASCADE)
    pelapor = models.CharField(max_length=50)
    pelanggaran = models.CharField(max_length=200)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hari} | {self.jam_pelanggaran} | {self.pelanggaran}"
