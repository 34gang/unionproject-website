from django.contrib import admin
from .models import Post, Comment  # ,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('judul', 'slug', 'tipe', 'status','Dibuat_Pada')
    list_filter = ("status", 'tipe')
    search_fields = ['judul', 'konten']
    prepopulated_fields = {'slug': ('judul',)}
    summernote_fields = ('konten',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'komentar', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'komentar')