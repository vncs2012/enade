# -*- coding: utf-8 -*-
from django.contrib import admin
from threading import Thread
from time import sleep
from .models import Aluno
from .models import PeriodoAvaliativo
from .models import Curso
from .models import Gabarito,GabaritoResposta
from .models import PeriodoAvaliativoAcademico
from .models import Imagem,RelatorioAcademicos
from jet.admin import CompactInline
from multiupload.admin import MultiUploadAdmin
from sorl.thumbnail.admin import AdminImageMixin
from upload import uploadProcessamento


class GabaritoRespostaInline(CompactInline):
    model = GabaritoResposta
    fk_name = 'cd_gabarito'
    can_delete = False
    verbose_name_plural = 'Resposta Gabarito'
    extra = 21
    show_change_link = True

class GabaritoAdmin(admin.ModelAdmin ):
    inlines = [GabaritoRespostaInline,]
    list_display = ('cd_periodo', 'cd_curso','cd_periodo_avaliativo')
    # list_display_links = ('no_academico', 'email','cd_curso','nu_cod_academico')
    # list_filter = ( 'no_academico', 'email','cd_curso','nu_cod_academico')
    list_per_page = 25

class PeriodoAvaliativoAdmin(admin.ModelAdmin):
    list_display = ('no_periodo_avaliativo', 'bo_ativo')
    # list_display_links = ('no_periodo_avaliativo', 'bo_ativo')
    search_fields = ('no_PeriodoAvaliativoAcademicoperiodo_avaliativo', 'bo_ativo')
    list_per_page = 25

class CursoAdmin(admin.ModelAdmin):
    list_display = ('no_curso', 'bo_curso')
    # list_display_links = ('no_curso', 'bo_curso')
    search_fields = ('no_curso', 'bo_curso')

class ImagemAdmin(AdminImageMixin, MultiUploadAdmin):
    list_display = ('nome', 'imagemAdmin', )
    # default value of all parameters:
    change_form_template = 'multiupload/change_form.html'
    change_list_template = 'multiupload/change_list.html'
    multiupload_template = 'multiupload/upload.html'
    # if true, enable multiupload on list screen
    # generaly used when the model is the uploaded element
    multiupload_list = True
    # if true enable multiupload on edit screen
    # generaly used when the model is a container for uploaded files
    # eg: gallery
    # can upload files direct inside a gallery.
    multiupload_form = True
    # max allowed filesize for uploads in bytes
    # 3 Mb
    multiupload_maxfilesize = 3 * 2 ** 20
    # min allowed filesize for uploads in bytes
    multiupload_minfilesize = 0
    # tuple with mimetype accepted
    multiupload_acceptedformats = (
        "image/jpeg",
        "image/pjpeg",
        "image/png",
    )

    def process_uploaded_file(self, uploaded, object, request):
        title = request.POST.get('title', '') or uploaded.name
        try:
            sleep(1)
            f = Imagem(ds_arquivo=uploaded,nome=title)
            f.save()
            cd_arquivo =f.cd_arquivo
            urlArquivo =str(f.ds_arquivo.url)
            thread = Thread(target=uploadProcessamento, args=(urlArquivo,cd_arquivo,request,title,))
            thread.setDaemon = True
            thread.start()
            thread.join()
        except Exception:
            pass
        return {
                'url': f.imagem(),
                'thumbnail_url': f.imagem(),
                'id': f.cd_arquivo,
            }   
    def delete_file(self, pk, request):
        '''
        Function to delete a file.
        '''
        # This is the default implementation.
        obj = get_object_or_404(self.queryset(request), pk=pk.cd_arquivo)
        obj.delete()

class RelatorioAcademicosAdmin(admin.ModelAdmin):
    change_list_template = "relatorio/relatorioAcademico.html"

class AlunoInline(CompactInline):
    model = PeriodoAvaliativoAcademico
    fk_name = 'cd_academico'
    can_delete = False
    verbose_name_plural = 'Informação do Semestre'
    extra = 1
    show_change_link = True

class AlunoAdmin(admin.ModelAdmin ):
    inlines = [AlunoInline,]
    list_display = ('no_academico', 'email','cd_curso','nu_cod_academico')
    list_filter = ( 'no_academico', 'email','cd_curso','nu_cod_academico')
    list_per_page = 25

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(PeriodoAvaliativo, PeriodoAvaliativoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Gabarito, GabaritoAdmin)
admin.site.register(Imagem, ImagemAdmin)
admin.site.register(RelatorioAcademicos, RelatorioAcademicosAdmin)
