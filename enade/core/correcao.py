#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

class correcao():
    global ProcessamentoImagen

    @staticmethod
    def getCorteRespostaGabarito(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[1400:2650, 80:468]

    @staticmethod
    def getCorteCodigoAluno(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[870:1330,150:975]

    @staticmethod
    def getCorteQuestionario(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[1350:2000,530:950]

    def ProcessamentoImagen(img):
        
        img = cv2.medianBlur(img,5)
    	ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    
    	nucleo = np.ones((5,5),np.uint16) 
        linhaFiltrada = cv2.morphologyEx(th1,cv2.MORPH_OPEN,nucleo, iterations = 3)
        linhaFiltrada = cv2.dilate(linhaFiltrada,nucleo,iterations = 3)
        
        ret,linhaFiltrada = cv2.threshold(linhaFiltrada,127,255,cv2.THRESH_BINARY_INV)
        
        detector_params = cv2.SimpleBlobDetector_Params()

        detector_params.filterByInertia = True
        detector_params.minInertiaRatio = 0.15
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(detector_params)
        else :
            detector = cv2.SimpleBlobDetector_create(detector_params)

        global keypoints
        keypoints = detector.detect(linhaFiltrada)
        
        im_with_keypoints = cv2.drawKeypoints(linhaFiltrada, keypoints, np.array([]), 
        (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  
        return im_with_keypoints

    @staticmethod
    def getRespostaGabarito(img):
        questoes= 20
        prova={}
        ProcessamentoImagen(img)

        for p in keypoints:
            if p.pt[0] > 10 and p.pt[0] < 80:
                # print(questoes,"-A",p.pt)
                prova[questoes]='A'
                questoes = (questoes-1)
            elif p.pt[0] > 86 and p.pt[0] < 152:
                # print(questoes,"-B",p.pt)
                prova[questoes]='B'
                questoes = (questoes-1)
            elif p.pt[0] > 160 and p.pt[0] < 230:
                prova[questoes]='C'
                questoes = (questoes-1)
            elif p.pt[0] > 240 and p.pt[0] < 307:
                prova[questoes]='D'
                questoes = (questoes-1)
            elif p.pt[0] > 315 and p.pt[0] < 380:
                # print(questoes,"-E-",p.pt)
                prova[questoes]='E'
                questoes = (questoes-1)
        return prova

    @staticmethod
    def getInscricao(img):
        inscricao=''
        ProcessamentoImagen(img)

        for p in keypoints:
            if p.pt[0] > 7 and p.pt[0] < 75:
                inscricao=inscricao+'0'
            elif p.pt[0] > 76 and p.pt[0] < 155:
                inscricao=inscricao+'1'
            elif p.pt[0] > 160 and p.pt[0] < 238:
                inscricao=inscricao+'2'
            elif p.pt[0] > 239 and p.pt[0] < 290:
                inscricao=inscricao+'3'
            elif p.pt[0] > 300 and p.pt[0] < 370:
                inscricao= inscricao+'4'
            elif p.pt[0] > 380 and p.pt[0] < 450:
                inscricao=inscricao+'5'
            elif p.pt[0] > 455 and p.pt[0] < 530:
                inscricao=inscricao+'6'
            elif p.pt[0] > 532 and p.pt[0] < 600:
                inscricao=inscricao+'7'
            elif p.pt[0] > 605 and p.pt[0] < 680:
                inscricao=inscricao+'8'
            elif p.pt[0] > 685 and p.pt[0] < 850:
                inscricao=inscricao+'9'
        return inscricao[::-1].zfill(6)
    @staticmethod
    def getRespostaQestionario(img):
        questionario={}
        questoesQuestionario=9
        ProcessamentoImagen(img)
        for p in keypoints:
            if p.pt[0] > 20 and p.pt[0] < 85:
                # print(questoes,"-A",p.pt)
                questionario[questoesQuestionario]='A'
                questoesQuestionario = (questoesQuestionario-1)
            elif p.pt[0] > 86 and p.pt[0] < 160:
                # print(questoes,"-B",p.pt)
                questionario[questoesQuestionario]='B'
                questoesQuestionario = (questoesQuestionario-1)
            elif p.pt[0] > 161 and p.pt[0] < 238:
                questionario[questoesQuestionario]='C'
                questoesQuestionario = (questoesQuestionario-1)
            elif p.pt[0] > 239 and p.pt[0] < 307:
                questionario[questoesQuestionario]='D'
                questoesQuestionario = (questoesQuestionario-1)
            elif p.pt[0] > 308 or p.pt[1] < 380:
                # print(questoes,"-E-",p.pt)
                questionario[questoesQuestionario]='E'
                questoesQuestionario = (questoesQuestionario-1)
        return questionario
