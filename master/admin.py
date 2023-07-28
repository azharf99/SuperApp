from django.contrib import admin

from master.models import Guru, Siswa, Kelas, WaliKelas, Mengajar, MataPelajaran, BelajarSiswa, Jurusan, JadwalMengajar

# Register your models here.
admin.site.register(Guru)
admin.site.register(Siswa)
admin.site.register(Kelas)
admin.site.register(WaliKelas)
admin.site.register(Mengajar)
admin.site.register(MataPelajaran)
admin.site.register(BelajarSiswa)
admin.site.register(Jurusan)
admin.site.register(JadwalMengajar)



admin.site.site_title = 'Halaman Admin'
admin.site.site_header = 'Login Admin'
