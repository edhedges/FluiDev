# -*- coding: utf-8 -*-
"""
    flow.py
    -------

    flow.py is the applications starting execution starting point, thus
    the name flow is appropriate.
"""

# Python stdlib imports
import os
import shutil
import sqlite3
import sys

# PySide module imports
from PySide.QtGui import QApplication, QMainWindow, QDialog, QFileDialog, \
    QDialogButtonBox, QTableWidgetItem

# UI Design module imports
from FluiDevUI import *
from NewWebsiteDialogUI import *


class FluiDevWebsite(object):
    """
    TODO
    """
    def __init__(self, website_name, website_path, date_created, date_edited):
        """
        TODO
        """
        super(FluiDevWebsite, self).__init__()
        self.website_name = website_name
        self.website_path = website_path
        self.date_created = date_created
        self.date_edited = date_edited

    @staticmethod
    def create(conn, website_name, website_path, date_created, date_edited):
        cursor = conn.cursor()
        query = """INSERT INTO FluiDevWebsite VALUES(
            NULL, :website_name, :website_path, :date_created, :date_edited
        )"""
        cursor.execute(
            query,
            {
                'website_name': website_name,
                'website_path': website_name,
                'date_created': date_created,
                'date_edited': date_edited
            }
        )
        cursor.close()

    @staticmethod
    def read(conn, column_names, table_name):
        """
        TODO
        """
        fd_websites = list()
        cursor = conn.cursor()
        query = "SELECT %s FROM %s" % (column_names, table_name)
        cursor.execute(query)
        read_data = cursor.fetchall()
        cursor.close()
        for row in read_data:
            fd_websites.append(FluiDevWebsite(row[0], row[1], row[2], row[3]))
        return fd_websites

    @staticmethod
    def update(conn):
        pass

    @staticmethod
    def delete(conn):
        #cursor = conn.cursor()
        #query = "DELETE FROM FluiDevWebsite"
        # DELETE FROM `table_name` ??? WHERE clause ???
        cursor.close()
        pass


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
        self.showing_warning = False
        self.ui = NewWebsiteDialogUIDesign()
        self.ui.setupUi(self)

        self.ui.chooseLocationButton.setDisabled(True)
        self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setDisabled(True)
        self.ui.websiteNameTextField.textChanged.connect(
            self.nameOfWebsiteChanged
        )
        self.ui.okCancelButtonBox.accepted.connect(self.createNewWebsite)
        self.ui.chooseLocationButton.clicked.connect(
            self.chooseWebsiteLocation
        )

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
            self.full_website_path = (
                self.website_containing_path +
                '/' +
                self.website_name
            )
            self.ui.locationTextField.setText(self.full_website_path)
            self.existingDirectoryCheck()
        choose_location_enabled = self.ui.chooseLocationButton.isEnabled()
        if choose_location_enabled and not self.website_name:
            self.ui.chooseLocationButton.setEnabled(False)
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setEnabled(
                False
            )
            self.hideWarningLabels()
        elif not choose_location_enabled:
            self.ui.chooseLocationButton.setEnabled(True)
            if self.ui.locationTextField.text():
                self.ui.okCancelButtonBox.button(
                    QDialogButtonBox.Ok).setEnabled(True)
                self.ui.okCancelButtonBox.button(
                    QDialogButtonBox.Ok).setDefault(True)

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
        chosen_location = QFileDialog().getExistingDirectory(
            self,
            "Choose location for website",
            "/"
        )
        if chosen_location:
            self.website_containing_path = chosen_location
        if self.website_containing_path:
            self.full_website_path = (
                self.website_containing_path +
                '/' +
                self.website_name
            )
            self.existingDirectoryCheck()
            self.ui.locationTextField.setText(self.full_website_path)
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setEnabled(
                True
            )
            self.ui.okCancelButtonBox.button(QDialogButtonBox.Ok).setDefault(
                True
            )

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

        self.full_website_path = (
            self.website_containing_path +
            '/' +
            self.website_name
        )
        try:
            shutil.rmtree(self.full_website_path)
            shutil.copytree(self.website_skeleton_path, self.full_website_path)
            ## Add this website to the list of FluiDevWebsite right here ##
        except OSError:
            pass

    def existingDirectoryCheck(self):
        """
        TODO
        """
        if os.path.exists(self.full_website_path) and not self.showing_warning:
            warning_title = 'Warning:'
            warning_message = """Clicking the Ok button will overwrite an
                              existing folder.
                              """
            self.showWarningLabels(warning_title, warning_message)
        else:
            self.hideWarningLabels()

    def showWarningLabels(self, warning_title, warning_message):
        """
        TODO
        """
        self.showing_warning = True
        self.ui.warningTitleLabel.setText(warning_title)
        self.ui.warningContentLabel.setText(warning_message)

    def hideWarningLabels(self):
        """
        TODO
        """
        self.showing_warning = False
        self.ui.warningTitleLabel.clear()
        self.ui.warningContentLabel.clear()


