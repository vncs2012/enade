# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files import File

# Create your tests here.

import unittest

from models import PeriodoAvaliativo, Curso, Aluno, PeriodoAvaliativoAcademico, Gabarito, GabaritoResposta, QuestionarioAcademico, GabaritoAcademico, Imagem

class PeriodoAvaliativoTestCase(unittest.TestCase):
    def setUp(self):
        PeriodoAvaliativo.objects.create(no_periodo_avaliativo='2018/2', bo_ativo=True)
        PeriodoAvaliativo.objects.create(no_periodo_avaliativo='2018/1', bo_ativo=True)

    def test_PeriodoAvaliativo(self):
        primeiro = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/2")
        segundo = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/1")
        self.assertEqual(primeiro.no_periodo_avaliativo, '2018/2')
        self.assertEqual(segundo.no_periodo_avaliativo, '2018/1')

    def test_PeriodoA_update(self):
        primeiro = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/2")
        segundo = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/1")
        primeiro.no_periodo_avaliativo = "primeiro"
        primeiro.save()
        segundo.no_periodo_avaliativo="segundo"
        segundo.save()
        self.assertEqual(primeiro.no_periodo_avaliativo, 'primeiro')
        self.assertEqual(segundo.no_periodo_avaliativo, 'segundo')
        
    def test_PeriodoA_remove(self):
        primeiro = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/2")
        primeiro.delete()
        segundo = PeriodoAvaliativo.objects.get(no_periodo_avaliativo="2018/1")
        segundo.delete()
        self.assertNotEqual(primeiro, '')
        self.assertNotEqual(segundo, '')

class CursoTestCase(unittest.TestCase):
    def setUp(self):
        Curso.objects.create(no_curso='Biologia', bo_curso=False)

    def test_Curso(self):
        curso = Curso.objects.get(no_curso='Biologia')
        self.assertEqual(curso.no_curso, 'Biologia')

    def test_Curso_update(self):
        Curso.objects.create(no_curso='ENG', bo_curso=False)
        alterarCurso = Curso.objects.get(no_curso='ENG')
        alterarCurso.no_curso = 'Medicina'
        alterarCurso.save()
        self.assertEqual(alterarCurso.no_curso, 'Medicina')
        
    def test_Curso_remove(self):
        Curso.objects.get(cd_curso=1).delete()

