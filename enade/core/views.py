# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string
from django.template.loader import get_template
import datetime
from xhtml2pdf import pisa 
from django import template
from django.db import connection
from django.views.decorators.csrf import csrf_exempt,requires_csrf_token,csrf_protect
from core.models import Aluno,Curso,PeriodoAvaliativo

@csrf_exempt
def home(reques):
    cursor = connection.cursor()
    cursor.execute("SELECT * from tb_periodo_avaliativo")

    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))

    context = {
        'pavaliativo': result
    }
    return render_to_response('core/index.html',context)

@csrf_exempt
def Desempenho(request):
    mat = request.POST.get('mat')
    cd_periodo = request.POST.get('cd_periodo')
    respostas = getRespostas(mat,cd_periodo)
    questoes = getGabarito(mat,cd_periodo)
    resAcademico = getRespostasAcademico(mat,cd_periodo)
    respostaAcademico = desepenhoAcadmicomontar(respostas,resAcademico)
    imagem = getImagem(mat,cd_periodo)
    context = {
    'resposta': respostas,
    'questoes':questoes,
    'resacademico' :respostaAcademico,
    'gabarito': imagem[0],
    'academico': Aluno.objects.filter(nu_cod_academico=mat)[0].no_academico
    }
    html = render_to_string('core/desempenho.html',context)
    
    return HttpResponse(html)

@csrf_exempt
def getCurso(request):
    context = {
    'curso': Curso.objects.all()    
    }
    html = render_to_string('relatorio/selectCurso.html',context)
    
    return HttpResponse(html)
    
@csrf_exempt
def relatorioAcademicoPeriodo(request):
    cd_curso = request.POST.get('cd_curso')
    cd_periodo = request.POST.get('cd_periodo')
   
    context = {
        "resultado": getRelatorioAcademicoPeriodo(cd_curso,cd_periodo),
        "curso": Curso.objects.filter(cd_curso=cd_curso)[0].no_curso,
        "acertadas": getRelatorioAcertosQuestoes(cd_curso,cd_periodo),
        "periodo":cd_periodo
    }
 
    html  = render_to_string('relatorio/relatorioAcademicoPeriodo.html',context)
    file = open('relatoriosPDF/'+cd_periodo+'-'+cd_curso+'.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')

    file.seek(0)
    pdf = file.read()
    file.close()
          
    return HttpResponse(pdf, 'application/pdf')

def getRespostas(mat,cd_periodo):
    cursor = connection.cursor()
    sql="SELECT gr.nu_questao,gr.res_questao ,pa.no_periodo_avaliativo,a.nu_cod_academico from correcao_gabarito.tb_periodo_avaliativo pa \
    join correcao_gabarito.tb_periodo_avaliativo_has_tb_academico pha USING(cd_periodo_avaliativo)\
    join correcao_gabarito.tb_academico a USING(cd_academico)\
    join correcao_gabarito.tb_gabarito_academico ga USING(cd_avaliativo_academico)\
    join correcao_gabarito.tb_gabarito g USING(cd_periodo_avaliativo)\
    join correcao_gabarito.tb_gabarito_resposta gr USING(cd_gabarito)\
    where gr.nu_questao = ga.nu_questao and gr.res_questao = ga.res_questao and a.nu_cod_academico='"+mat+"'\
    and pa.cd_periodo_avaliativo ="+ cd_periodo

    cursor.execute(sql)
    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def getImagem(mat,cd_periodo):
    cursor = connection.cursor()
    sql="SELECT ds_arquivo from tb_periodo_avaliativo pa \
        join tb_periodo_avaliativo_has_tb_academico pha USING(cd_periodo_avaliativo)\
        join tb_academico a USING(cd_academico)\
        join correcao_gabarito.tb_upload_gabarito aa using(cd_avaliativo_academico)\
        where a.nu_cod_academico='"+mat+"'\
        and pa.cd_periodo_avaliativo ="+ cd_periodo
    
    cursor.execute(sql)
    return  cursor.fetchone()