class FluiDevWindow(QMainWindow):
    """
    FluiDevWindow is a QMainWindow that implements the first window a
    user will see when they open FluiDev.

    This class initializes the UI design and functionality and from here
    one can view FluiDev features, create a new website, and resume work
    on existing projects.
    """
    def __init__(self, fd_websites, parent=None):
        """
        Initializes the FluiDevWindow class by declaring the UI design
        and connecting the necessary signals and slots.

        self.existing_website_paths - this will hold the apps existing
        website paths and will get then be used to create a list of type
        FluiDevWebsite.

        self.ui - this will hold the QMainWindow object with the design
        from FluiDevWindow. After the UI is setup then the `Create a
        New Website` button signal is connected to the
        `createNewWebsiteButtonPushed` slot.
        """
        super(FluiDevWindow, self).__init__(parent)
        self.fd_websites = fd_websites
        self.ui = FluiDevUIDesign()
        self.ui.setupUi(self)
        self.populateExistingFluiDevWebsites()
        self.ui.createNewWebsiteButton.clicked.connect(
            self.createNewWebsiteButtonPushed
        )

    def populateExistingFluiDevWebsites(self):
        """
        TODO
        """
        for website in self.fd_websites:
            new_row = self.ui.existingWebsitesDisplay.rowCount()
            self.ui.existingWebsitesDisplay.insertRow(new_row)
            self.ui.existingWebsitesDisplay.setItem(
                new_row,
                0,
                QTableWidgetItem(website.website_name)
            )
            self.ui.existingWebsitesDisplay.setItem(
                new_row,
                1,
                QTableWidgetItem(website.date_created)
            )
            self.ui.existingWebsitesDisplay.setItem(
                new_row,
                2,
                QTableWidgetItem(website.date_edited)
            )

    def createNewWebsiteButtonPushed(self):
        """
        createNewWebsiteButtonPushed is executed when the user presses
        the `Create a New Website` button.

        newWebsiteDialog - creates a QDialog of type NewWesbsitePrompt.
        """
        newWebsiteDialog = NewWebsiteDialog()
        newWebsiteDialog.show()
        newWebsiteDialog.exec_()


def goWithTheFlow():
    """
    goWithTheFlow handles all of the necessary aspects of starting the
    FluiDev application. This consists of creating/initializing the db,
    creating a QApplication, creating the main FluiDevWindow and then
    executing the application.

    app - QApplication necessary in every PySide application

    fluiDevWindow - QMainWindow object that represent the first window
    the user will see when they run the application
    """
    fd_websites = list()
    db_file = 'FluiDev.db'
    db_schema_file = 'FluiDevSchema.sql'
    db_is_new = not os.path.exists(db_file)

    with sqlite3.connect(db_file) as conn:
        if db_is_new:
            with open(db_schema_file, 'rt') as schema_file:
                schema = schema_file.read()
            conn.executescript(schema)

        fd_websites = FluiDevWebsite.read(
            conn,
            'website_name, website_path, date_created, date_edited',
            'FluiDevWebsite'
        )
    conn.close()

    app = QApplication(sys.argv)
    fluiDevWindow = FluiDevWindow(fd_websites)
    fluiDevWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    goWithTheFlow()
