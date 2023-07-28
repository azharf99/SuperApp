from django import forms
from master.models import *
from django.utils.translation import gettext_lazy as _

                                
class GuruForm(forms.ModelForm):
    class Meta:
        model = Guru
        fields = ['nama_guru', 'jenis_kelamin', 'alamat', 'jabatan', 'email', 'nomor_hp', 'status', 'foto']
        labels = {
                "niy": _("Nomor Induk Yayasan"),
                "nama_guru": _("Nama Guru"),
            }
        help_texts = {
                "niy": _("Nomor induk yayasan harus unik."),
            }
        error_messages = {
                "nama_guru": {
                    "max_length": _("Nama teralu panjang."),
                },
            }
        
class SiswaForm(forms.ModelForm):
    class Meta:
        model = Siswa
        fields = '__all__'


class JurusanForm(forms.ModelForm):
    class Meta:
        model = Jurusan
        fields = '__all__'


class MataPelajaranForm(forms.ModelForm):
    class Meta:
        model = MataPelajaran
        fields = '__all__'


class KelasForm(forms.ModelForm):
    class Meta:
        model = Kelas
        fields = '__all__'


class MengajarForm(forms.ModelForm):
    class Meta:
        model = Mengajar
        fields = '__all__'


class WaliKelasForm(forms.ModelForm):
    class Meta:
        model = WaliKelas
        fields = '__all__'


class BelajarSiswaForm(forms.ModelForm):
    class Meta:
        model = BelajarSiswa
        fields = '__all__'


class JadwalMengajarForm(forms.ModelForm):
    class Meta:
        model = JadwalMengajar
        fields = '__all__'
    
