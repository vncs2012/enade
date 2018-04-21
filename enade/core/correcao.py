#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np

class correcao():
    global ProcessamentoImagen

    @staticmethod
    def getCorteRespostaGabarito(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[1400:2615, 95:490]

    @staticmethod
    def getCorteCodigoAluno(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[880:1339,175:975]

    @staticmethod
    def getCorteQuestionario(imge):
        img =cv2.imread(imge, cv2.IMREAD_GRAYSCALE)
        return img[1400:1945,550:950]

    def ProcessamentoImagen(img):
        img = cv2.medianBlur(img,5)
        ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        nucleo = np.ones((5,5), np.uint16)
        linhaFiltrada = cv2.dilate(th1,nucleo,iterations = 5)
        linhaFiltrada = cv2.erode(linhaFiltrada,nucleo,iterations = 5)

        detector_params = cv2.SimpleBlobDetector_Params()
        # Filter by Inertia
        detector_params.filterByInertia= True
        detector_params.minInertiaRatio= 0.15
        # Create a detector with the parameters
        ver = (cv2.__version__).split('.')
        if int(ver[0]) < 3 :
            detector = cv2.SimpleBlobDetector(detector_params)
        else :
            detector = cv2.SimpleBlobDetector_create(detector_params)
        # detector = cv2.SimpleBlobDetector(detector_params)
        global keypoints
        keypoints = detector.detect(linhaFiltrada)
        im_with_keypoints = cv2.drawKeypoints(linhaFiltrada,keypoints,np.array([]),(125,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        return im_with_keypoints

    @staticmethod
    def getRespostaGabarito(img):
        questoes= 20
        prova={}
        ProcessamentoImagen(img)
    
        for p in keypoints:
            if p.pt[0] > 22 and p.pt[0] < 80:
                # print(questoes,"-A",p.pt)
                prova[questoes]='A'
                questoes = (questoes-1)
            elif p.pt[0] > 100 and p.pt[0] < 160:
                # print(questoes,"-B",p.pt)
                prova[questoes]='B'
                questoes = (questoes-1)
            elif p.pt[0] > 172 and p.pt[0] < 238:
                prova[questoes]='C'
                questoes = (questoes-1)
            elif p.pt[0] > 247 and p.pt[0] < 307:
                prova[questoes]='D'
                questoes = (questoes-1)
            elif p.pt[0] > 319 and p.pt[0] < 380:
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
        return inscricao[::-1]
    
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
