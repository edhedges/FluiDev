# -*- coding: utf-8 -*-
"""
    flow.py
    -------

    flow.py is the applications starting execution starting point, thus
    the name flow is appropriate.
"""

# Python stdlib imports
import os
import sys
import shutil

# PySide module imports
from PySide.QtGui import QApplication, QMainWindow, QDialog, QFileDialog, \
    QDialogButtonBox

# UI Design module imports
from FluiDevUI import *
from NewWebsiteDialogUI import *


class NewWebsiteDialog(QDialog):
    """
    NewWebsiteDialog is a QDialog window that implements what happens if
    the user decides to click the `Create a New Website` button.

    This class sets up the UI and functionality for the QDialog that
    aims at making the creation of a new project simple.
    """

    def __init__(self, parent=None):
        """
        Initializes the NewWebsiteDialog QDialog window by creating some
        class bound variables, setting up the UI, and connecting signals
        and slots.

        self.website_name - This variable stores the website name that
        is typed in by the user.

        self.website_containing_path - This variable holds the path that
        the user chooses. This path will hold a directory named after
        `self.website_name`.

        self.full_website_path - This variable holds the full path of
        the new website. This includes `self.website_containing_path`
        and `self.website_name`.

        self.new_website_skeleton_path - This variable holds the full
        path of the new website skeleton. The contents of this directory
        will be copied into every new website the user creates.

        Three signals are connected to slots that handle input for a new
        website name, website path, and whether the user will create it
        via the `Ok` button or not via the `Cancel` button.
        """
        super(NewWebsiteDialog, self).__init__(parent)
        self.website_name = ''
        self.website_containing_path = ''
        self.full_website_path = ''
        self.website_skeleton_path = os.getcwd() + '/assets/skeleton'
        self.ui = NewWebsiteDialogUIDesign()
        self.ui.setupUi(self)
        self.ui.chooseLocationButton.setDisabled(True)
        self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setDisabled(True)
        self.ui.websiteNameTextField.textChanged.connect(self.nameOfWebsiteChanged)
        self.ui.okCancelButtonBox.accepted.connect(self.createNewWebsite)
        self.ui.chooseLocationButton.clicked.connect(self.chooseWebsiteLocation)

    def nameOfWebsiteChanged(self):
        """
        nameOfWebsiteChanged is executed when the user makes a change to
        the text in the `Website Name`.

        self.website_name - this variable holds the value used for the
        new websites name.

        This function checks sets the name of the website that will be
        used to create a directory with the same name in the file system
        of the computer. While setting this value it also checks whether
        the path has already been chosen it also makes sure that if the
        path is picked and the websites name changes it updates the path
        automatically. Another thing it does is handle whether the `Ok`
        button and `Choose Location` button are enabled and disabled in
        the correct manner.

        For example if the user has not typed a name in the `Website
        Name` box then both the `Choose Location` and the `Ok` button
        are disabled. When the user enters the website name the `Choose
        Location` button becomes enabled. After the user has chosen a
        location to store their site at the `Ok` button becomes enabled.
        Now the user can either click ok and the website is created,
        change the path of the website, or change the name. If the name
        is changed the path is updated in real time as stated above.
        """
        self.website_name = self.ui.websiteNameTextField.text()
        if self.ui.locationTextField.text():
            self.ui.locationTextField.setText(
                self.website_containing_path +
                '/' +
                self.website_name
            )
        choose_location_enabled = self.ui.chooseLocationButton.isEnabled()
        if choose_location_enabled and not self.website_name:
            self.ui.chooseLocationButton.setEnabled(False)
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        elif not choose_location_enabled:
            self.ui.chooseLocationButton.setEnabled(True)
            if self.ui.locationTextField.text():
                self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setEnabled(True)
                self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setDefault(True)

    def chooseWebsiteLocation(self):
        """
        chooseWebsiteLocation is executed when the user clicks the
        `Choose location...` button.

        self.website_containing_path - this variable holds the path that
        the user will set using the native file system dialog which is
        called by the QFileDialog static method `getExistingDirectory`.

        The function does a check to make sure that the path actually
        exists then sets the `self.full_website_path`. The read only
        QLineEdit text is then set to a string representing the path
        chosen + the name of the website. For a greater user experience
        the QDialogButtonBox.Ok button is enabled and set as the default
        option.
        """
        self.website_containing_path = QFileDialog().getExistingDirectory(
                self,
                "Choose location for website",
                "/"
            )
        if self.website_containing_path:
            self.full_website_path = self.website_containing_path + '/' + self.website_name
            self.ui.locationTextField.setText(self.full_website_path)
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setEnabled(True)
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setDefault(True)

    def createNewWebsite(self):
        """
        createNewWebsite is executed when a `self.website_name` and
        `self.website_containing_path` have been set and the user clicks
        the QDialogButtonBox.Ok button.

        self.full_website_path - this variable holds the path where the
        new websites project directory and files will be created.

        When this function is ran a directory by the name of the website
        is created at the specified path and some bare bones files and
        directories are copied into the website directory. The contents
        of the website directory contain the bare minimum that must be
        done for most sites while still giving the user complete content
        control.
        """

        self.full_website_path = self.website_containing_path + '/' + self.website_name
        try:
            shutil.copytree(self.website_skeleton_path, self.full_website_path)
        except OSError:
            # Open dialog asking if they would like to overwrite file
            # depending on the answer either do nothing or overwite away
            pass


class FluiDevWindow(QMainWindow):
    """
    FluiDevWindow is a QMainWindow that implements the first window a
    user will see when they open FluiDev.

    This class initializes the UI design and functionality and from here
    one can view FluiDev features, create a new website, and resume work
    on existing projects.
    """

    def __init__(self, parent=None):
        """
        Initializes the FluiDevWindow class by declaring the UI design
        and connecting the necessary signals and slots.

        self.ui - this will hold the QMainWindow object with the design
        from FluiDevWindow. After the UI is setup then the `Create a
        New Website` button signal is connected to the
        `createNewWebsiteButtonPushed` slot.
        """
        super(FluiDevWindow, self).__init__(parent)
        self.ui = FluiDevUIDesign()
        self.ui.setupUi(self)
        self.ui.createNewWebsiteButton.clicked.connect(self.createNewWebsiteButtonPushed)

    def createNewWebsiteButtonPushed(self):
        """
        createNewWebsiteButtonPushed is executed when the user presses
        the `Create a New Website` button.

        newWebsiteDialog - creates a QDialog of type NewWesbsitePrompt.
        The dialog is then set to modal so it retains focus and is shown
        and executed.
        """
        newWebsiteDialog = NewWebsiteDialog()
        newWebsiteDialog.setModal(True)
        newWebsiteDialog.show()
        newWebsiteDialog.exec_()


def goWithTheFlow():
    """
    goWithTheFlow creates a QApplication and a QMainWindow. Then it
    shows the QMainWindow and executes the QApplication. This function
    starts the application.

    app - QApplication necessary in every PySide application

    fluiDevWindow - QMainWindow object that represent the first window
    the user will see when they run the application
    """
    app = QApplication(sys.argv)
    fluiDevWindow = FluiDevWindow()
    fluiDevWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    goWithTheFlow()
