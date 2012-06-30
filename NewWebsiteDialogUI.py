# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class NewWebsiteDialogUIDesign(object):
    def setupUi(self, newWebsiteDialog):
        newWebsiteDialog.setObjectName("newWebsiteDialog")
        newWebsiteDialog.resize(689, 260)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newWebsiteDialog.sizePolicy().hasHeightForWidth())
        newWebsiteDialog.setSizePolicy(sizePolicy)
        newWebsiteDialog.setMinimumSize(QtCore.QSize(689, 260))
        newWebsiteDialog.setMaximumSize(QtCore.QSize(689, 260))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        newWebsiteDialog.setPalette(palette)
        newWebsiteDialog.setModal(True)
        self.layoutWidget = QtGui.QWidget(newWebsiteDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 651, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.okCancelButtonBox = QtGui.QDialogButtonBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okCancelButtonBox.sizePolicy().hasHeightForWidth())
        self.okCancelButtonBox.setSizePolicy(sizePolicy)
        self.okCancelButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.okCancelButtonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.okCancelButtonBox.setObjectName("okCancelButtonBox")
        self.gridLayout.addWidget(self.okCancelButtonBox, 2, 2, 1, 1)
        self.websiteNameLabel = QtGui.QLabel(self.layoutWidget)
        self.websiteNameLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.websiteNameLabel.setObjectName("websiteNameLabel")
        self.gridLayout.addWidget(self.websiteNameLabel, 0, 0, 1, 1)
        self.websiteNameTextField = QtGui.QLineEdit(self.layoutWidget)
        self.websiteNameTextField.setObjectName("websiteNameTextField")
        self.gridLayout.addWidget(self.websiteNameTextField, 0, 1, 1, 1)
        self.locationTextField = QtGui.QLineEdit(self.layoutWidget)
        self.locationTextField.setText("")
        self.locationTextField.setReadOnly(True)
        self.locationTextField.setObjectName("locationTextField")
        self.gridLayout.addWidget(self.locationTextField, 1, 1, 1, 1)
        self.locationLabel = QtGui.QLabel(self.layoutWidget)
        self.locationLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 1, 0, 1, 1)
        self.chooseLocationButton = QtGui.QPushButton(self.layoutWidget)
        self.chooseLocationButton.setObjectName("chooseLocationButton")
        self.gridLayout.addWidget(self.chooseLocationButton, 1, 2, 1, 1)
        self.warningTitleLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setItalic(False)
        font.setUnderline(False)
        font.setBold(True)
        self.warningTitleLabel.setFont(font)
        self.warningTitleLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.warningTitleLabel.setText("")
        self.warningTitleLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.warningTitleLabel.setObjectName("warningTitleLabel")
        self.gridLayout.addWidget(self.warningTitleLabel, 2, 0, 1, 1)
        self.warningContentLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.warningContentLabel.setFont(font)
        self.warningContentLabel.setStyleSheet("color: rgb(255, 0, 0);")
        self.warningContentLabel.setText("")
        self.warningContentLabel.setWordWrap(True)
        self.warningContentLabel.setObjectName("warningContentLabel")
        self.gridLayout.addWidget(self.warningContentLabel, 2, 1, 1, 1)

        self.retranslateUi(newWebsiteDialog)
        QtCore.QObject.connect(self.okCancelButtonBox, QtCore.SIGNAL("accepted()"), newWebsiteDialog.accept)
        QtCore.QObject.connect(self.okCancelButtonBox, QtCore.SIGNAL("rejected()"), newWebsiteDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newWebsiteDialog)

    def retranslateUi(self, newWebsiteDialog):
        newWebsiteDialog.setWindowTitle(QtGui.QApplication.translate("newWebsiteDialog", "New Website", None, QtGui.QApplication.UnicodeUTF8))
        self.websiteNameLabel.setText(QtGui.QApplication.translate("newWebsiteDialog", "Website Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.locationLabel.setText(QtGui.QApplication.translate("newWebsiteDialog", "Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.chooseLocationButton.setText(QtGui.QApplication.translate("newWebsiteDialog", "Choose Location...", None, QtGui.QApplication.UnicodeUTF8))
