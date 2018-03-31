from time import sleep
from correcao import correcao 
from .models import Imagem
from .models import PeriodoAvaliativoAcademico
from .models import GabaritoAcademico,QuestionarioAcademico

def uploadProcessamento(urlArquivo,cd_arquivo,request,title):
    sleep(1)
    imagem_original= urlArquivo
    # matricula da prova e update do cd_avaliativo_academico
    img_codigo=correcao.getCorteCodigoAluno(imagem_original)
    codigoAcademico = correcao.getInscricao(img_codigo)
    # import pdb; pdb.set_trace()
    consulta_matricula = PeriodoAvaliativoAcademico.objects.get(nu_matricula=codigoAcademico)   
    Imagem.objects.filter(pk=cd_arquivo).update(cd_avaliativo_academico=consulta_matricula.cd_avaliativo_academico)
    #Corrigindo gabarito
    respostas={}
    img_prova = correcao.getCorteRespostaGabarito(imagem_original)
    respostas = correcao.getRespostaGabarito(img_prova)
    # Salvando gabarito
    for i in respostas:
        ga= GabaritoAcademico(nu_questao=i,res_questao=respostas[i],cd_avaliativo_academico=consulta_matricula.cd_avaliativo_academico,cd_usuario=request.user.id)
        ga.save()
    #salvar e procesamento do questionario
    questionario={}
    img_questionario= correcao.getCorteQuestionario(imagem_original)
    questionario= correcao.getRespostaQestionario(img_questionario)
    # import pdb; pdb.set_trace()
    for i in questionario:
        qe= QuestionarioAcademico(nu_questionario=i,res_questionario=questionario[i],cd_avaliativo_academico=consulta_matricula.cd_avaliativo_academico,cd_usuario=request.user.id)
        qe.save()
    # import pdb; pdb.set_trace()
    