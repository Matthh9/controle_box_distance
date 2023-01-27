# -*- coding: utf-8 -*-
#
# programme python du projet de controle a distance des moyens de tests fixes du cokcpit BYTEL par une connexion à un arduino
# auteur : DA SILVA Matthieu
# date : 2020-2021


PORTTV = "port19"
SWITCH1 = "port16"
SWITCH2 = "port17"
#port A4 = 18 et A5 = 19


from PyQt5 import QtWidgets, uic  #QtCore, QtGui, QtWidgets, uic
import sys
import time

# import interface as ihm
from functools import partial

import pygame.camera
import pygame.image

import pyaudio

from threading import Thread

import serial
import serial.tools.list_ports

#utile pour la mise exe du programme, sans ça le prgramme bug sur les pc de l'entreprise
from multiprocessing import Queue
import cffi

import pyautogui
pyautogui.PAUSE = 0
import pygame.mixer
from datetime import datetime, timedelta


port=""
debit=9600
serialPort=None

global fermeture
fermeture = False

global derniereCommande
derniereCommande = datetime.now()

global app



class ExampleApp(QtWidgets.QMainWindow):
    global fermeture
    global derniereCommande
    boxChoisi=""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("interface.ui", self)
        # self.setupUi(self)


        #si on change d'onglet on appelle la fonction changementOnglet pour savoir si on doit passer sur le led TV ou le système de commande de box
        self.tabWidget.currentChanged.connect(self.changementOnglet)
        

        #programmation des interrections avec la télécommande des box
        self.box_tv.clicked.connect(partial(self.envoiMessagePortCom,"16D62CD3"))
        self.box_on_off.clicked.connect(partial(self.envoiMessagePortCom,"16D648B7"))

        self.box_haut.clicked.connect(partial(self.envoiMessagePortCom,"16D6D02F"))
        self.box_gauche.clicked.connect(partial(self.envoiMessagePortCom,"16D6D827"))
        self.box_ok.clicked.connect(partial(self.envoiMessagePortCom,"16D6A857"))
        self.box_droite.clicked.connect(partial(self.envoiMessagePortCom,"16D638C7"))
        self.box_bas.clicked.connect(partial(self.envoiMessagePortCom,"16D630CF"))

        self.box_retour.clicked.connect(partial(self.envoiMessagePortCom,"16D650AF"))
        self.box_menu.clicked.connect(partial(self.envoiMessagePortCom,"16D628D7"))
        self.box_v_plus.clicked.connect(partial(self.envoiMessagePortCom,"16D6B04F"))
        self.box_p_plus.clicked.connect(partial(self.envoiMessagePortCom,"16D608F7"))
        self.box_p_moins.clicked.connect(partial(self.envoiMessagePortCom,"16D658A7"))
        self.box_v_moins.clicked.connect(partial(self.envoiMessagePortCom,"16D6708F"))

        self.box_1.clicked.connect(partial(self.envoiMessagePortCom,"16D6807F"))
        self.box_2.clicked.connect(partial(self.envoiMessagePortCom,"16D640BF"))
        self.box_3.clicked.connect(partial(self.envoiMessagePortCom,"16D6C03F"))
        self.box_4.clicked.connect(partial(self.envoiMessagePortCom,"16D620DF"))
        self.box_5.clicked.connect(partial(self.envoiMessagePortCom,"16D6A05F"))
        self.box_6.clicked.connect(partial(self.envoiMessagePortCom,"16D6609F"))
        self.box_7.clicked.connect(partial(self.envoiMessagePortCom,"16D6E01F"))
        self.box_8.clicked.connect(partial(self.envoiMessagePortCom,"16D610EF"))
        self.box_9.clicked.connect(partial(self.envoiMessagePortCom,"16D6906F"))
        self.box_0.clicked.connect(partial(self.envoiMessagePortCom,"16D600FF"))

        self.box_reset_electrique.clicked.connect(partial(self.envoiMessagePortCom,"reset_electrique"))
        self.box_code_adulte.clicked.connect(partial(self.envoiMessagePortCom,"16D6807F;16D640BF;16D6C03F;16D620DF;"))
        # self.box_code_adulte.clicked.connect(partial(self.envoiMultiMessagePortCom,"16D6807F","16D640BF","16D6C03F","16D620DF"))



        #progammation des interractions avec la partie sélecteur box
        ## On envoie plusieurs fois le code du port au switch car il n'est pas très sensible
        self.techno_1.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FF20DF","port4"))
        self.techno_2.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FFA05F","port5"))
        self.techno_3.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FF609F","port6"))
        self.techno_4.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FF7887","port7"))
        self.techno_5.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FFE01F","port8"))
        self.techno_6.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FF10EF","port9"))
        self.techno_7.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FF906F","port10"))
        self.techno_8.clicked.connect(partial(self.envoiMultiMessagePortCom,SWITCH1,"salve;8;FFD827","port11"))
        self.techno_9.clicked.connect(partial(self.envoiMessagePortCom,"port2")) #pour la box 4K pas besoin de changement de port du switch HDMI


        #programmation des interrections avec la télécommande TV
        self.tv_on_off.clicked.connect(partial(self.envoiMessagePortCom,"E0E06798"))
        self.tv_source.clicked.connect(partial(self.envoiMessagePortCom,"E0E0807F"))
        self.tv_haut.clicked.connect(partial(self.envoiMessagePortCom,"E0E006F9"))
        self.tv_gauche.clicked.connect(partial(self.envoiMessagePortCom,"E0E0A659"))
        self.tv_ok.clicked.connect(partial(self.envoiMessagePortCom,"E0E016E9"))
        self.tv_droite.clicked.connect(partial(self.envoiMessagePortCom,"E0E046B9"))
        self.tv_bas.clicked.connect(partial(self.envoiMessagePortCom,"E0E08679"))

        self.tv_retour.clicked.connect(partial(self.envoiMessagePortCom,"E0E01AE5"))
        self.tv_menu.clicked.connect(partial(self.envoiMessagePortCom,"E0E09E61"))
        self.tv_v_plus.clicked.connect(partial(self.envoiMessagePortCom,"E0E0E01F"))
        self.tv_p_plus.clicked.connect(partial(self.envoiMessagePortCom,"E0E048B7"))
        self.tv_v_moins.clicked.connect(partial(self.envoiMessagePortCom,"E0E0D02F"))
        self.tv_p_moins.clicked.connect(partial(self.envoiMessagePortCom,"E0E008F7"))

        self.tv_1.clicked.connect(partial(self.envoiMessagePortCom,"E0E020DF"))
        self.tv_2.clicked.connect(partial(self.envoiMessagePortCom,"E0E0A05F"))
        self.tv_3.clicked.connect(partial(self.envoiMessagePortCom,"E0E0609F"))
        self.tv_4.clicked.connect(partial(self.envoiMessagePortCom,"E0E010EF"))
        self.tv_5.clicked.connect(partial(self.envoiMessagePortCom,"E0E0906F"))
        self.tv_6.clicked.connect(partial(self.envoiMessagePortCom,"E0E050AF"))
        self.tv_7.clicked.connect(partial(self.envoiMessagePortCom,"E0E030CF"))
        self.tv_8.clicked.connect(partial(self.envoiMessagePortCom,"E0E0B04F"))
        self.tv_9.clicked.connect(partial(self.envoiMessagePortCom,"E0E0708F"))
        self.tv_0.clicked.connect(partial(self.envoiMessagePortCom,"E0E08877"))
        self.tv_log.clicked.connect(partial(self.envoiMessagePortCom,"E0E034CB"))
        self.tv_reset_electrique.clicked.connect(partial(self.envoiMessagePortCom,"reset_electrique"))

        self.envoyer_commande.clicked.connect(self.envoie_commande_manuelle)

    def changementOnglet(self):
        index=self.tabWidget.currentIndex()
        if(index==2):
            self.envoiMessagePortCom(PORTTV)
        else:
            self.envoiMessagePortCom(self.boxChoisi)
        

    def envoiMultiMessagePortCom(self, *messages):
        for message in messages:
            if message!=True and message!=False: # le dernier élement du tuple est true
                if "port" in message:
                    self.boxChoisi=message

                self.envoiMessagePortCom(message)
                time.sleep(0.300)


    def envoiMessagePortCom(self,chaine):
        global derniereCommande
        # print(chaine)
        serialPort.write(str.encode(chaine))
        derniereCommande = datetime.now()

    def envoie_commande_manuelle(self):
        self.envoiMessagePortCom(self.commande_manuelle.text())
        self.commande_manuelle.clear()
        # print("commande manuelle")
        # print(chaine)
        # print(self.commande_manuelle.text())
        

