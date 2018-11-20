from django.contrib import admin
from .models import category, obra, pessoa, pessoaVoto, voto

admin.site.register(category)

class obraAdmin(admin.ModelAdmin):
    list_display = ('insc_obra', 'nome_obra', 'category_obra',)
    list_filter = ('category_obra',)


admin.site.register(obra, obraAdmin)
admin.site.register(pessoa)
admin.site.register(pessoaVoto)

class votoAdmin(admin.ModelAdmin):
    list_display = ('obraVotada', 'quantidadeVotos', 'category_obra',)
    list_filter = ('quantidadeVotos','category_obra',)


admin.site.register(voto, votoAdmin)
