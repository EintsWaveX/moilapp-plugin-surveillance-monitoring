# Form implementation generated from reading ui file '.\ui_setup.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Setup(object):
    def setupUi(self, Setup):
        Setup.setObjectName("Setup")
        Setup.resize(631, 756)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Setup)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalFrame_3 = QtWidgets.QFrame(parent=Setup)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.wholeFrame = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.wholeFrame.setContentsMargins(0, 0, 0, 0)
        self.wholeFrame.setObjectName("wholeFrame")
        self.frame_3 = QtWidgets.QFrame(parent=self.verticalFrame_3)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_title_image_result = QtWidgets.QLabel(parent=self.frame_3)
        self.label_title_image_result.setMinimumSize(QtCore.QSize(300, 25))
        self.label_title_image_result.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_title_image_result.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_title_image_result.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title_image_result.setObjectName("label_title_image_result")
        self.horizontalLayout_9.addWidget(self.label_title_image_result)
        self.label_title_original = QtWidgets.QLabel(parent=self.frame_3)
        self.label_title_original.setMinimumSize(QtCore.QSize(300, 25))
        self.label_title_original.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_title_original.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_title_original.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title_original.setObjectName("label_title_original")
        self.horizontalLayout_9.addWidget(self.label_title_original)
        self.wholeFrame.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalFrame_3)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_image_result = QtWidgets.QLabel(parent=self.frame_2)
        self.label_image_result.setMinimumSize(QtCore.QSize(300, 260))
        self.label_image_result.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_image_result.setText("")
        self.label_image_result.setObjectName("label_image_result")
        self.horizontalLayout_8.addWidget(self.label_image_result)
        self.label_image_original = QtWidgets.QLabel(parent=self.frame_2)
        self.label_image_original.setMinimumSize(QtCore.QSize(300, 260))
        self.label_image_original.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_image_original.setText("")
        self.label_image_original.setObjectName("label_image_original")
        self.horizontalLayout_8.addWidget(self.label_image_original)
        self.wholeFrame.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.verticalFrame_3)
        self.frame.setObjectName("frame")
        self.coordinateFrame = QtWidgets.QHBoxLayout(self.frame)
        self.coordinateFrame.setObjectName("coordinateFrame")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.coordinateFrame.addItem(spacerItem)
        self.label_50 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setMinimumSize(QtCore.QSize(10, 20))
        self.label_50.setObjectName("label_50")
        self.coordinateFrame.addWidget(self.label_50)
        self.label_pos_x = QtWidgets.QLabel(parent=self.frame)
        self.label_pos_x.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pos_x.setObjectName("label_pos_x")
        self.coordinateFrame.addWidget(self.label_pos_x)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.coordinateFrame.addItem(spacerItem1)
        self.label_51 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy)
        self.label_51.setMinimumSize(QtCore.QSize(10, 20))
        self.label_51.setObjectName("label_51")
        self.coordinateFrame.addWidget(self.label_51)
        self.label_pos_y = QtWidgets.QLabel(parent=self.frame)
        self.label_pos_y.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_pos_y.setObjectName("label_pos_y")
        self.coordinateFrame.addWidget(self.label_pos_y)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.coordinateFrame.addItem(spacerItem2)
        self.label_52 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy)
        self.label_52.setMinimumSize(QtCore.QSize(10, 20))
        self.label_52.setObjectName("label_52")
        self.coordinateFrame.addWidget(self.label_52)
        self.label_alpha = QtWidgets.QLabel(parent=self.frame)
        self.label_alpha.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_alpha.setObjectName("label_alpha")
        self.coordinateFrame.addWidget(self.label_alpha)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.coordinateFrame.addItem(spacerItem3)
        self.label_53 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy)
        self.label_53.setMinimumSize(QtCore.QSize(10, 20))
        self.label_53.setObjectName("label_53")
        self.coordinateFrame.addWidget(self.label_53)
        self.label_beta = QtWidgets.QLabel(parent=self.frame)
        self.label_beta.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_beta.setObjectName("label_beta")
        self.coordinateFrame.addWidget(self.label_beta)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.coordinateFrame.addItem(spacerItem4)
        self.wholeFrame.addWidget(self.frame)
        self.frame1 = QtWidgets.QFrame(parent=self.verticalFrame_3)
        self.frame1.setObjectName("frame1")
        self.settingFrame = QtWidgets.QVBoxLayout(self.frame1)
        self.settingFrame.setContentsMargins(-1, 0, -1, -1)
        self.settingFrame.setObjectName("settingFrame")
        self.frame2 = QtWidgets.QFrame(parent=self.frame1)
        self.frame2.setObjectName("frame2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.setModeFrame = QtWidgets.QFrame(parent=self.frame2)
        self.setModeFrame.setObjectName("setModeFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.setModeFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(parent=self.setModeFrame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_15.setMinimumSize(QtCore.QSize(0, 0))
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.comboBox_resolution_sources = QtWidgets.QComboBox(parent=self.frame_4)
        self.comboBox_resolution_sources.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_resolution_sources.setMaximumSize(QtCore.QSize(16777215, 26))
        self.comboBox_resolution_sources.setObjectName("comboBox_resolution_sources")
        self.horizontalLayout_7.addWidget(self.comboBox_resolution_sources)
        self.checkBox = QtWidgets.QCheckBox(parent=self.frame_4)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_7.addWidget(self.checkBox)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.setModeFrame)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.modeSelect = QtWidgets.QFrame(parent=self.frame_5)
        self.modeSelect.setObjectName("modeSelect")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.modeSelect)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.modeLab = QtWidgets.QLabel(parent=self.modeSelect)
        self.modeLab.setMinimumSize(QtCore.QSize(60, 15))
        self.modeLab.setObjectName("modeLab")
        self.verticalLayout_6.addWidget(self.modeLab)
        self.m1Button = QtWidgets.QRadioButton(parent=self.modeSelect)
        self.m1Button.setObjectName("m1Button")
        self.modeSelectGroup = QtWidgets.QButtonGroup(Setup)
        self.modeSelectGroup.setObjectName("modeSelectGroup")
        self.modeSelectGroup.addButton(self.m1Button)
        self.verticalLayout_6.addWidget(self.m1Button)
        self.m2Button = QtWidgets.QRadioButton(parent=self.modeSelect)
        self.m2Button.setObjectName("m2Button")
        self.modeSelectGroup.addButton(self.m2Button)
        self.verticalLayout_6.addWidget(self.m2Button)
        self.labelZoom = QtWidgets.QLabel(parent=self.modeSelect)
        self.labelZoom.setMinimumSize(QtCore.QSize(60, 10))
        self.labelZoom.setObjectName("labelZoom")
        self.verticalLayout_6.addWidget(self.labelZoom)
        self.doubleSpinBox_zoom = QtWidgets.QDoubleSpinBox(parent=self.modeSelect)
        self.doubleSpinBox_zoom.setMaximum(20.0)
        self.doubleSpinBox_zoom.setSingleStep(0.01)
        self.doubleSpinBox_zoom.setObjectName("doubleSpinBox_zoom")
        self.verticalLayout_6.addWidget(self.doubleSpinBox_zoom)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.horizontalLayout_6.addWidget(self.modeSelect)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelAlpha = QtWidgets.QLabel(parent=self.frame_6)
        self.labelAlpha.setMinimumSize(QtCore.QSize(60, 10))
        self.labelAlpha.setObjectName("labelAlpha")
        self.verticalLayout_2.addWidget(self.labelAlpha)
        self.doubleSpinBox_alpha = QtWidgets.QDoubleSpinBox(parent=self.frame_6)
        self.doubleSpinBox_alpha.setMinimum(-360.0)
        self.doubleSpinBox_alpha.setMaximum(360.0)
        self.doubleSpinBox_alpha.setSingleStep(0.1)
        self.doubleSpinBox_alpha.setObjectName("doubleSpinBox_alpha")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_alpha)
        self.labelBeta = QtWidgets.QLabel(parent=self.frame_6)
        self.labelBeta.setMinimumSize(QtCore.QSize(60, 10))
        self.labelBeta.setObjectName("labelBeta")
        self.verticalLayout_2.addWidget(self.labelBeta)
        self.doubleSpinBox_beta = QtWidgets.QDoubleSpinBox(parent=self.frame_6)
        self.doubleSpinBox_beta.setMinimum(-360.0)
        self.doubleSpinBox_beta.setMaximum(360.0)
        self.doubleSpinBox_beta.setSingleStep(0.1)
        self.doubleSpinBox_beta.setObjectName("doubleSpinBox_beta")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_beta)
        self.labelRoll = QtWidgets.QLabel(parent=self.frame_6)
        self.labelRoll.setMinimumSize(QtCore.QSize(60, 10))
        self.labelRoll.setObjectName("labelRoll")
        self.verticalLayout_2.addWidget(self.labelRoll)
        self.doubleSpinBox_roll = QtWidgets.QDoubleSpinBox(parent=self.frame_6)
        self.doubleSpinBox_roll.setMinimum(-360.0)
        self.doubleSpinBox_roll.setMaximum(360.0)
        self.doubleSpinBox_roll.setSingleStep(0.1)
        self.doubleSpinBox_roll.setObjectName("doubleSpinBox_roll")
        self.verticalLayout_2.addWidget(self.doubleSpinBox_roll)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout_6.addWidget(self.frame_6)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.horizontalLayout_2.addWidget(self.setModeFrame)
        self.navigationFrame = QtWidgets.QFrame(parent=self.frame2)
        self.navigationFrame.setObjectName("navigationFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.navigationFrame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame3 = QtWidgets.QFrame(parent=self.navigationFrame)
        self.frame3.setObjectName("frame3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame3)
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.leftButton = QtWidgets.QPushButton(parent=self.frame3)
        self.leftButton.setMinimumSize(QtCore.QSize(60, 60))
        self.leftButton.setMaximumSize(QtCore.QSize(50, 50))
        self.leftButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.leftButton.setIcon(icon)
        self.leftButton.setObjectName("leftButton")
        self.horizontalLayout.addWidget(self.leftButton)
        self.horizontalLayout_4.addWidget(self.frame3)
        self.frame4 = QtWidgets.QFrame(parent=self.navigationFrame)
        self.frame4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.frame4.setObjectName("frame4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame4)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.topButton = QtWidgets.QPushButton(parent=self.frame4)
        self.topButton.setMinimumSize(QtCore.QSize(60, 60))
        self.topButton.setMaximumSize(QtCore.QSize(50, 50))
        self.topButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/up.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.topButton.setIcon(icon1)
        self.topButton.setObjectName("topButton")
        self.verticalLayout.addWidget(self.topButton)
        self.centerButton = QtWidgets.QPushButton(parent=self.frame4)
        self.centerButton.setMinimumSize(QtCore.QSize(60, 60))
        self.centerButton.setMaximumSize(QtCore.QSize(50, 50))
        self.centerButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.centerButton.setIcon(icon2)
        self.centerButton.setObjectName("centerButton")
        self.verticalLayout.addWidget(self.centerButton)
        self.belowButton = QtWidgets.QPushButton(parent=self.frame4)
        self.belowButton.setMinimumSize(QtCore.QSize(60, 60))
        self.belowButton.setMaximumSize(QtCore.QSize(50, 50))
        self.belowButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/down.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.belowButton.setIcon(icon3)
        self.belowButton.setObjectName("belowButton")
        self.verticalLayout.addWidget(self.belowButton)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem9)
        self.horizontalLayout_4.addWidget(self.frame4)
        self.frame5 = QtWidgets.QFrame(parent=self.navigationFrame)
        self.frame5.setObjectName("frame5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame5)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rightButton = QtWidgets.QPushButton(parent=self.frame5)
        self.rightButton.setMinimumSize(QtCore.QSize(60, 60))
        self.rightButton.setMaximumSize(QtCore.QSize(50, 50))
        self.rightButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.rightButton.setIcon(icon4)
        self.rightButton.setObjectName("rightButton")
        self.horizontalLayout_3.addWidget(self.rightButton)
        self.horizontalLayout_4.addWidget(self.frame5)
        spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.horizontalLayout_2.addWidget(self.navigationFrame)
        self.settingFrame.addWidget(self.frame2)
        self.frame6 = QtWidgets.QFrame(parent=self.frame1)
        self.frame6.setObjectName("frame6")
        self.endFrame = QtWidgets.QHBoxLayout(self.frame6)
        self.endFrame.setObjectName("endFrame")
        self.cancelButton = QtWidgets.QPushButton(parent=self.frame6)
        self.cancelButton.setMinimumSize(QtCore.QSize(120, 30))
        self.cancelButton.setObjectName("cancelButton")
        self.endFrame.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(parent=self.frame6)
        self.okButton.setMinimumSize(QtCore.QSize(120, 30))
        self.okButton.setObjectName("okButton")
        self.endFrame.addWidget(self.okButton)
        self.settingFrame.addWidget(self.frame6)
        self.wholeFrame.addWidget(self.frame1)
        self.verticalLayout_5.addWidget(self.verticalFrame_3)

        self.retranslateUi(Setup)
        QtCore.QMetaObject.connectSlotsByName(Setup)

    def retranslateUi(self, Setup):
        _translate = QtCore.QCoreApplication.translate
        Setup.setWindowTitle(_translate("Setup", "Form"))
        self.label_title_image_result.setText(_translate("Setup", "Result View"))
        self.label_title_original.setText(_translate("Setup", "Original View"))
        self.label_50.setText(_translate("Setup", "x:"))
        self.label_pos_x.setText(_translate("Setup", "0"))
        self.label_51.setText(_translate("Setup", "y:"))
        self.label_pos_y.setText(_translate("Setup", "0"))
        self.label_52.setText(_translate("Setup", "α:"))
        self.label_alpha.setText(_translate("Setup", "0"))
        self.label_53.setText(_translate("Setup", "β:"))
        self.label_beta.setText(_translate("Setup", "0"))
        self.label_15.setText(_translate("Setup", "Camera Res:"))
        self.checkBox.setText(_translate("Setup", "Polygon"))
        self.modeLab.setText(_translate("Setup", "Mode:"))
        self.m1Button.setText(_translate("Setup", "M1"))
        self.m2Button.setText(_translate("Setup", "M2"))
        self.labelZoom.setText(_translate("Setup", "Zoom:"))
        self.labelAlpha.setText(_translate("Setup", "Alpha:"))
        self.labelBeta.setText(_translate("Setup", "Beta:"))
        self.labelRoll.setText(_translate("Setup", "Roll:"))
        self.cancelButton.setText(_translate("Setup", "Cancel"))
        self.okButton.setText(_translate("Setup", "OK"))
