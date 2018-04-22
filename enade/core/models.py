# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from sorl.thumbnail import ImageField
from django.template.defaultfilters import slugify

# Create your models here.
ar_periodo=((None,"Selecione um Periodo"),
               (1,"1"),
               (2,"2"),
               (3,"3"),
               (4,"4"),
               (5,"5"),
               (6,"6"),
               (7,"7"),
               (8,"8"),
               (9,"9"),
               (10,"10"),
              )
ar_opcao=((None,"Selecione uma Resposta"),
               ('A',"A"),
               ('B',"B"),
               ('C',"C"),
               ('D',"D"),
               ('E',"E")
              )
class Curso(models.Model):
    ar_status= ((None,""),(True,"Ativo"),(False,"Inativo"))
    cd_curso = models.AutoField(primary_key=True,editable=False)
    no_curso = models.CharField("Curso",max_length=150, blank=False)
    bo_curso = models.NullBooleanField("Status",choices=ar_status,blank=True)

    class Meta:
        managed = False
        db_table = 'tb_curso'
    def __str__(self):
        return self.no_curso

curso = Curso.objects.all()
listaCurso=list([('', '-- Selecione um Curso --'), ] + [(t.cd_curso, t.no_curso) for t in curso]);

class PeriodoAvaliativo(models.Model):
    ar_status= ((None,""),(True,"Ativo"),(False,"Inativo"))
    cd_periodo_avaliativo = models.AutoField(primary_key=True,editable=False)
    no_periodo_avaliativo = models.CharField("Periodo Avaliativo",max_length=150, blank=False)
    bo_ativo = models.NullBooleanField("Status",choices=ar_status,blank=True)

    class Meta:
        managed = False
        db_table = 'tb_periodo_avaliativo'

    def __str__(self):
        return self.no_periodo_avaliativo

periodoAva = PeriodoAvaliativo.objects.all()
listaPeriodoAva=list([('', '-- Selecione um Periodo avaliativo --'), ] + [(t.cd_periodo_avaliativo, t.no_periodo_avaliativo) for t in periodoAva]);


class Aluno(models.Model):
    cd_academico = models.AutoField(primary_key=True,editable=False)
    no_academico = models.CharField("Academico",max_length=150, blank=False)
    email = models.EmailField("E-mail",blank=True)
    cd_curso = models.IntegerField("Curso",choices=listaCurso)
    nu_cod_academico = models.CharField("Codigo do academico",max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'tb_academico'

    def __str__(self):
      return self.no_academico

    @staticmethod
    def autocomplete_search_fields():
        return ('no_academico', 'nu_cod_academico')

class Gabarito(models.Model):
    cd_gabarito = models.AutoField(primary_key=True,editable=False)
    cd_periodo = models.IntegerField("Periodo",choices=ar_periodo,blank=False)
    cd_curso = models.IntegerField("Curso",choices=listaCurso)
    cd_periodo_avaliativo = models.IntegerField("Periodo Avaliativo ", choices=listaPeriodoAva)
    class Meta:
        managed = False
        db_table = 'tb_gabarito'

    def __str__(self):
        return "Salvo com Sucesso"

class GabaritoResposta(models.Model):
    cd_gabarito_resposta = models.AutoField(primary_key=True,editable=False)
    nu_questao = models.CharField("N da Questao",max_length=2,blank=False)
    res_questao = models.CharField("Resposta da Questo",max_length=1,choices=ar_opcao)
    cd_gabarito = models.ForeignKey(Gabarito, db_column= 'cd_gabarito')

    class Meta:
        managed = False
        db_table = 'tb_gabarito_resposta'

    def __str__(self):
        return "Salvo com Sucesso"

class PeriodoAvaliativoAcademico(models.Model):

    cd_avaliativo_academico = models.AutoField(primary_key=True,editable=False)
    cd_periodo_avaliativo = models.IntegerField("Periodo Avaliativo",choices=listaPeriodoAva)
    cd_academico = models.ForeignKey(Aluno,db_column= 'cd_academico',on_delete=models.CASCADE)
    nu_matricula = models.CharField("Matricula",max_length=15,blank=False)
    cd_periodo = models.IntegerField("Periodo",choices=ar_periodo,blank=False)

    class Meta:
        managed = False
        db_table = 'tb_periodo_avaliativo_has_tb_academico'
        # order_with_respect_to = 'tb_academico'

    def __str__(self):
        return "Salvo com Sucesso"

def rename_file_and_upload_to(objeto, arquivo):
	"""
	Essa função irá normalizar como um slug, o nome do arquivo que está sendo gravado e, irá gravá-lo
	em /media/uploads/APPNAME_CLASSNAME/nome_do_arquivo_normalizado.extensao
	"""
	import os
	caminho = str( '%s/%s' % ( objeto._meta.app_label, objeto.__class__.__name__ ) ).lower()
	nome, ext = os.path.splitext( arquivo )
	url = slugify( nome[:15] )
	return os.path.join( 'core/static', caminho, url+ext )

class Imagem(models.Model):
    class Meta:
        ordering = ('nome', )
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        db_table = 'tb_upload_gabarito'
    cd_arquivo = models.AutoField(primary_key=True,editable=False)
    ds_arquivo  = ImageField(
        u'Imagem', upload_to=rename_file_and_upload_to, max_length=255
    )
    nome = models.CharField("Nome da imagem",max_length=255)
    cd_avaliativo_academico = models.IntegerField("Periodo",choices=ar_periodo,blank=False)
    def imagemAdmin(self):
        from sorl.thumbnail import get_thumbnail
        if self.nome:
            try:
                im = get_thumbnail(self.nome, '100x70', quality=80)
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''
    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'
    def imagem(self):
        from sorl.thumbnail import get_thumbnail
        if self.nome:
            try:
                im = get_thumbnail(self.nome, '80x45', quality=80)
                return im.url
            except:
                return ''
        return ''
    def __str__(self):
        return self.ds_arquivo.url
    def url(self):
        return reverse('imagem', args=(self.slug,))

class GabaritoAcademico(models.Model):
    cd_gabarito_academico = models.AutoField(primary_key=True,editable=False)
    nu_questao = models.IntegerField()
    res_questao = models.CharField(max_length=2)
    cd_avaliativo_academico = models.IntegerField()
    cd_usuario = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tb_gabarito_academico'
    def __unicode__(self):
        return self.res_questao

class QuestionarioAcademico(models.Model):
    cd_gabarito_questionario = models.AutoField(primary_key=True,editable=False)
    nu_questionario = models.IntegerField()
    res_questionario = models.CharField(max_length=2)
    cd_avaliativo_academico = models.IntegerField()
    cd_usuario = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tb_gabarito_questionario'
    def __unicode__(self):
        return self.res_questionario

class RelatorioAcademicos(models.Model):
    cd_gabarito_questionario = models.AutoField(primary_key=True,editable=False)
    nu_questionario = models.IntegerField()
    res_questionario = models.CharField(max_length=2)
    cd_avaliativo_academico = models.IntegerField()
    cd_usuario = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'tb_gabarito_questionario'

    def __unicode__(self):
        return self.res_questionario
