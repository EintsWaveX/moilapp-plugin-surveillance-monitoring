# Form implementation generated from reading ui file '.\ui_recoder.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Recorder(object):
    def setupUi(self, Recorder):
        Recorder.setObjectName("Recorder")
        Recorder.setEnabled(True)
        Recorder.resize(1238, 556)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Recorder.sizePolicy().hasHeightForWidth())
        Recorder.setSizePolicy(sizePolicy)
        Recorder.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Recorder)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.wholeFrame = QtWidgets.QFrame(parent=Recorder)
        self.wholeFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.wholeFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wholeFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.wholeFrame.setObjectName("wholeFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.wholeFrame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_3 = QtWidgets.QFrame(parent=self.wholeFrame)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.frame = QtWidgets.QFrame(parent=self.wholeFrame)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.display1 = QtWidgets.QVBoxLayout()
        self.display1.setSpacing(1)
        self.display1.setObjectName("display1")
        self.displayFrame1 = QtWidgets.QFrame(parent=self.frame)
        self.displayFrame1.setMinimumSize(QtCore.QSize(0, 0))
        self.displayFrame1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame1.setObjectName("displayFrame1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.displayFrame1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.displayLab1 = QtWidgets.QLabel(parent=self.displayFrame1)
        self.displayLab1.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.displayLab1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab1.setText("")
        self.displayLab1.setObjectName("displayLab1")
        self.horizontalLayout_6.addWidget(self.displayLab1)
        self.display1.addWidget(self.displayFrame1)
        self.horizontalLayout_2.addLayout(self.display1)
        self.display2 = QtWidgets.QVBoxLayout()
        self.display2.setSpacing(1)
        self.display2.setObjectName("display2")
        self.displayFrame2 = QtWidgets.QFrame(parent=self.frame)
        self.displayFrame2.setMinimumSize(QtCore.QSize(0, 0))
        self.displayFrame2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame2.setObjectName("displayFrame2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.displayFrame2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.displayLab2 = QtWidgets.QLabel(parent=self.displayFrame2)
        self.displayLab2.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab2.setText("")
        self.displayLab2.setObjectName("displayLab2")
        self.horizontalLayout_7.addWidget(self.displayLab2)
        self.display2.addWidget(self.displayFrame2)
        self.horizontalLayout_2.addLayout(self.display2)
        self.display3 = QtWidgets.QVBoxLayout()
        self.display3.setSpacing(1)
        self.display3.setObjectName("display3")
        self.displayFrame3 = QtWidgets.QFrame(parent=self.frame)
        self.displayFrame3.setMinimumSize(QtCore.QSize(0, 0))
        self.displayFrame3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame3.setObjectName("displayFrame3")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.displayFrame3)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.displayLab3 = QtWidgets.QLabel(parent=self.displayFrame3)
        self.displayLab3.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab3.setText("")
        self.displayLab3.setObjectName("displayLab3")
        self.horizontalLayout_21.addWidget(self.displayLab3)
        self.display3.addWidget(self.displayFrame3)
        self.horizontalLayout_2.addLayout(self.display3)
        self.display4 = QtWidgets.QVBoxLayout()
        self.display4.setSpacing(1)
        self.display4.setObjectName("display4")
        self.displayFrame4 = QtWidgets.QFrame(parent=self.frame)
        self.displayFrame4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame4.setObjectName("displayFrame4")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.displayFrame4)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.displayLab4 = QtWidgets.QLabel(parent=self.displayFrame4)
        self.displayLab4.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab4.setText("")
        self.displayLab4.setObjectName("displayLab4")
        self.horizontalLayout_20.addWidget(self.displayLab4)
        self.display4.addWidget(self.displayFrame4)
        self.horizontalLayout_2.addLayout(self.display4)
        self.verticalLayout_4.addWidget(self.frame)
        self.displayFrame5 = QtWidgets.QFrame(parent=self.wholeFrame)
        self.displayFrame5.setObjectName("displayFrame5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.displayFrame5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.display5 = QtWidgets.QVBoxLayout()
        self.display5.setSpacing(1)
        self.display5.setObjectName("display5")
        self.frame_9 = QtWidgets.QFrame(parent=self.displayFrame5)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.displayLab5 = QtWidgets.QLabel(parent=self.frame_9)
        self.displayLab5.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab5.setText("")
        self.displayLab5.setObjectName("displayLab5")
        self.horizontalLayout_8.addWidget(self.displayLab5)
        self.display5.addWidget(self.frame_9)
        self.horizontalLayout_9.addLayout(self.display5)
        self.display6 = QtWidgets.QVBoxLayout()
        self.display6.setSpacing(1)
        self.display6.setObjectName("display6")
        self.displayFrame6 = QtWidgets.QFrame(parent=self.displayFrame5)
        self.displayFrame6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame6.setObjectName("displayFrame6")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.displayFrame6)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.displayLab6 = QtWidgets.QLabel(parent=self.displayFrame6)
        self.displayLab6.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab6.setText("")
        self.displayLab6.setObjectName("displayLab6")
        self.horizontalLayout_15.addWidget(self.displayLab6)
        self.display6.addWidget(self.displayFrame6)
        self.horizontalLayout_9.addLayout(self.display6)
        self.display7 = QtWidgets.QVBoxLayout()
        self.display7.setSpacing(1)
        self.display7.setObjectName("display7")
        self.displayFrame7 = QtWidgets.QFrame(parent=self.displayFrame5)
        self.displayFrame7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame7.setObjectName("displayFrame7")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.displayFrame7)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.displayLab7 = QtWidgets.QLabel(parent=self.displayFrame7)
        self.displayLab7.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab7.setText("")
        self.displayLab7.setObjectName("displayLab7")
        self.horizontalLayout_16.addWidget(self.displayLab7)
        self.display7.addWidget(self.displayFrame7)
        self.horizontalLayout_9.addLayout(self.display7)
        self.display8 = QtWidgets.QVBoxLayout()
        self.display8.setSpacing(1)
        self.display8.setObjectName("display8")
        self.displayFrame8 = QtWidgets.QFrame(parent=self.displayFrame5)
        self.displayFrame8.setMinimumSize(QtCore.QSize(0, 0))
        self.displayFrame8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.displayFrame8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.displayFrame8.setObjectName("displayFrame8")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.displayFrame8)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.displayLab8 = QtWidgets.QLabel(parent=self.displayFrame8)
        self.displayLab8.setMinimumSize(QtCore.QSize(300, 260))
        self.displayLab8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.displayLab8.setText("")
        self.displayLab8.setObjectName("displayLab8")
        self.horizontalLayout_18.addWidget(self.displayLab8)
        self.display8.addWidget(self.displayFrame8)
        self.horizontalLayout_9.addLayout(self.display8)
        self.verticalLayout_4.addWidget(self.displayFrame5)
        self.line_2 = QtWidgets.QFrame(parent=self.wholeFrame)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_5.addWidget(self.wholeFrame)

        self.retranslateUi(Recorder)
        QtCore.QMetaObject.connectSlotsByName(Recorder)

    def retranslateUi(self, Recorder):
        _translate = QtCore.QCoreApplication.translate
        Recorder.setWindowTitle(_translate("Recorder", "Form"))
