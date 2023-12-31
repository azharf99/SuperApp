# Generated by Django 4.2.3 on 2023-07-28 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import master.compress_image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BelajarSiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_ajaran', models.CharField(max_length=20)),
                ('semester', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('niy', models.CharField(auto_created=True, max_length=21, primary_key=True, serialize=False)),
                ('nama_guru', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[(None, 'Pilih Jenis Kelamin'), ('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=1)),
                ('alamat', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('nomor_hp', models.CharField(max_length=15)),
                ('status', models.CharField(blank=True, default='Nonaktif', max_length=20, null=True)),
                ('foto', master.compress_image.CompressedImageField(blank=True, default='avatar.png', help_text='Format foto disarankan .jpg/.jpeg', null=True, quality=50, upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='JadwalMengajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(choices=[(None, 'Pilih Hari Mengajar'), ('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'), ('Kamis', 'Kamis'), ('Sabtu', 'Sabtu'), ('Ahad', 'Ahad')], max_length=20)),
                ('jam', models.CharField(choices=[(None, 'Pilih Jam Mengajar'), ('Jam ke-1', 'Jam ke-1 07.00 - 07.30 (Normal)'), ('Jam ke-2', 'Jam ke-2 07.30 - 08.10 (Normal)'), ('Jam ke-3', 'Jam ke-3 08.10 - 08.50 (Normal)'), ('Jam ke-4', 'Jam ke-4 08.55 - 09.35 (Normal)'), ('Jam ke-5', 'Jam ke-5 09.35 - 10.15 (Normal)'), ('Jam ke-6', 'Jam ke-6 10.45 - 11.25 (Normal)'), ('Jam ke-7', 'Jam ke-7 11.25 - 12.10 (Normal)'), ('Jam ke-8', 'Jam ke-8 13.40 - 14.20 (Normal)'), ('Jam ke-9', 'Jam ke-9 14.20 - 15.00 (Normal)')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('kode_jurusan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_jurusan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('kode_kelas', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_kelas', models.CharField(max_length=20)),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.jurusan')),
            ],
        ),
        migrations.CreateModel(
            name='MataPelajaran',
            fields=[
                ('kode_mapel', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_mapel', models.CharField(max_length=40)),
                ('jenis_mapel', models.CharField(choices=[(None, 'Pilih Jenis Mapel'), ('Umum', 'Umum (Diknas)'), ("Syar'i", "Syar'i (Pesantren)")], max_length=20)),
                ('kelompok_mapel', models.CharField(choices=[(None, 'Pilih Kelompok Mapel'), ('Kelompok A', 'Kelompok A (Umum)'), ('Kelompok B', 'Kelompok B (Umum)'), ('Kelompok C', 'Kelompok C (Peminatan)')], max_length=20)),
                ('jurusan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.jurusan')),
            ],
        ),
        migrations.CreateModel(
            name='WaliKelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_ajaran', models.CharField(max_length=20)),
                ('guru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.guru')),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.kelas')),
            ],
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('nis', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nisn', models.CharField(max_length=30)),
                ('nama_siswa', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(choices=[(None, 'Pilih Jenis Kelamin'), ('L', 'Laki-laki'), ('P', 'Perempuan')], max_length=10)),
                ('alamat', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField()),
                ('email', models.EmailField(max_length=50)),
                ('nomor_hp', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=20)),
                ('foto', master.compress_image.CompressedImageField(blank=True, default='avatar.png', help_text='Format foto disarankan .jpg/.jpeg', null=True, quality=50, upload_to='student')),
            ],
            options={
                'indexes': [models.Index(fields=['nis', 'nisn'], name='master_sisw_nis_2a422a_idx')],
            },
        ),
        migrations.CreateModel(
            name='Mengajar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_nilai_pts', models.FileField(blank=True, null=True, upload_to='pts')),
                ('file_nilai_pas', models.FileField(blank=True, null=True, upload_to='pas')),
                ('tahun_ajaran', models.CharField(max_length=20)),
                ('guru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='master.guru')),
                ('kelas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.kelas')),
                ('mapel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.matapelajaran')),
            ],
        ),
        migrations.AddIndex(
            model_name='jurusan',
            index=models.Index(fields=['kode_jurusan'], name='master_juru_kode_ju_f22fa9_idx'),
        ),
        migrations.AddField(
            model_name='jadwalmengajar',
            name='pelajaran',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.mengajar'),
        ),
        migrations.AddField(
            model_name='guru',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='belajarsiswa',
            name='kelas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.kelas'),
        ),
        migrations.AddField(
            model_name='belajarsiswa',
            name='siswa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.siswa'),
        ),
        migrations.AddIndex(
            model_name='matapelajaran',
            index=models.Index(fields=['kode_mapel'], name='master_mata_kode_ma_0bac12_idx'),
        ),
        migrations.AddIndex(
            model_name='kelas',
            index=models.Index(fields=['kode_kelas'], name='master_kela_kode_ke_db40dc_idx'),
        ),
        migrations.AddIndex(
            model_name='guru',
            index=models.Index(fields=['niy'], name='master_guru_niy_0fd50d_idx'),
        ),
    ]
