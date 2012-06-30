# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class FluiDevUIDesign(object):
    def setupUi(self, FluiDevMainWindow):
        FluiDevMainWindow.setObjectName("FluiDevMainWindow")
        FluiDevMainWindow.resize(844, 550)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FluiDevMainWindow.sizePolicy().hasHeightForWidth())
        FluiDevMainWindow.setSizePolicy(sizePolicy)
        FluiDevMainWindow.setMinimumSize(QtCore.QSize(844, 550))
        FluiDevMainWindow.setMaximumSize(QtCore.QSize(844, 550))
        FluiDevMainWindow.setBaseSize(QtCore.QSize(844, 550))
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
        FluiDevMainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        FluiDevMainWindow.setFont(font)
        FluiDevMainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(FluiDevMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.createNewWebsiteButton = QtGui.QPushButton(self.centralwidget)
        self.createNewWebsiteButton.setGeometry(QtCore.QRect(480, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.createNewWebsiteButton.setFont(font)
        self.createNewWebsiteButton.setObjectName("createNewWebsiteButton")
        self.existingWebsitesDisplay = QtGui.QTableWidget(self.centralwidget)
        self.existingWebsitesDisplay.setGeometry(QtCore.QRect(480, 160, 302, 311))
        self.existingWebsitesDisplay.setObjectName("existingWebsitesDisplay")
        self.existingWebsitesDisplay.setColumnCount(3)
        self.existingWebsitesDisplay.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.existingWebsitesDisplay.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.existingWebsitesDisplay.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.existingWebsitesDisplay.setHorizontalHeaderItem(2, item)
        self.existingWebsitesLabel = QtGui.QLabel(self.centralwidget)
        self.existingWebsitesLabel.setGeometry(QtCore.QRect(550, 130, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.existingWebsitesLabel.setFont(font)
        self.existingWebsitesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.existingWebsitesLabel.setObjectName("existingWebsitesLabel")
        self.featureList = QtGui.QTreeWidget(self.centralwidget)
        self.featureList.setGeometry(QtCore.QRect(60, 160, 321, 311))
        self.featureList.setObjectName("featureList")
        item_0 = QtGui.QTreeWidgetItem(self.featureList)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.featureList)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_0 = QtGui.QTreeWidgetItem(self.featureList)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.titleLabel = QtGui.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(60, 20, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setWeight(75)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.authorLabel = QtGui.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(60, 70, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(50)
        font.setBold(False)
        self.authorLabel.setFont(font)
        self.authorLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.authorLabel.setOpenExternalLinks(True)
        self.authorLabel.setObjectName("authorLabel")
        self.featuresLabel = QtGui.QLabel(self.centralwidget)
        self.featuresLabel.setGeometry(QtCore.QRect(130, 130, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.featuresLabel.setFont(font)
        self.featuresLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.featuresLabel.setObjectName("featuresLabel")
        FluiDevMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(FluiDevMainWindow)
        self.statusbar.setObjectName("statusbar")
        FluiDevMainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSimple_Web = QtGui.QMenu(self.menubar)
        self.menuSimple_Web.setObjectName("menuSimple_Web")
        FluiDevMainWindow.setMenuBar(self.menubar)
        self.actionAbout_Simple_Web = QtGui.QAction(FluiDevMainWindow)
        self.actionAbout_Simple_Web.setObjectName("actionAbout_Simple_Web")
        self.actionPreferences = QtGui.QAction(FluiDevMainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionQuite = QtGui.QAction(FluiDevMainWindow)
        self.actionQuite.setObjectName("actionQuite")
        self.actionNew_Website = QtGui.QAction(FluiDevMainWindow)
        self.actionNew_Website.setObjectName("actionNew_Website")
        self.actionOpen_Existing_Website = QtGui.QAction(FluiDevMainWindow)
        self.actionOpen_Existing_Website.setObjectName("actionOpen_Existing_Website")
        self.actionSave_Website = QtGui.QAction(FluiDevMainWindow)
        self.actionSave_Website.setObjectName("actionSave_Website")
        self.actionDocumentation = QtGui.QAction(FluiDevMainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionSource_Code = QtGui.QAction(FluiDevMainWindow)
        self.actionSource_Code.setObjectName("actionSource_Code")
        self.actionSupport = QtGui.QAction(FluiDevMainWindow)
        self.actionSupport.setObjectName("actionSupport")
        self.actionDonate = QtGui.QAction(FluiDevMainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.actionTutorial = QtGui.QAction(FluiDevMainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionAbout = QtGui.QAction(FluiDevMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionPreferences_2 = QtGui.QAction(FluiDevMainWindow)
        self.actionPreferences_2.setObjectName("actionPreferences_2")
        self.actionQuit = QtGui.QAction(FluiDevMainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout_2 = QtGui.QAction(FluiDevMainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionPreferencew = QtGui.QAction(FluiDevMainWindow)
        self.actionPreferencew.setObjectName("actionPreferencew")
        self.actionQuit_2 = QtGui.QAction(FluiDevMainWindow)
        self.actionQuit_2.setObjectName("actionQuit_2")
        self.actionAdf = QtGui.QAction(FluiDevMainWindow)
        self.actionAdf.setObjectName("actionAdf")
        self.actionAbout_3 = QtGui.QAction(FluiDevMainWindow)
        self.actionAbout_3.setObjectName("actionAbout_3")
        self.actionPreferences_3 = QtGui.QAction(FluiDevMainWindow)
        self.actionPreferences_3.setObjectName("actionPreferences_3")
        self.actionQuit_3 = QtGui.QAction(FluiDevMainWindow)
        self.actionQuit_3.setObjectName("actionQuit_3")
        self.actionInfo = QtGui.QAction(FluiDevMainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionSettings = QtGui.QAction(FluiDevMainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionQuit_4 = QtGui.QAction(FluiDevMainWindow)
        self.actionQuit_4.setObjectName("actionQuit_4")
        self.menuFile.addAction(self.actionNew_Website)
        self.menuFile.addAction(self.actionOpen_Existing_Website)
        self.menuHelp.addAction(self.actionSupport)
        self.menuHelp.addAction(self.actionTutorial)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionSource_Code)
        self.menuHelp.addAction(self.actionDonate)
        self.menuSimple_Web.addAction(self.actionInfo)
        self.menubar.addAction(self.menuSimple_Web.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(FluiDevMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FluiDevMainWindow)

    def retranslateUi(self, FluiDevMainWindow):
        FluiDevMainWindow.setWindowTitle(QtGui.QApplication.translate("FluiDevMainWindow", "FluiDev", None, QtGui.QApplication.UnicodeUTF8))
        self.createNewWebsiteButton.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Create a New  Website", None, QtGui.QApplication.UnicodeUTF8))
        self.existingWebsitesDisplay.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("FluiDevMainWindow", "Website Name", None, QtGui.QApplication.UnicodeUTF8))
        self.existingWebsitesDisplay.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("FluiDevMainWindow", "Date Last Edited", None, QtGui.QApplication.UnicodeUTF8))
        self.existingWebsitesDisplay.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("FluiDevMainWindow", "Date Created", None, QtGui.QApplication.UnicodeUTF8))
        self.existingWebsitesLabel.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Existings Websites", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.headerItem().setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Feature List", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.featureList.isSortingEnabled()
        self.featureList.setSortingEnabled(False)
        self.featureList.topLevelItem(0).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Website Management", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(0).child(0).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Create, edit, and delete static pages", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(0).child(1).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Create, edit, and delete a static blog", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(0).child(2).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Customize website settings", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(1).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Markup Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(1).child(0).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Markdown", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(1).child(1).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "HTML5", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(1).child(2).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "reStructuredText", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(1).child(3).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Zen Coding", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(2).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Theme Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(2).child(0).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Editable barebones theme", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(2).child(1).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Editable Simple Web theme", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(2).child(2).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Create and edit custom themes", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.topLevelItem(2).child(3).setText(0, QtGui.QApplication.translate("FluiDevMainWindow", "Write custom CSS", None, QtGui.QApplication.UnicodeUTF8))
        self.featureList.setSortingEnabled(__sortingEnabled)
        self.titleLabel.setText(QtGui.QApplication.translate("FluiDevMainWindow", "FluiDev", None, QtGui.QApplication.UnicodeUTF8))
        self.authorLabel.setText(QtGui.QApplication.translate("FluiDevMainWindow", "by <a href=\"http://edhedges.com\">Eddie Hedges</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.featuresLabel.setText(QtGui.QApplication.translate("FluiDevMainWindow", "FluiDev Features", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("FluiDevMainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("FluiDevMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSimple_Web.setTitle(QtGui.QApplication.translate("FluiDevMainWindow", "Simple Web", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Simple_Web.setText(QtGui.QApplication.translate("FluiDevMainWindow", "About Simple Web", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuite.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Website.setText(QtGui.QApplication.translate("FluiDevMainWindow", "New Website", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen_Existing_Website.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Open Existing Website", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_Website.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Save Website", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocumentation.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Documentation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSource_Code.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Source Code", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSupport.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Support", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDonate.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Donate", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTutorial.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Tutorial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("FluiDevMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences_2.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_2.setText(QtGui.QApplication.translate("FluiDevMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferencew.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_2.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdf.setText(QtGui.QApplication.translate("FluiDevMainWindow", "adf", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_3.setText(QtGui.QApplication.translate("FluiDevMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences_3.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_3.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInfo.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit_4.setText(QtGui.QApplication.translate("FluiDevMainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
