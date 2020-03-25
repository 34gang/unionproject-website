from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phonenumber_field.modelfields import PhoneNumberField
from short_text_field.models import ShortTextField

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Nama_Depan = models.CharField(max_length=40, default="",blank=False)
    Nama_Belakang = models.CharField(max_length=40, default="",blank=False)
    Alamat_Email = models.EmailField()
    Tanggal_Lahir = models.DateField(default="", blank=False, help_text="Masukkan dalam format MM/DD/YYYY. Contoh: 01/01/2000", error_messages="Tanggal Lahir harus dalam format Bulan/Tanggal/Tahun dan berbentuk angka semua. Jangan lupa untuk menambahkan /. Contoh: 01/01/2000")
    kota = ShortTextField(default='', blank=False, help_text="Masukkan nama kota dengan benar")
    GENDER_CHOICES = (('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan'))
    Jenis_Kelamin = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=False)
    Nomor_HP = PhoneNumberField(default='+62',null=False, blank=False, unique=True, max_length=15)
    Akun_Instagram = models.CharField(blank=False, null=False, default="@", max_length=35)
    bio = models.TextField(default='', blank=True)

    def __str__(self):
        return self.user.username
