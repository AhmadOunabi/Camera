from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
from PyQt5.uic import loadUiType
import urllib.request 
import os
from os import path


ui,_ = loadUiType(path.join(path.dirname(__file__),'main.ui'))


class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_buttons()
        #self.cam=cv2.VideoCapture(0)
        self.img_counter=0
    
    
    def Handel_buttons(self):
        self.pushButton.clicked.connect(self.open_camera)
        self.pushButton_2.clicked.connect(self.close_camera)
        self.pushButton_3.clicked.connect(self.take_pic)
    def open_camera(self):
        self.cam=cv2.VideoCapture(0)
        cv2.namedWindow('Kamera')
        while True:
            ret, self.frame=self.cam.read()
            cv2.imshow('Kamera',self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cam.release()
        cv2.destroyAllWindows()
    def close_camera(self):
            while True:
                cv2.destroyWindow(self.frame)
    
    def take_pic(self):
        img_name = "opencv_frame_{}.png".format(self.img_counter)
        cv2.imwrite(img_name,self.frame)
        self.img_counter+=1
        
    img_counter=img_counter
    print(img_counter)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()