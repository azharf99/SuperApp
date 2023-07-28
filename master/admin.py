from django.contrib import admin
from master.models import *

# Register your models here.
admin.site.register(Guru)
admin.site.register(Siswa)
admin.site.register(Kelas)
admin.site.register(WaliKelas)
admin.site.register(Mengajar)
admin.site.register(MataPelajaran)
admin.site.register(Nilai)
admin.site.register(NilaiSikap)
admin.site.register(BelajarSiswa)
admin.site.register(Jurusan)
admin.site.register(JadwalMengajar)
admin.site.register(Presensi)
admin.site.register(Pelanggaran)
admin.site.register(Prestasi)
admin.site.register(Ekstrakurikuler)
admin.site.register(CatatanWalikelas)


admin.site.site_title = 'Halaman Admin'
admin.site.site_header = 'Halaman Admin'
