from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from pelanggaran.models import Pelanggaran
from pelanggaran.forms import PelanggaranForm

# Create your views here.

"""
View : Memodifikasi Pelanggaran Model
"""

class PelanggaranListView(ListView):
    model = Pelanggaran

class PelanggaranDetailView(DetailView):
    model = Pelanggaran

class PelanggaranAddView(LoginRequiredMixin, CreateView):
    login_url = "/admin/login/"
    model = Pelanggaran
    form_class = PelanggaranForm
    success_url = '/app/pelanggaran-list'

class PelanggaranUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = Pelanggaran
    form_class = PelanggaranForm
    success_url = '/app/pelanggaran-list'

class PelanggaranDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = Pelanggaran
    success_url = reverse_lazy("pelanggaran-index")