class AlunoTestCase(unittest.TestCase):
    def setUp(self):
        Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")

    def test_Aluno(self):
        aluno = Aluno.objects.get(no_academico='Vinicius')
        self.assertEqual(aluno.no_academico, 'Vinicius')

    def test_Aluno_update(self):
        Aluno.objects.create(no_academico='jose', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        alterarAluno = Aluno.objects.get(no_academico='jose')
        alterarAluno.no_academico = 'Richard'
        alterarAluno.save()
        self.assertEqual(alterarAluno.no_academico, 'Richard')
        
    def test_Aluno_remove(self):
        Aluno.objects.get(cd_academico=1).delete() 

class PeriodoAvaliativoAcademicoTestCase(unittest.TestCase):
    def setUp(self):
        aluno= Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        PeriodoAvaliativoAcademico.objects.create(cd_periodo_avaliativo=1, cd_academico=aluno,nu_matricula="000024",cd_periodo=7)

    def test_PeriodoAvaliativoAcademico(self):
        periodo = PeriodoAvaliativoAcademico.objects.get(cd_avaliativo_academico=1)
        assert periodo.cd_periodo_avaliativo == 1

    def test_PeriodoAvaliativoAcademico_update(self):
        alterarperiodo = PeriodoAvaliativoAcademico.objects.filter(nu_matricula="000024").update(cd_periodo=8)
        assert alterarperiodo != None
    def test_PeriodoAvaliativoAcademico_remove(self):
        PeriodoAvaliativoAcademico.objects.get(cd_avaliativo_academico=1).delete()

class GabaritoTestCase(unittest.TestCase):
    def setUp(self):
        aluno= Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        periodo =PeriodoAvaliativoAcademico.objects.create(cd_periodo_avaliativo=1, cd_academico=aluno,nu_matricula="000024",cd_periodo=7)
        curso = Curso.objects.create(no_curso='Biologia', bo_curso=False)
        Gabarito.objects.create(cd_periodo=5, cd_curso=curso.cd_curso,cd_periodo_avaliativo=periodo.cd_periodo_avaliativo)

    def test_Gabarito(self):
        gabarito = Gabarito.objects.get(cd_gabarito=1)
        assert gabarito != None

    def test_Gabarito_update(self):
        alterarGabarito = Gabarito.objects.filter(cd_gabarito=1).update(cd_periodo=8)
        assert alterarGabarito != None
    
    def test_Gabarito_remove(self):
        Gabarito.objects.get(cd_gabarito=1).delete()  

class GabaritoRespostaTestCase(unittest.TestCase):
    def setUp(self):
        aluno= Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        periodo =PeriodoAvaliativoAcademico.objects.create(cd_periodo_avaliativo=1, cd_academico=aluno,nu_matricula="000024",cd_periodo=7)
        curso = Curso.objects.create(no_curso='Biologia', bo_curso=False)
        gabrito = Gabarito.objects.create(cd_periodo=5, cd_curso=curso.cd_curso,cd_periodo_avaliativo=periodo.cd_periodo_avaliativo)
        GabaritoResposta.objects.create(nu_questao='1', res_questao='A',cd_gabarito=gabrito)

    def test_GabaritoResposta(self):
        gabarito = GabaritoResposta.objects.get(cd_gabarito_resposta=1)
        assert gabarito != None

    def test_GabaritoResposta_update(self):
        alterarGabarito = GabaritoResposta.objects.filter(cd_gabarito_resposta=1).update(nu_questao='2', res_questao='B')
        assert alterarGabarito != None
    
    def test_GabaritoResposta_remove(self):
        GabaritoResposta.objects.get(cd_gabarito_resposta=1).delete()

class QuestionarioAcademicoTestCase(unittest.TestCase):
    def setUp(self):
        aluno= Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        periodo =PeriodoAvaliativoAcademico.objects.create(cd_periodo_avaliativo=1, cd_academico=aluno,nu_matricula="000024",cd_periodo=7)
        curso = Curso.objects.create(no_curso='Biologia', bo_curso=False)
        gabrito = Gabarito.objects.create(cd_periodo=5, cd_curso=curso.cd_curso,cd_periodo_avaliativo=periodo.cd_periodo_avaliativo)
        QuestionarioAcademico.objects.create(nu_questionario=1, res_questionario='A',cd_avaliativo_academico=1,cd_usuario=1)

    def test_QuestionarioAcademico(self):
        gabarito = QuestionarioAcademico.objects.get(cd_gabarito_questionario=1)
        assert gabarito != None

    def test_QuestionarioAcademico_update(self):
        alterarGabarito = QuestionarioAcademico.objects.filter(cd_gabarito_questionario=1).update(nu_questionario='2', res_questionario='B')
        assert alterarGabarito != None
    
    def test_QuestionarioAcademico_remove(self):
        QuestionarioAcademico.objects.get(cd_gabarito_questionario=1).delete()

class GabaritoAcademicoTestCase(unittest.TestCase):
    def setUp(self):
        aluno= Aluno.objects.create(no_academico='Vinicius', email="vncs@gmai.com",cd_curso=1,nu_cod_academico="00001")
        periodo =PeriodoAvaliativoAcademico.objects.create(cd_periodo_avaliativo=1, cd_academico=aluno,nu_matricula="000024",cd_periodo=7)
        curso = Curso.objects.create(no_curso='Biologia', bo_curso=False)
        gabrito = Gabarito.objects.create(cd_periodo=5, cd_curso=curso.cd_curso,cd_periodo_avaliativo=periodo.cd_periodo_avaliativo)
        GabaritoAcademico.objects.create(nu_questao=1, res_questao='A',cd_avaliativo_academico=1,cd_usuario=1)

    def test_QuestionarioAcademico(self):
        gabarito = GabaritoAcademico.objects.get(cd_gabarito_academico=1)
        assert gabarito != None

    def test_QuestionarioAcademico_update(self):
        alterarGabarito = GabaritoAcademico.objects.filter(cd_gabarito_academico=1).update(nu_questao=2, res_questao='B')
        assert alterarGabarito != None
    
    def test_QuestionarioAcademico_remove(self):
        GabaritoAcademico.objects.get(cd_gabarito_academico=1).delete()                                           