from django import forms
from django.utils.translation import gettext_lazy as _
from pelanggaran.models import Pelanggaran


class PelanggaranForm(forms.ModelForm):
    class Meta:
        model = Pelanggaran
        fields = '__all__'