# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.selecteur_box = QtWidgets.QWidget()
        self.selecteur_box.setObjectName("selecteur_box")
        self.layoutWidget = QtWidgets.QWidget(self.selecteur_box)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 150, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.techno_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_1.setObjectName("techno_1")
        self.verticalLayout_2.addWidget(self.techno_1)
        self.techno_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_2.setObjectName("techno_2")
        self.verticalLayout_2.addWidget(self.techno_2)
        self.techno_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_3.setObjectName("techno_3")
        self.verticalLayout_2.addWidget(self.techno_3)
        self.techno_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_4.setObjectName("techno_4")
        self.verticalLayout_2.addWidget(self.techno_4)
        self.techno_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_5.setObjectName("techno_5")
        self.verticalLayout_2.addWidget(self.techno_5)
        self.techno_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_6.setObjectName("techno_6")
        self.verticalLayout_2.addWidget(self.techno_6)
        self.techno_7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_7.setObjectName("techno_7")
        self.verticalLayout_2.addWidget(self.techno_7)
        self.techno_8 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_8.setEnabled(True)
        self.techno_8.setObjectName("techno_8")
        self.verticalLayout_2.addWidget(self.techno_8)
        self.techno_9 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_9.setEnabled(True)
        self.techno_9.setObjectName("techno_9")
        self.verticalLayout_2.addWidget(self.techno_9)
        self.techno_10 = QtWidgets.QRadioButton(self.layoutWidget)
        self.techno_10.setEnabled(True)
        self.techno_10.setObjectName("techno_10")
        self.verticalLayout_2.addWidget(self.techno_10)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_2.addWidget(self.radioButton_2)
        self.tabWidget.addTab(self.selecteur_box, "")
        self.telecommande_box = QtWidgets.QWidget()
        self.telecommande_box.setObjectName("telecommande_box")
        self.box_haut = QtWidgets.QPushButton(self.telecommande_box)
        self.box_haut.setEnabled(True)
        self.box_haut.setGeometry(QtCore.QRect(80, 40, 41, 23))
        self.box_haut.setObjectName("box_haut")
        self.box_v_plus = QtWidgets.QPushButton(self.telecommande_box)
        self.box_v_plus.setEnabled(True)
        self.box_v_plus.setGeometry(QtCore.QRect(30, 160, 41, 23))
        self.box_v_plus.setObjectName("box_v_plus")
        self.box_9 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_9.setGeometry(QtCore.QRect(130, 290, 41, 23))
        self.box_9.setObjectName("box_9")
        self.box_v_moins = QtWidgets.QPushButton(self.telecommande_box)
        self.box_v_moins.setGeometry(QtCore.QRect(30, 190, 41, 23))
        self.box_v_moins.setObjectName("box_v_moins")
        self.box_droite = QtWidgets.QPushButton(self.telecommande_box)
        self.box_droite.setGeometry(QtCore.QRect(130, 70, 51, 23))
        self.box_droite.setObjectName("box_droite")
        self.box_bas = QtWidgets.QPushButton(self.telecommande_box)
        self.box_bas.setGeometry(QtCore.QRect(80, 100, 41, 23))
        self.box_bas.setObjectName("box_bas")
        self.box_menu = QtWidgets.QPushButton(self.telecommande_box)
        self.box_menu.setGeometry(QtCore.QRect(130, 130, 51, 23))
        self.box_menu.setObjectName("box_menu")
        self.box_4 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_4.setGeometry(QtCore.QRect(30, 260, 41, 23))
        self.box_4.setObjectName("box_4")
        self.box_3 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_3.setEnabled(True)
        self.box_3.setGeometry(QtCore.QRect(130, 230, 41, 23))
        self.box_3.setObjectName("box_3")
        self.box_2 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_2.setEnabled(True)
        self.box_2.setGeometry(QtCore.QRect(80, 230, 41, 23))
        self.box_2.setObjectName("box_2")
        self.box_on_off = QtWidgets.QPushButton(self.telecommande_box)
        self.box_on_off.setEnabled(True)
        self.box_on_off.setGeometry(QtCore.QRect(130, 10, 51, 23))
        self.box_on_off.setObjectName("box_on_off")
        self.box_1 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_1.setEnabled(True)
        self.box_1.setGeometry(QtCore.QRect(30, 230, 41, 23))
        self.box_1.setObjectName("box_1")
        self.box_5 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_5.setGeometry(QtCore.QRect(80, 260, 41, 23))
        self.box_5.setObjectName("box_5")
        self.box_6 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_6.setGeometry(QtCore.QRect(130, 260, 41, 23))
        self.box_6.setObjectName("box_6")
        self.box_0 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_0.setGeometry(QtCore.QRect(80, 320, 41, 23))
        self.box_0.setObjectName("box_0")
        self.box_7 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_7.setGeometry(QtCore.QRect(30, 290, 41, 23))
        self.box_7.setObjectName("box_7")
        self.box_ok = QtWidgets.QPushButton(self.telecommande_box)
        self.box_ok.setGeometry(QtCore.QRect(80, 70, 41, 23))
        self.box_ok.setObjectName("box_ok")
        self.box_gauche = QtWidgets.QPushButton(self.telecommande_box)
        self.box_gauche.setGeometry(QtCore.QRect(20, 70, 51, 23))
        self.box_gauche.setObjectName("box_gauche")
        self.box_retour = QtWidgets.QPushButton(self.telecommande_box)
        self.box_retour.setGeometry(QtCore.QRect(20, 130, 51, 23))
        self.box_retour.setObjectName("box_retour")
        self.box_8 = QtWidgets.QPushButton(self.telecommande_box)
        self.box_8.setGeometry(QtCore.QRect(80, 290, 41, 23))
        self.box_8.setObjectName("box_8")
        self.box_p_plus = QtWidgets.QPushButton(self.telecommande_box)
        self.box_p_plus.setEnabled(True)
        self.box_p_plus.setGeometry(QtCore.QRect(130, 160, 41, 23))
        self.box_p_plus.setObjectName("box_p_plus")
        self.box_p_moins = QtWidgets.QPushButton(self.telecommande_box)
        self.box_p_moins.setEnabled(True)
        self.box_p_moins.setGeometry(QtCore.QRect(130, 190, 41, 23))
        self.box_p_moins.setObjectName("box_p_moins")
        self.box_tv = QtWidgets.QPushButton(self.telecommande_box)
        self.box_tv.setGeometry(QtCore.QRect(30, 10, 41, 23))
        self.box_tv.setObjectName("box_tv")
        self.box_reset_electrique = QtWidgets.QPushButton(self.telecommande_box)
        self.box_reset_electrique.setGeometry(QtCore.QRect(0, 360, 91, 23))
        self.box_reset_electrique.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 85, 0);")
        self.box_reset_electrique.setObjectName("box_reset_electrique")
        self.box_code_adulte = QtWidgets.QPushButton(self.telecommande_box)
        self.box_code_adulte.setGeometry(QtCore.QRect(130, 360, 71, 23))
        self.box_code_adulte.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 85, 0);")
        self.box_code_adulte.setObjectName("box_code_adulte")
        self.tabWidget.addTab(self.telecommande_box, "")
        self.telecommande_tv = QtWidgets.QWidget()
        self.telecommande_tv.setObjectName("telecommande_tv")
        self.tv_5 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_5.setGeometry(QtCore.QRect(80, 260, 41, 23))
        self.tv_5.setObjectName("tv_5")
        self.tv_1 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_1.setEnabled(True)
        self.tv_1.setGeometry(QtCore.QRect(30, 230, 41, 23))
        self.tv_1.setObjectName("tv_1")
        self.tv_ok = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_ok.setGeometry(QtCore.QRect(80, 70, 41, 23))
        self.tv_ok.setObjectName("tv_ok")
        self.tv_3 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_3.setEnabled(True)
        self.tv_3.setGeometry(QtCore.QRect(130, 230, 41, 23))
        self.tv_3.setObjectName("tv_3")
        self.tv_2 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_2.setEnabled(True)
        self.tv_2.setGeometry(QtCore.QRect(80, 230, 41, 23))
        self.tv_2.setObjectName("tv_2")
        self.tv_p_plus = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_p_plus.setEnabled(True)
        self.tv_p_plus.setGeometry(QtCore.QRect(130, 160, 41, 23))
        self.tv_p_plus.setObjectName("tv_p_plus")
        self.tv_0 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_0.setGeometry(QtCore.QRect(80, 320, 41, 23))
        self.tv_0.setObjectName("tv_0")
        self.tv_retour = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_retour.setGeometry(QtCore.QRect(20, 130, 51, 23))
        self.tv_retour.setObjectName("tv_retour")
        self.tv_8 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_8.setGeometry(QtCore.QRect(80, 290, 41, 23))
        self.tv_8.setObjectName("tv_8")
        self.tv_v_plus = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_v_plus.setEnabled(True)
        self.tv_v_plus.setGeometry(QtCore.QRect(30, 160, 41, 23))
        self.tv_v_plus.setObjectName("tv_v_plus")
        self.tv_bas = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_bas.setGeometry(QtCore.QRect(80, 100, 41, 23))
        self.tv_bas.setObjectName("tv_bas")
        self.tv_gauche = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_gauche.setGeometry(QtCore.QRect(20, 70, 51, 23))
        self.tv_gauche.setObjectName("tv_gauche")
        self.tv_v_moins = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_v_moins.setGeometry(QtCore.QRect(30, 190, 41, 23))
        self.tv_v_moins.setObjectName("tv_v_moins")
        self.tv_7 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_7.setGeometry(QtCore.QRect(30, 290, 41, 23))
        self.tv_7.setObjectName("tv_7")
        self.tv_on_off = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_on_off.setEnabled(True)
        self.tv_on_off.setGeometry(QtCore.QRect(20, 10, 51, 23))
        self.tv_on_off.setObjectName("tv_on_off")
        self.tv_menu = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_menu.setGeometry(QtCore.QRect(130, 130, 51, 23))
        self.tv_menu.setObjectName("tv_menu")
        self.tv_6 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_6.setGeometry(QtCore.QRect(130, 260, 41, 23))
        self.tv_6.setObjectName("tv_6")
        self.tv_9 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_9.setGeometry(QtCore.QRect(130, 290, 41, 23))
        self.tv_9.setObjectName("tv_9")
        self.tv_droite = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_droite.setGeometry(QtCore.QRect(130, 70, 51, 23))
        self.tv_droite.setObjectName("tv_droite")
        self.tv_source = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_source.setGeometry(QtCore.QRect(130, 10, 51, 23))
        self.tv_source.setObjectName("tv_source")
        self.tv_4 = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_4.setGeometry(QtCore.QRect(30, 260, 41, 23))
        self.tv_4.setObjectName("tv_4")
        self.tv_haut = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_haut.setEnabled(True)
        self.tv_haut.setGeometry(QtCore.QRect(80, 40, 41, 23))
        self.tv_haut.setObjectName("tv_haut")
        self.tv_p_moins = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_p_moins.setEnabled(True)
        self.tv_p_moins.setGeometry(QtCore.QRect(130, 190, 41, 23))
        self.tv_p_moins.setObjectName("tv_p_moins")
        self.tv_log = QtWidgets.QPushButton(self.telecommande_tv)
        self.tv_log.setGeometry(QtCore.QRect(30, 330, 41, 23))
        self.tv_log.setObjectName("tv_log")
        self.tabWidget.addTab(self.telecommande_tv, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.box_on_off, self.box_haut)
        MainWindow.setTabOrder(self.box_haut, self.box_gauche)
        MainWindow.setTabOrder(self.box_gauche, self.box_ok)
        MainWindow.setTabOrder(self.box_ok, self.box_droite)
        MainWindow.setTabOrder(self.box_droite, self.box_bas)
        MainWindow.setTabOrder(self.box_bas, self.box_retour)
        MainWindow.setTabOrder(self.box_retour, self.box_menu)
        MainWindow.setTabOrder(self.box_menu, self.box_v_plus)
        MainWindow.setTabOrder(self.box_v_plus, self.box_p_plus)
        MainWindow.setTabOrder(self.box_p_plus, self.box_v_moins)
        MainWindow.setTabOrder(self.box_v_moins, self.box_p_moins)
        MainWindow.setTabOrder(self.box_p_moins, self.box_1)
        MainWindow.setTabOrder(self.box_1, self.box_2)
        MainWindow.setTabOrder(self.box_2, self.box_3)
        MainWindow.setTabOrder(self.box_3, self.box_4)
        MainWindow.setTabOrder(self.box_4, self.box_5)
        MainWindow.setTabOrder(self.box_5, self.box_6)
        MainWindow.setTabOrder(self.box_6, self.box_7)
        MainWindow.setTabOrder(self.box_7, self.box_8)
        MainWindow.setTabOrder(self.box_8, self.box_9)
        MainWindow.setTabOrder(self.box_9, self.box_0)
        MainWindow.setTabOrder(self.box_0, self.techno_2)
        MainWindow.setTabOrder(self.techno_2, self.techno_4)
        MainWindow.setTabOrder(self.techno_4, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.techno_5)
        MainWindow.setTabOrder(self.techno_5, self.techno_6)
        MainWindow.setTabOrder(self.techno_6, self.techno_7)
        MainWindow.setTabOrder(self.techno_7, self.techno_8)
        MainWindow.setTabOrder(self.techno_8, self.techno_1)
        MainWindow.setTabOrder(self.techno_1, self.techno_3)
        MainWindow.setTabOrder(self.techno_3, self.techno_9)
        MainWindow.setTabOrder(self.techno_9, self.box_tv)
        MainWindow.setTabOrder(self.box_tv, self.box_reset_electrique)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.techno_1.setText(_translate("MainWindow", "1 - Cable"))
        self.techno_2.setText(_translate("MainWindow", "2 - RTI90 - SD FEC / HD"))
        self.techno_3.setText(_translate("MainWindow", "3 - DBI8500E SD / HD /C+"))
        self.techno_4.setText(_translate("MainWindow", "4 - Fibre"))
        self.techno_5.setText(_translate("MainWindow", "5 - RTI422 Sensation"))
        self.techno_6.setText(_translate("MainWindow", "6 - Miami MultiCast"))
        self.techno_7.setText(_translate("MainWindow", "7 - Miami OTT"))
        self.techno_8.setText(_translate("MainWindow", "8 - ADSL GCF"))
        self.techno_9.setText(_translate("MainWindow", "9 - Box 4K"))
        self.techno_10.setText(_translate("MainWindow", "10 - réserve"))
        self.radioButton.setText(_translate("MainWindow", "11 - réserve"))
        self.radioButton_2.setText(_translate("MainWindow", "12 - réserve"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selecteur_box), _translate("MainWindow", "Sélecteur box"))
        self.box_haut.setText(_translate("MainWindow", "Haut"))
        self.box_v_plus.setText(_translate("MainWindow", "V+"))
        self.box_9.setText(_translate("MainWindow", "9"))
        self.box_v_moins.setText(_translate("MainWindow", "V-"))
        self.box_droite.setText(_translate("MainWindow", "Droite"))
        self.box_bas.setText(_translate("MainWindow", "Bas"))
        self.box_menu.setText(_translate("MainWindow", "Menu"))
        self.box_4.setText(_translate("MainWindow", "4"))
        self.box_3.setText(_translate("MainWindow", "3"))
        self.box_2.setText(_translate("MainWindow", "2"))
        self.box_on_off.setText(_translate("MainWindow", "On/Off"))
        self.box_1.setText(_translate("MainWindow", "1"))
        self.box_5.setText(_translate("MainWindow", "5"))
        self.box_6.setText(_translate("MainWindow", "6"))
        self.box_0.setText(_translate("MainWindow", "0"))
        self.box_7.setText(_translate("MainWindow", "7"))
        self.box_ok.setText(_translate("MainWindow", "OK"))
        self.box_gauche.setText(_translate("MainWindow", "Gauche"))
        self.box_retour.setText(_translate("MainWindow", "Retour"))
        self.box_8.setText(_translate("MainWindow", "8"))
        self.box_p_plus.setText(_translate("MainWindow", "P+"))
        self.box_p_moins.setText(_translate("MainWindow", "P-"))
        self.box_tv.setText(_translate("MainWindow", "TV"))
        self.box_reset_electrique.setText(_translate("MainWindow", "Reset électrique"))
        self.box_code_adulte.setText(_translate("MainWindow", "Code adulte"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.telecommande_box), _translate("MainWindow", "Box"))
        self.tv_5.setText(_translate("MainWindow", "5"))
        self.tv_1.setText(_translate("MainWindow", "1"))
        self.tv_ok.setText(_translate("MainWindow", "OK"))
        self.tv_3.setText(_translate("MainWindow", "3"))
        self.tv_2.setText(_translate("MainWindow", "2"))
        self.tv_p_plus.setText(_translate("MainWindow", "P+"))
        self.tv_0.setText(_translate("MainWindow", "0"))
        self.tv_retour.setText(_translate("MainWindow", "Retour"))
        self.tv_8.setText(_translate("MainWindow", "8"))
        self.tv_v_plus.setText(_translate("MainWindow", "V+"))
        self.tv_bas.setText(_translate("MainWindow", "Bas"))
        self.tv_gauche.setText(_translate("MainWindow", "Gauche"))
        self.tv_v_moins.setText(_translate("MainWindow", "V-"))
        self.tv_7.setText(_translate("MainWindow", "7"))
        self.tv_on_off.setText(_translate("MainWindow", "On/Off"))
        self.tv_menu.setText(_translate("MainWindow", "Menu"))
        self.tv_6.setText(_translate("MainWindow", "6"))
        self.tv_9.setText(_translate("MainWindow", "9"))
        self.tv_droite.setText(_translate("MainWindow", "Droite"))
        self.tv_source.setText(_translate("MainWindow", "Source"))
        self.tv_4.setText(_translate("MainWindow", "4"))
        self.tv_haut.setText(_translate("MainWindow", "Haut"))
        self.tv_p_moins.setText(_translate("MainWindow", "P-"))
        self.tv_log.setText(_translate("MainWindow", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.telecommande_tv), _translate("MainWindow", "TV"))