def recherchePortCom():
    comlist = serial.tools.list_ports.comports()
    for element in comlist:
        if ("Arduino" in element.description or "Périphérique série USB (COM" in element.description):
            return element.device
    return ""





class main(Thread):
    global app

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global fermeture
        global app

        app = QtWidgets.QApplication(sys.argv)
        global serialPort
        port=recherchePortCom()
        print(port)
        if (port==""):
            fermeture=True
            print("Arduino introuvable, vérifier le bon fonctionnement physique du microcontroleur")
        else:
            try:
                serialPort=serial.Serial(port,debit)
                form = ExampleApp()
                form.show()
                app.exec_()
                
                fermeture=True
                serialPort.write(str.encode("Fin"))
                serialPort.close() #On ferme proprement le port com mais il se libère au bout de quelque seconde si le programme est fermé
            except (OSError, serial.SerialException):
                fermeture=True
                print("portCom non libre, merci de re essayer dans quelques instants, si le problème persiste, deconnecter tous les utilisateurs ou redémmarer la machine")


class video(Thread):
    global fermeture

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global fermeture
        global app
        
        pygame.camera.init()

        cameras = pygame.camera.list_cameras()
        
        print ("Using camera %s ..." % cameras[0])
        
        webcam = pygame.camera.Camera(cameras[0])
        
        webcam.start()
        
        # grab first frame
        img = webcam.get_image()
        
        WIDTH = img.get_width()
        HEIGHT = img.get_height()
        
        
        screen = pygame.display.set_mode( ( WIDTH, HEIGHT ) )
        pygame.display.set_caption("pyGame Camera View")
        
        while True :
            for e in pygame.event.get() :
                if e.type == pygame.QUIT :
                    running= False
                    fermeture=True
                    print("fin")
                    webcam.stop()
                    pygame.camera.quit()
                    pygame.quit()
                    sys.exit()
                    
                if fermeture == True :
                    app.exit()
                    running= False
                    print("fin")
                    webcam.stop()
                    pygame.camera.quit()
                    pygame.quit()
                    sys.exit()
        
            # draw frame
            screen.blit(img, (0,0))
            pygame.display.flip()
            # grab next frame    
            img = webcam.get_image()
    


