from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Avg
from master.models import *
from master.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
    return render(request, 'index.html')

"""
View : Memodifikasi User Model
"""

class UserView(ListView):
    model = User

class UserAddView(CreateView):
    model = User
    fields = ['username', 'email', 'password']

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'password', 'first_name', 'last_name']
    success_url = 'app/user-list'

class UserDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Guru
    success_url = reverse_lazy("user-list")


"""
View : Memodifikasi Guru Model
"""

class GuruListView(ListView):
    model = Guru

class GuruDetailView(DetailView):
    model = Guru

class GuruAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Guru
    form_class = GuruForm
    success_url = '/app/teacher-list'

class GuruUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Guru
    form_class = GuruForm
    success_url = '/app/teacher-list'

class GuruDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Guru
    success_url = reverse_lazy("teacher-list")

"""
View : Memodifikasi Siswa Model
"""

class SiswaListView(ListView):
    model = Siswa

class SiswaDetailView(DetailView):
    model = Siswa

class SiswaAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Siswa
    form_class = SiswaForm
    success_url = '/app/student-list'

class SiswaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Siswa
    form_class = SiswaForm
    success_url = '/app/student-list'

class SiswaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Siswa
    success_url = reverse_lazy("student-list")

"""
View : Memodifikasi Jurusan Model
"""

class JurusanListView(ListView):
    model = Jurusan

class JurusanDetailView(DetailView):
    model = Jurusan

class JurusanAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Jurusan
    form_class = JurusanForm
    success_url = '/app/jurusan-list'

class JurusanUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Jurusan
    form_class = JurusanForm
    success_url = '/app/jurusan-list'

class JurusanDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Jurusan
    success_url = reverse_lazy("jurusan-list")


"""
View : Memodifikasi MataPelajaran Model
"""

class MataPelajaranListView(ListView):
    model = MataPelajaran

class MataPelajaranDetailView(DetailView):
    model = MataPelajaran

class MataPelajaranAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = MataPelajaran
    form_class = MataPelajaranForm
    success_url = '/app/mapel-list'

class MataPelajaranUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = MataPelajaran
    form_class = MataPelajaranForm
    success_url = '/app/mapel-list'

class MataPelajaranDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = MataPelajaran
    success_url = reverse_lazy("mapel-list")

"""
View : Memodifikasi Kelas Model
"""

class KelasListView(ListView):
    model = Kelas

class KelasDetailView(DetailView):
    model = Kelas

class KelasAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Kelas
    form_class = KelasForm
    success_url = '/app/kelas-list'

class KelasUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Kelas
    form_class = KelasForm
    success_url = '/app/kelas-list'

class KelasDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Kelas
    success_url = reverse_lazy("kelas-list")


"""
View : Memodifikasi Mengajar Model
"""

class MengajarListView(ListView):
    model = Mengajar

class MengajarDetailView(DetailView):
    model = Mengajar

class MengajarAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Mengajar
    form_class = MengajarForm
    success_url = '/app/mengajar-list'

class MengajarUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Mengajar
    form_class = MengajarForm
    success_url = '/app/mengajar-list'

class MengajarDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Mengajar
    success_url = reverse_lazy("mengajar-list")



"""
View : Memodifikasi Wali Kelas Model
"""

class WaliKelasListView(ListView):
    model = WaliKelas

class WaliKelasDetailView(DetailView):
    model = WaliKelas

class WaliKelasAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = WaliKelas
    form_class = WaliKelasForm
    success_url = '/app/walikelas-list'

class WaliKelasUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = WaliKelas
    form_class = WaliKelasForm
    success_url = '/app/walikelas-list'

class WaliKelasDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = WaliKelas
    success_url = reverse_lazy("walikelas-list")


"""
View : Memodifikasi Belajar Siswa Model
"""

class BelajarSiswaListView(ListView):
    model = BelajarSiswa

class BelajarSiswaDetailView(DetailView):
    model = BelajarSiswa

class BelajarSiswaAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = BelajarSiswa
    form_class = BelajarSiswaForm
    success_url = '/app/belajarsiswa-list'

class BelajarSiswaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = BelajarSiswa
    form_class = BelajarSiswaForm
    success_url = '/app/belajarsiswa-list'

class BelajarSiswaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = BelajarSiswa
    success_url = reverse_lazy("belajarsiswa-list")


"""
View : Memodifikasi Jadwal Mengajar Model
"""

class JadwalMengajarListView(ListView):
    model = JadwalMengajar

class JadwalMengajarDetailView(DetailView):
    model = JadwalMengajar

class JadwalMengajarAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = JadwalMengajar
    form_class = JadwalMengajarForm
    success_url = '/app/jadwal-list'

class JadwalMengajarUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = JadwalMengajar
    form_class = JadwalMengajarForm
    success_url = '/app/jadwal-list'

class JadwalMengajarDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = JadwalMengajar
    success_url = reverse_lazy("jadwal-list")