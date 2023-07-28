from django import forms
from django.utils.translation import gettext_lazy as _
from penilaian.models import Nilai, NilaiSikap, Prestasi, Ekstrakurikuler, Presensi, CatatanWalikelas


class NilaiForm(forms.ModelForm):
    class Meta:
        model = Nilai
        fields = '__all__'


class NilaiSikapForm(forms.ModelForm):
    class Meta:
        model = NilaiSikap
        fields = '__all__'


class PresensiForm(forms.ModelForm):
    class Meta:
        model = Presensi
        fields = '__all__'


class PrestasiForm(forms.ModelForm):
    class Meta:
        model = Prestasi
        fields = '__all__'


class EkstrakurikulerForm(forms.ModelForm):
    class Meta:
        model = Ekstrakurikuler
        fields = '__all__'


class CatatanWalikelasForm(forms.ModelForm):
    class Meta:
        model = CatatanWalikelas
        fields = '__all__'