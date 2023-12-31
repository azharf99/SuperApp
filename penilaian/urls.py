from django.urls import path

from penilaian.views import NilaiListView, NilaiAddView, NilaiDetailView, NilaiUpdateView, NilaiDeleteView, \
    NilaiSikapListView, NilaiSikapAddView, NilaiSikapDetailView, NilaiSikapUpdateView, NilaiSikapDeleteView, \
    PresensiListView, PresensiAddView, PresensiDetailView, PresensiUpdateView, PresensiDeleteView, PrestasiListView, \
    PrestasiAddView, PrestasiDetailView, PrestasiUpdateView, PrestasiDeleteView, EkstrakurikulerListView, \
    EkstrakurikulerAddView, EkstrakurikulerDetailView, EkstrakurikulerUpdateView, EkstrakurikulerDeleteView, \
    CatatanWalikelasListView, CatatanWalikelasAddView, CatatanWalikelasDetailView, CatatanWalikelasUpdateView, \
    CatatanWalikelasDeleteView

urlpatterns = [
    path('', NilaiListView.as_view(), name='nilai-index'),
    path('nilai/add', NilaiAddView.as_view(), name='nilai-add'),
    path('nilai/<str:pk>', NilaiDetailView.as_view(), name='nilai-detail'),
    path('nilai/update/<str:pk>', NilaiUpdateView.as_view(), name='nilai-update'),
    path('nilai/delete/<str:pk>', NilaiDeleteView.as_view(), name='nilai-delete'),
    path('sikap-list', NilaiSikapListView.as_view(), name='sikap-list'),
    path('sikap/add', NilaiSikapAddView.as_view(), name='sikap-add'),
    path('sikap/<str:pk>', NilaiSikapDetailView.as_view(), name='sikap-detail'),
    path('sikap/update/<str:pk>', NilaiSikapUpdateView.as_view(), name='sikap-update'),
    path('sikap/delete/<str:pk>', NilaiSikapDeleteView.as_view(), name='sikap-delete'),
    path('presensi-list', PresensiListView.as_view(), name='presensi-list'),
    path('presensi/add', PresensiAddView.as_view(), name='presensi-add'),
    path('presensi/<str:pk>', PresensiDetailView.as_view(), name='presensi-detail'),
    path('presensi/update/<str:pk>', PresensiUpdateView.as_view(), name='presensi-update'),
    path('presensi/delete/<str:pk>', PresensiDeleteView.as_view(), name='presensi-delete'),
    path('prestasi-list', PrestasiListView.as_view(), name='prestasi-list'),
    path('prestasi/add', PrestasiAddView.as_view(), name='prestasi-add'),
    path('prestasi/<str:pk>', PrestasiDetailView.as_view(), name='prestasi-detail'),
    path('prestasi/update/<str:pk>', PrestasiUpdateView.as_view(), name='prestasi-update'),
    path('prestasi/delete/<str:pk>', PrestasiDeleteView.as_view(), name='prestasi-delete'),
    path('ekskul-list', EkstrakurikulerListView.as_view(), name='ekskul-list'),
    path('ekskul/add', EkstrakurikulerAddView.as_view(), name='ekskul-add'),
    path('ekskul/<str:pk>', EkstrakurikulerDetailView.as_view(), name='ekskul-detail'),
    path('ekskul/update/<str:pk>', EkstrakurikulerUpdateView.as_view(), name='ekskul-update'),
    path('ekskul/delete/<str:pk>', EkstrakurikulerDeleteView.as_view(), name='ekskul-delete'),
    path('catatan-list', CatatanWalikelasListView.as_view(), name='catatan-list'),
    path('catatan/add', CatatanWalikelasAddView.as_view(), name='catatan-add'),
    path('catatan/<str:pk>', CatatanWalikelasDetailView.as_view(), name='catatan-detail'),
    path('catatan/update/<str:pk>', CatatanWalikelasUpdateView.as_view(), name='catatan-update'),
    path('catatan/delete/<str:pk>', CatatanWalikelasDeleteView.as_view(), name='catatan-delete'),
]
