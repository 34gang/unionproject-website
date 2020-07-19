from django import forms
from accounts.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    Konfirmasi_Password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'Konfirmasi_Password',)

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("Konfirmasi_Password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password tidak cocok"
            )

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('Nama_Depan','Nama_Belakang','Alamat_Email','Tanggal_Lahir','Jenis_Kelamin', 'kota','Nomor_HP', 'Akun_Instagram','bio',)