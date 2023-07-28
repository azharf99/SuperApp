from django.urls import path
from pelanggaran.views import PelanggaranListView, PelanggaranAddView, PelanggaranDetailView, PelanggaranUpdateView, \
    PelanggaranDeleteView

urlpatterns = [
    path('', PelanggaranListView.as_view(), name='pelanggaran-index'),
    path('pelanggaran/add', PelanggaranAddView.as_view(), name='pelanggaran-add'),
    path('pelanggaran/<str:pk>', PelanggaranDetailView.as_view(), name='pelanggaran-detail'),
    path('pelanggaran/update/<str:pk>', PelanggaranUpdateView.as_view(), name='pelanggaran-update'),
    path('pelanggaran/delete/<str:pk>', PelanggaranDeleteView.as_view(), name='pelanggaran-delete'),
]