def getGabarito(mat,cd_periodo):
    cursor = connection.cursor()
    cd_curso = Aluno.objects.filter(nu_cod_academico=mat)[0].cd_curso
    sql="SELECT gr.nu_questao,gr.res_questao ,pa.no_periodo_avaliativo from tb_periodo_avaliativo pa \
    join tb_gabarito g USING(cd_periodo_avaliativo)\
    join tb_gabarito_resposta gr USING(cd_gabarito)\
    where  pa.cd_periodo_avaliativo ="+ cd_periodo

    cursor.execute(sql)
    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def getRespostasAcademico(mat,cd_periodo):
    cursor = connection.cursor()
    sql="SELECT ga.nu_questao,ga.res_questao ,pa.no_periodo_avaliativo from tb_periodo_avaliativo pa \
    join tb_periodo_avaliativo_has_tb_academico pha USING(cd_periodo_avaliativo)\
    join tb_academico a USING(cd_academico)\
    join tb_gabarito_academico ga USING(cd_avaliativo_academico)\
    where  a.nu_cod_academico='"+mat+"'\
    and pa.cd_periodo_avaliativo ="+ cd_periodo

    cursor.execute(sql)
    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def getRelatorioAcademicoPeriodo(cd_curso,cd_periodo):
    cursor = connection.cursor()
    sql="SELECT count(pha.cd_academico) as totalacertadas,pa.no_periodo_avaliativo,ac.no_academico,ac.nu_cod_academico\
         from correcao_gabarito.tb_periodo_avaliativo pa\
		 join correcao_gabarito.tb_periodo_avaliativo_has_tb_academico pha USING(cd_periodo_avaliativo)\
		 join correcao_gabarito.tb_academico ac using(cd_academico)\
		 join correcao_gabarito.tb_gabarito_academico ga USING(cd_avaliativo_academico)\
	     join correcao_gabarito.tb_gabarito g USING(cd_periodo_avaliativo)\
		 join correcao_gabarito.tb_gabarito_resposta gr USING(cd_gabarito)\
		 where gr.nu_questao = ga.nu_questao and gr.res_questao = ga.res_questao\
		 and pa.bo_ativo and g.cd_periodo = "+cd_periodo+" and g.cd_curso = "+cd_curso+" \
		GROUP by no_periodo_avaliativo,pha.cd_academico\
		ORDER by totalacertadas DESC"
        
    cursor.execute(sql)
    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def getRelatorioAcertosQuestoes(cd_curso,cd_periodo):
    cursor = connection.cursor()
    sql="SELECT gr.nu_questao,count(gr.res_questao) as totalacertadas,pa.no_periodo_avaliativo from correcao_gabarito.tb_periodo_avaliativo pa\
		 join correcao_gabarito.tb_periodo_avaliativo_has_tb_academico pha USING(cd_periodo_avaliativo)\
		 join correcao_gabarito.tb_gabarito_academico ga USING(cd_avaliativo_academico)\
	     	 join correcao_gabarito.tb_gabarito g USING(cd_periodo_avaliativo)\
		 join correcao_gabarito.tb_gabarito_resposta gr USING(cd_gabarito)\
		 where gr.nu_questao = ga.nu_questao and gr.res_questao = ga.res_questao\
		 and pa.bo_ativo and g.cd_periodo = "+cd_periodo+" and g.cd_curso = "+cd_curso+"\
		 GROUP by gr.nu_questao,gr.res_questao,no_periodo_avaliativo\
		 ORDER by gr.nu_questao"
        
    cursor.execute(sql)
    fieldnames = [name[0] for name in cursor.description]
    result =[]
    for row in cursor.fetchall():
        rowset=[]
        for field in zip(fieldnames,row):
            rowset.append(field)
        result.append(dict(rowset))
    return result

def desepenhoAcadmicomontar(certas,respostas):
    for k,certa in enumerate(certas):
        for kk,resposta in enumerate(respostas):
            if ((certa.get('nu_questao',k) == resposta.get('nu_questao',kk)) and (certa.get('res_questao',k)  == resposta.get('res_questao',kk))): 
                dict(dic0.items() + dic1.items())
    return respostas