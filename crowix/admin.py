from django.contrib import admin
from .models import artical,product,news,certif
from DjangoUeditor.models import UEditorField

class articalAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'tag','slug')
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'tag','slug')
class newsAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'time')
class certifAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'time')

# Register your models here.
admin.site.register(artical, articalAdmin)
admin.site.register(product, productAdmin)
admin.site.register(news, newsAdmin)
admin.site.register(certif, certifAdmin)