from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from penilaian.forms import NilaiForm, NilaiSikapForm, PresensiForm, PrestasiForm, EkstrakurikulerForm, \
    CatatanWalikelasForm
from penilaian.models import Nilai, NilaiSikap, Presensi, Prestasi, CatatanWalikelas, Ekstrakurikuler

# Create your views here.

"""
View : Memodifikasi Nilai Model
"""

class NilaiListView(ListView):
    model = Nilai

class NilaiDetailView(DetailView):
    model = Nilai

class NilaiAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Nilai
    form_class = NilaiForm
    success_url = '/app/nilai-list'

class NilaiUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Nilai
    form_class = NilaiForm
    success_url = '/app/nilai-list'

class NilaiDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Nilai
    success_url = reverse_lazy("nilai-index")


"""
View : Memodifikasi Nilai Sikap Model
"""

class NilaiSikapListView(ListView):
    model = NilaiSikap

class NilaiSikapDetailView(DetailView):
    model = NilaiSikap

class NilaiSikapAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = NilaiSikap
    form_class = NilaiSikapForm
    success_url = '/app/sikap-list'

class NilaiSikapUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = NilaiSikap
    form_class = NilaiSikapForm
    success_url = '/app/sikap-list'

class NilaiSikapDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = NilaiSikap
    success_url = reverse_lazy("sikap-list")

"""
View : Memodifikasi Presensi Model
"""

class PresensiListView(ListView):
    model = Presensi

class PresensiDetailView(DetailView):
    model = Presensi

class PresensiAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Presensi
    form_class = PresensiForm
    success_url = '/app/presensi-list'

class PresensiUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Presensi
    form_class = PresensiForm
    success_url = '/app/presensi-list'

class PresensiDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Presensi
    success_url = reverse_lazy("presensi-list")


"""
View : Memodifikasi Prestasi Model
"""

class PrestasiListView(ListView):
    model = Prestasi

class PrestasiDetailView(DetailView):
    model = Prestasi

class PrestasiAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Prestasi
    form_class = PrestasiForm
    success_url = '/app/prestasi-list'

class PrestasiUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Prestasi
    form_class = PrestasiForm
    success_url = '/app/prestasi-list'

class PrestasiDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Prestasi
    success_url = reverse_lazy("prestasi-list")


"""
View : Memodifikasi Ekstrakurikuler Model
"""

class EkstrakurikulerListView(ListView):
    model = Ekstrakurikuler

class EkstrakurikulerDetailView(DetailView):
    model = Ekstrakurikuler

class EkstrakurikulerAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Ekstrakurikuler
    form_class = EkstrakurikulerForm
    success_url = '/app/ekskul-list'

class EkstrakurikulerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Ekstrakurikuler
    form_class = EkstrakurikulerForm
    success_url = '/app/ekskul-list'

class EkstrakurikulerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Ekstrakurikuler
    success_url = reverse_lazy("ekskul-list")



"""
View : Memodifikasi CatatanWalikelas Model
"""

class CatatanWalikelasListView(ListView):
    model = CatatanWalikelas

class CatatanWalikelasDetailView(DetailView):
    model = CatatanWalikelas

class CatatanWalikelasAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = CatatanWalikelas
    form_class = CatatanWalikelasForm
    success_url = '/app/catatan-list'

class CatatanWalikelasUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = CatatanWalikelas
    form_class = CatatanWalikelasForm
    success_url = '/app/catatan-list'

class CatatanWalikelasDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = CatatanWalikelas
    success_url = reverse_lazy("catatan-list")