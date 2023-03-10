# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BackgroundCutter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading

from rembg import remove
from PIL import Image
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

async def re_pbar(pbar, val):
    pbar.setValue(val)


async def bg_cut(input_path, output_path, pbar, val):
    input_img = Image.open(input_path)
    output_img = remove(input_img)
    output_img.save(output_path)
    await re_pbar(pbar=pbar, val=val)


class Ui_MainWindow():
    def setupUi(self, MainWindow):

        # Main

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 311))
        self.tabWidget.setMaximumSize(QtCore.QSize(811, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.main = QtWidgets.QWidget()
        self.main.setEnabled(True)
        self.main.setSizeIncrement(QtCore.QSize(0, 0))
        self.main.setBaseSize(QtCore.QSize(0, 0))
        self.main.setObjectName("main")
        self.main_title = QtWidgets.QLabel(self.main)
        self.main_title.setGeometry(QtCore.QRect(0, 20, 581, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.tabWidget.addTab(self.main, "")
        self.Background = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)


        # Background

        self.Background.setFont(font)
        self.Background.setObjectName("Background")


        self.pbar = QProgressBar(self.Background)
        self.pbar.setGeometry(10, 220, 121, 23)

# background_input_path_button
        self.background_input_path_button = QtWidgets.QPushButton(self.Background)
        self.background_input_path_button.setGeometry(QtCore.QRect(10, 50, 121, 23))
        self.background_input_path_button.setObjectName("background_input_path_button")
        self.background_input_path_button.clicked.connect(self.getDirectory_Bg_input_path)

# background_output_path_button
        self.background_output_path_button = QtWidgets.QPushButton(self.Background)
        self.background_output_path_button.setGeometry(QtCore.QRect(10, 80, 131, 23))
        self.background_output_path_button.setObjectName("background_output_path_button")
        self.background_output_path_button.clicked.connect(self.getDirectory_Bg_output_path)

# background_title
        self.background_title = QtWidgets.QLabel(self.Background)
        self.background_title.setGeometry(QtCore.QRect(10, 0, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.background_title.setFont(font)
        self.background_title.setObjectName("background_title")

# input_path_cheker
        self.input_path_cheker = QPlainTextEdit(self.Background)
        self.input_path_cheker.setGeometry(QtCore.QRect(150, 50, 660, 20))
        self.input_path_cheker.setObjectName("input_path_cheker")

# output_path_cheker        
        self.output_path_cheker = QPlainTextEdit(self.Background)
        self.output_path_cheker.setGeometry(QtCore.QRect(150, 80, 660, 20))
        self.output_path_cheker.setObjectName("output_path_cheker")

# background_start
        self.background_start = QtWidgets.QPushButton(self.Background)
        self.background_start.setGeometry(QtCore.QRect(660, 220, 101, 41))
        self.background_start.setObjectName("background_start")
        self.background_start.clicked.connect(self.thread2)

# background_instruction
        self.background_instruction = QtWidgets.QLabel(self.Background)
        self.background_instruction.setGeometry(QtCore.QRect(10, 130, 761, 81))

        font = QtGui.QFont()
        font.setPointSize(13)
        self.background_instruction.setFont(font)
        self.background_instruction.setObjectName("background_instruction")
        self.tabWidget.addTab(self.Background, "")


        # Size

        self.Size = QtWidgets.QWidget()
        self.Size.setObjectName("Size")
        self.size_title = QtWidgets.QLabel(self.Size)
        self.size_title.setGeometry(QtCore.QRect(10, 0, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.size_title.setFont(font)
        self.size_title.setObjectName("size_title")

# width
        self.width = QtWidgets.QSpinBox(self.Size)
        self.width.setGeometry(QtCore.QRect(10, 40, 61, 22))
        self.width.setMinimum(-100000000)
        self.width.setMaximum(100000000)
        self.width.setObjectName("width")

# height
        self.height = QtWidgets.QSpinBox(self.Size)
        self.height.setGeometry(QtCore.QRect(140, 40, 61, 22))
        self.height.setMinimum(-100000000)
        self.height.setMaximum(100000000)
        self.height.setObjectName("height")

# label_2
        self.label_2 = QtWidgets.QLabel(self.Size)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 21, 21))
        self.label_2.setObjectName("label_2")

# label_5
        self.label_5 = QtWidgets.QLabel(self.Size)
        self.label_5.setGeometry(QtCore.QRect(110, 40, 21, 21))
        self.label_5.setObjectName("label_5")

# label_6
        self.label_6 = QtWidgets.QLabel(self.Size)
        self.label_6.setGeometry(QtCore.QRect(210, 40, 16, 21))
        self.label_6.setObjectName("label_6")

# size_input_path_button
        self.size_input_path_button = QtWidgets.QPushButton(self.Size)
        self.size_input_path_button.setGeometry(QtCore.QRect(10, 70, 121, 23))
        self.size_input_path_button.setObjectName("size_input_path_button")
        self.size_input_path_button.clicked.connect(self.getDirectory_Size_input_path)

# size_output_path_button
        self.size_output_path_button = QtWidgets.QPushButton(self.Size)
        self.size_output_path_button.setGeometry(QtCore.QRect(10, 100, 131, 23))
        self.size_output_path_button.setObjectName("size_output_path_button")
        self.size_output_path_button.clicked.connect(self.getDirectory_Size_output_path)

# size_resize
        self.size_resize = QtWidgets.QPushButton(self.Size)
        self.size_resize.setGeometry(QtCore.QRect(660, 220, 101, 41))
        self.size_resize.setObjectName("size_resize")
        self.size_resize.clicked.connect(self.Size_start_button)

# size_input_path_cheker
        self.size_input_path_cheker = QPlainTextEdit(self.Size)
        self.size_input_path_cheker.setGeometry(QtCore.QRect(150, 70, 660, 20))
        self.size_input_path_cheker.setObjectName("size_input_path_cheker")

# size_output_path_cheker
        self.size_output_path_cheker = QPlainTextEdit(self.Size)
        self.size_output_path_cheker.setGeometry(QtCore.QRect(150, 100, 660, 20))
        self.size_output_path_cheker.setObjectName("size_output_path_cheker")

# size_instruction
        self.size_instruction = QtWidgets.QLabel(self.Size)
        self.size_instruction.setGeometry(QtCore.QRect(10, 130, 771, 81))


        font = QtGui.QFont()
        font.setPointSize(13)
        self.size_instruction.setFont(font)
        self.size_instruction.setObjectName("size_instruction")


        # Resolution

        self.tabWidget.addTab(self.Size, "")
        self.Resolution = QtWidgets.QWidget()
        self.Resolution.setObjectName("Resolution")
        self.resolution_title = QtWidgets.QLabel(self.Resolution)
        self.resolution_title.setGeometry(QtCore.QRect(10, 0, 771, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
# resolution_title
        self.resolution_title.setFont(font)
        self.resolution_title.setObjectName("resolution_title")

# resolution_png_to_jpg
        self.resolution_png_to_jpg = QtWidgets.QRadioButton(self.Resolution)
        self.resolution_png_to_jpg.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.resolution_png_to_jpg.setObjectName("resolution_png_to_jpg")

# resolution_jpeg_to_png
        self.resolution_jpeg_to_png = QtWidgets.QRadioButton(self.Resolution)
        self.resolution_jpeg_to_png.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.resolution_jpeg_to_png.setObjectName("resolution_jpeg_to_png")

# resolution_input_path_button
        self.resolution_input_path_button = QtWidgets.QPushButton(self.Resolution)
        self.resolution_input_path_button.setGeometry(QtCore.QRect(10, 80, 121, 23))
        self.resolution_input_path_button.setObjectName("resolution_input_path_button")
        self.resolution_input_path_button.clicked.connect(self.getDirectory_Res_input_path)

# resolution_output_path_button
        self.resolution_output_path_button = QtWidgets.QPushButton(self.Resolution)
        self.resolution_output_path_button.setGeometry(QtCore.QRect(10, 110, 131, 23))
        self.resolution_output_path_button.setObjectName("resolution_output_path_button")
        self.resolution_output_path_button.clicked.connect(self.getDirectory_Res_output_path)

# resolution_input_path_cheker
        self.resolution_input_path_cheker = QPlainTextEdit(self.Resolution)
        self.resolution_input_path_cheker.setGeometry(QtCore.QRect(150, 80, 660, 20))
        self.resolution_input_path_cheker.setObjectName("resolution_input_path_cheker")

# resolution_output_path_cheker
        self.resolution_output_path_cheker = QPlainTextEdit(self.Resolution)
        self.resolution_output_path_cheker.setGeometry(QtCore.QRect(150, 110, 660, 20))
        self.resolution_output_path_cheker.setObjectName("resolution_output_path_cheker")

# resolution_instruction
        self.resolution_instruction = QtWidgets.QLabel(self.Resolution)
        self.resolution_instruction.setGeometry(QtCore.QRect(10, 140, 800, 91))


        font = QtGui.QFont()
        font.setPointSize(13)
        self.resolution_instruction.setFont(font)
        self.resolution_instruction.setObjectName("resolution_instruction")

# resolution_start
        self.resolution_start = QtWidgets.QPushButton(self.Resolution)
        self.resolution_start.setGeometry(QtCore.QRect(660, 220, 101, 41))
        self.resolution_start.setObjectName("resolution_start")
        self.resolution_start.clicked.connect(self.Res_start_button)


        self.tabWidget.addTab(self.Resolution, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BackgroundCutter"))
        self.main_title.setText(_translate("MainWindow", "BackgroundCutter\n"
"?????????????????? ???????????????? ?? ???????? 3 ??????????????:\n"
"  ???????????????? ?????????????? ???????? ?? ????????????????????(?????????????? Background)\n"
"  ?????????????????? ?????????????? ???????????????????? ?? ????????????????(?????????????? Size)\n"
"  ?????????????????? ???????????????????? ????????????????????(?????????????? Resolution)\n"
"\n"
"?????????????????? ?????????????????????????? :)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), _translate("MainWindow", "main"))
        self.background_input_path_button.setText(_translate("MainWindow", "?????????? ?? ??????????????????????"))
        self.background_output_path_button.setText(_translate("MainWindow", "?????????? ?????? ????????????????????"))
        self.background_title.setText(_translate("MainWindow", "BackgroundCutter (???????????????? ?????????????? ???????? ?? ????????????????????)"))
        # self.input_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        # self.output_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        self.background_start.setText(_translate("MainWindow", "Start"))
        self.background_instruction.setText(_translate("MainWindow", "???????????????? ???????? ?????? ???????????????????? (?????????? ?? ???????????????????? ????????????????????????, ?? ?????????? ??????\n????????????????????), ?????????? ?????????????? ???????????? 'Start'"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Background), _translate("MainWindow", "Background"))
        self.size_title.setText(_translate("MainWindow", "BackgroundCutter (?????????????????? ??????????????)"))
        self.label_2.setText(_translate("MainWindow", "px"))
        self.label_5.setText(_translate("MainWindow", "????"))
        self.label_6.setText(_translate("MainWindow", "px"))
        self.size_input_path_button.setText(_translate("MainWindow", "?????????? ?? ??????????????????????"))
        self.size_output_path_button.setText(_translate("MainWindow", "?????????? ?????? ????????????????????"))
        self.size_resize.setText(_translate("MainWindow", "Resize"))
        # self.size_input_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        # self.size_output_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        self.size_instruction.setText(_translate("MainWindow", "?????????????? ?????????? ?? ???????????? ????????????, ?? ???????????? ???????????????????? ???? ???????????? ??????????????.\n??????????, ???????????????? ?????????? ?? ?????????????????? ????????????????????????,\n?????????? ???????????????? ?????????? ?????? ???????????????????? ?? ?????????????? ???????????? 'Resize' :)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Size), _translate("MainWindow", "Size"))
        self.resolution_title.setText(_translate("MainWindow", "BackgroundCutter (?????????????????? ????????????????????)"))
        self.resolution_png_to_jpg.setText(_translate("MainWindow", "png -> jpeg"))
        self.resolution_jpeg_to_png.setText(_translate("MainWindow", "jpeg -> png"))
        self.resolution_input_path_button.setText(_translate("MainWindow", "?????????? ?? ??????????????????????"))
        self.resolution_output_path_button.setText(_translate("MainWindow", "?????????? ?????? ????????????????????"))
        # self.resolution_input_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        # self.resolution_output_path_cheker.setText(_translate("MainWindow", "C:/Programs/python"))
        self.resolution_instruction.setText(_translate("MainWindow", "???????????????? ?????????????? ???????????????????? ????????????????????, ?????????? ?????? ???????????????????? ?? ?????????????? ???????????? 'Start' :)"))
        self.resolution_start.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Resolution), _translate("MainWindow", "Resolution"))

# init
        # init ???????????? Bg
        self.__Bg_input_path = None
        self.__Bg_output_path = None
        
        # init ???????????? Size
        self.__Size_input_path = None
        self.__Size_output_path = None
        self.__Size_weidth_size = None
        self.__Size_height_size = None

        # init ???????????? Res
        self.__Res_answer = None
        self.__Res_input_path = None
        self.__Res_output_path = None


# ??????????????

# ?????????????? ???????????? Bg
    def get_Bg_input_path(self):
        return self.__Bg_input_path

    def get_Bg_output_path(self):
        return self.__Bg_output_path

# ?????????????? ???????????? Size
    def get_Size_input_path(self):
        return self.__Size_input_path

    def get_Size_output_path(self):
        return self.__Size_output_path

    def get_Size_weidth_size(self):
        return self.__Size_weidth_size

    def get_Size_height_size(self):
        return self.__Size_height_size

# ?????????????? ???????????? Res
    def get_Res_answer(self):
        return self.__Res_answer

    def get_Res_input_path(self):
        return self.__Res_input_path

    def get_Res_output_path(self):
        return self.__Res_output_path

# ??????????????

# ?????????????? ???????????? Bg
    def set_Bg_input_path(self, arg):
        self.__Bg_input_path = arg

    def set_Bg_output_path(self, arg):
        self.__Bg_output_path = arg

# ?????????????? ???????????? Size
    def set_Size_input_path(self, arg):
        self.__Size_input_path = arg

    def set_Size_output_path(self, arg):
        self.__Size_output_path = arg

    def set_Size_weidth_size(self, arg):
        self.__Size_weidth_size = arg

    def set_Size_height_size(self, arg):
        self.__Size_height_size = arg

# ?????????????? ???????????? Res
    def set_Res_answer(self, arg):
        self.__Res_answer = arg

    def set_Res_input_path(self, arg):
        self.__Res_input_path = arg

    def set_Res_output_path(self, arg):
        self.__Res_output_path = arg


# ?????????????? ?????????? ???? ??????????

#Bg_input_path
    def getDirectory_Bg_input_path(self):                                                     # <-----
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.input_path_cheker.setPlainText(folder)
        self.set_Bg_input_path(arg=folder)

# Bg_output_path
    def getDirectory_Bg_output_path(self):                                                     # <-----
        folder1 = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.output_path_cheker.setPlainText(folder1)
        self.set_Bg_output_path(arg=folder1)

# Size_input_path
    def getDirectory_Size_input_path(self):                                                     # <-----
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.size_input_path_cheker.setPlainText(folder)
        self.set_Size_input_path(arg=folder)

# Size_output_path
    def getDirectory_Size_output_path(self):                                                     # <-----
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.size_output_path_cheker.setPlainText(folder)
        self.set_Size_output_path(arg=folder)

# Res_input_path
    def getDirectory_Res_input_path(self):                                                     # <-----
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.resolution_input_path_cheker.setPlainText(folder)
        self.set_Res_input_path(arg=folder)

# Res_output_path
    def getDirectory_Res_output_path(self):                                                     # <-----
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        self.resolution_output_path_cheker.setPlainText(folder)
        self.set_Res_output_path(arg=folder)



# BackgroundStartButton multithreading
    def thread2(self):
        t1=threading.Thread(target=self.BackgroundStartButton)
        t1.start()
        


# BackgroundStartButton

    def BackgroundStartButton(self):
        self.input_files_path = self.get_Bg_input_path()
        self.output_files_path = self.get_Bg_output_path()
        self.list_of_extensions = ["*.png", "*.jpg"]
        self.all_files = []

        self.pbar.setValue(0)

        for self.ext in self.list_of_extensions:
            self.all_files.extend(Path(f"{self.input_files_path[2:]}").glob(self.ext))
        
        # print(all_files)

        for self.index, self.item in enumerate(self.all_files):
            self.input_path = Path(self.item)
            self.file_name = self.input_path.stem

            self.output_path = f'{self.output_files_path[2:]}\{self.file_name}-output_bg.png'
            
            self.input_img = Image.open(self.input_path)
            self.output_img = remove(self.input_img) 
            self.output_img.save(self.output_path)
            
            self.number = int((self.index / len(self.all_files)) * 100)

            self.pbar.setValue(self.number)
        
        self.pbar.setValue(100)
        


    def Size_start_button(self):
        self.result_list = [self.width.value(), self.height.value()]
        self.input_files_path = self.get_Size_input_path()[2:]
        self.output_files_path = self.get_Size_output_path()[2:]

        self.list_of_extensions = ["*.png", "*.jpg"]
        self.all_files = []

        for self.ext in self.list_of_extensions:
            self.all_files.extend(Path(self.input_files_path).glob(self.ext))

        # print(all_files)
        for self.index, self.item in enumerate(self.all_files):
            
            self.input_path = Path(self.item)
            self.file_name = self.input_path.stem

            self.output_path = f'{self.output_files_path}\{self.file_name}-output_resize.png'
            
            self.input_img = Image.open(self.input_path)

            if self.input_img.mode != 'RGB':
                self.input_img = self.input_img.convert('RGB')

            self.output_img = self.input_img.resize((int(self.result_list[0]), int(self.result_list[1])))
            self.output_img.save(self.output_path)

        Message_box.show_info_messagebox()


    def Res_start_button(self):

        if self.resolution_png_to_jpg.isChecked():
            self.input_files_path = self.get_Res_input_path()[2:]
            self.output_files_path = self.get_Res_output_path()[2:]

            self.list_of_extensions = ["*.png"]
            self.all_files = []

            for self.ext in self.list_of_extensions:
                self.all_files.extend(Path(f"{self.input_files_path}").glob(self.ext))
    
            # print(all_files)

            for index, self.item in enumerate(self.all_files):
                self.input_path = Path(self.item)
                self.file_name = self.input_path.stem

                self.output_path = f'{self.output_files_path}\{self.file_name}-output_re_ex.jpg'
                
                self.input_img = Image.open(self.input_path)
                self.new_img = Image.new("RGBA", self.input_img.size, "WHITE")
                self.new_img.paste(self.input_img, (0, 0), self.input_img)
                self.new_img.convert('RGB').save(self.output_path, "JPEG")
                

        if self.resolution_jpeg_to_png.isChecked():

            self.input_files_path = self.get_Res_input_path()[2:]
            self.output_files_path = self.get_Res_output_path()[2:]

            self.list_of_extensions = ["*.jpg"]
            self.all_files = []

            for self.ext in self.list_of_extensions:
                self.all_files.extend(Path(f"{self.input_files_path}").glob(self.ext))
    
            
            for index, self.item in enumerate(self.all_files):
                self.input_path = Path(self.item)
                self.file_name = self.input_path.stem

                self.output_path = f'{self.output_files_path}\{self.file_name}-output_re_ex.png'
                
                self.input_img = Image.open(self.input_path)
                self.output_img = self.input_img.convert('RGB')
                self.output_img.save(self.output_path)

        Message_box.show_info_messagebox()


class Message_box():

    def show_info_messagebox():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
    
        # setting message for Message Box
        msg.setText("???????????????? ??????????????????!")
        
        # setting Message box window title
        msg.setWindowTitle("Information MessageBox")
        
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        # start the app
        retval = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