class son(Thread):
    global fermeture

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global fermeture

        FORMAT = pyaudio.paInt16
        CHUNK = 1024
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        p2 = pyaudio.PyAudio()
        stream_lecture = p2.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True)

        while(True):
            data = stream.read(CHUNK)#peut-être un nombre d'octets par frame
            stream_lecture.write(data)
            if fermeture==True :
                break

        stream.stop_stream()
        stream.close()
        p.terminate()

        stream_lecture.stop_stream()
        stream_lecture.close()

        p2.terminate()
        
        

class timer(Thread):
    global fermeture
    global derniereCommande
    global app

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global fermeture
        global derniereCommande

        while(not(fermeture)):
            time.sleep(5)
            
            derniereCommande15min = derniereCommande + timedelta(minutes=15)
            if(derniereCommande15min<datetime.now()):
                print("Fermeture automatique")
                fermeture=True
                app.quit()

            

### joue un son au début du logiciel
#fonction montant le son 
for i in range(50):
    pyautogui.press('volumeup')

pygame.mixer.init()
pygame.mixer.music.load('démarrage_controle_distance.mp3') #mp3 aussi
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue



# Création des threads
global thread_1
thread_1 = main()
thread_2 = video()
thread_3 = son()
thread_4 = timer()

# Lancement des threads
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()



### joue un son de fin du logiciel
# fonction montant le son 
for i in range(50):
    pyautogui.press('volumeup')

pygame.mixer.init()
pygame.mixer.music.load('fin_controle_distance.mp3') #mp3 aussi
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue