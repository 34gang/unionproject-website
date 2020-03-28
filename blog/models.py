from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Dipublikasikan")

)

class Post(models.Model):
    judul = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    TIPE = (('Pemberitahuan/Pengumuman', 'Pemberitahuan/Pengumuman'),
        ('Cerita Pendek/Novel','Cerita Pendek/Novel'),
              ('Edit/Video Musik', 'Edit/Video Musk'),
              ('Desain Grafis', 'Desain Grafis'),
              ('Art/Gambar', 'Art/Gambar'))
    tipe = models.TextField(choices=TIPE, max_length=100)
    konten = models.TextField()
    Diperbarui_Pada = models.DateTimeField(auto_now= True)
    Dibuat_Pada = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-Dibuat_Pada']

    def __str__(self):
        return self.judul

#class Comment(models.Model):
    #post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    #nama = models.CharField(default="", max_length=30)
    #isi = models.TextField()
    #Dibuat_Pada = models.DateTimeField(auto_now_add=True)
    #active = models.BooleanField(default=False)

    #class Meta:
        #ordering = ['Dibuat_Pada']

    #def __str__(self):
        #return 'Comment {} by {}'.format(self.isi, self.nama)