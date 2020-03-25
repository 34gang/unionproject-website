from django.contrib import admin
from .models import Post #,Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('judul', 'slug', 'tipe', 'status','Dibuat_Pada')
    list_filter = ("status", 'tipe')
    search_fields = ['judul', 'konten']
    prepopulated_fields = {'slug': ('judul',)}
    summernote_fields = ('konten',)

#@admin.register(Comment)
#class CommentAdmin(admin.ModelAdmin):
    #list_display = ('nama', 'isi', 'post', 'Dibuat_Pada', 'active')
 #   list_filter = ('active', 'Dibuat_Pada')
  #  search_fields = ('nama', 'isi')
   # actions = ['approve_comments']

    #def approve_comments(self, request, queryset):
        #queryset.update(active=True)


admin.site.register(Post, PostAdmin)