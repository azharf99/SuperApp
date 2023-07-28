from django.contrib import admin

from penilaian.models import Nilai, NilaiSikap, Presensi, Prestasi, Ekstrakurikuler, CatatanWalikelas

# Register your models here.
admin.site.register(Nilai)
admin.site.register(NilaiSikap)
admin.site.register(Presensi)
admin.site.register(Prestasi)
admin.site.register(Ekstrakurikuler)
admin.site.register(CatatanWalikelas)