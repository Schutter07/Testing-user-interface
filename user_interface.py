from PyQt5 import QtWidgets, uic
import sys
import requests
from os import getcwd, remove, path
from shutil import copyfile
import subprocess
import pytest

class Ui(QtWidgets.QMainWindow):
    testFileName = ""
    opgaveFileName = ""
    def __init__(self):
        super(Ui, self).__init__()
        if hasattr(sys, '_MEIPASS'):
            ui_path = os.path.join(sys._MEIPASS, "gui.ui")
        else:
            ui_path = "gui.ui"
        uic.loadUi(ui_path, self)  # Load the UI

        testFileName = "-1"
        opgaveFileName = "-1"
        label = "-1"
        self.pushButtonCheck.setEnabled(False)
        self.pushButtonNext.setEnabled(False)
        self.pushButtonPrev.setEnabled(False)

        # Oefeningen hoofdstuk 2
        self.actionOpgave_2_1.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 2.1", "test_opgave2_1.py", "opgave2_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/test_opgave2_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/opgave2_1.txt"))
        self.actionOpgave_2_2.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/opgave2_2.txt"))

        # Oefeningen hoofdstuk 3
        self.actionOpgave_pagina_16.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 16",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina16.txt"))
        self.actionOpgave_pagina_17.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 17",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina17.txt"))
        self.actionOpgave_pagina_20.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave pagina 20", "test_opgave_pagina20.py", "opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina20.txt"))
        self.actionOpgave_3_1.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 3.1", "test_opgave3_1.py", "opgave3_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_1.txt"))
        self.actionOpgave_3_2.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_2.txt"))
        self.actionOpgave_3_3.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3.3",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_3.txt"))
        self.actionOpgave_3_4.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_4.txt"))
        self.actionOpgave_3_5.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 3.5", "test_opgave3_5.py", "opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_5.txt"))

        # oefeningen hoofdstuk 4
        self.actionOpgave_pagina_26.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 26",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina26.txt"))
        self.actionOpgave_pagina_29.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 29",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina29.txt"))
        self.actionOpgave_pagina_31.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 31",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina31.txt"))
        self.actionOpgave_1_pagina_32.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave1_pagina32.txt"))
        self.actionOpgave_2_pagina_32.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave2_pagina32.txt"))
        self.actionOpgave_3_pagina_32.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave3_pagina32.txt"))
        self.actionOpgave_pagina_33.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 33",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina33.txt"))
        self.actionOpgave_4_1.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 4.1",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_1.txt"))
        self.actionOpgave_4_2.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 4.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_2.txt"))
        self.actionOpgave_4_3.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 4.3",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_3.txt"))
        self.actionOpgave_4_4.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 4.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_4.txt"))

        # oefeningen hoofdstuk 5
        self.actionOpgave_1_pagina_41.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina41.txt"))
        self.actionOpgave_2_pagina_41.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina41.txt"))
        self.actionOpgave_3_pagina_41.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave3_pagina41.txt"))
        self.actionOpgave_1_pagina_42.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina42.txt"))
        self.actionOpgave_2_pagina_42.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina42.txt"))
        self.actionOpgave_pagina_43.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave pagina 43", "test_opgave_pagina43.py", "opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave_pagina43.txt"))
        self.actionOpgave_1_pagina_49.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina49.txt"))
        self.actionOpgave_2_pagina_49.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina49.txt"))
        self.actionOpgave_5_1.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 5.1", "test_opgave5_1.py", "opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_1.txt"))
        self.actionOpgave_5_2.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 5.2", "test_opgave5_2.py", "opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_2.txt"))
        self.actionOpgave_5_3.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 5.3", "test_opgave5_3.py", "opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_3.txt"))
        self.actionOpgave_5_4.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 5.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_4.txt"))
        self.actionOpgave_5_5.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 5.5",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_5.txt"))

        # Oefeningen hoofdstuk 6
        self.actionOpgave_1_pagina_53.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina53.txt"))
        self.actionOpgave_2_pagina_53.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina53.txt"))
        self.actionOpgave_3_pagina_53.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 3 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave3_pagina53.txt"))
        self.actionOpgave_pagina_54.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 54",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina54.txt"))
        self.actionOpgave_1_pagina_56.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 1 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina56.txt"))
        self.actionOpgave_2_pagina_56.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 2 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina56.txt"))
        self.actionOpgave_pagina_57.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 57",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina57.txt"))
        self.actionOpgave_pagina_58.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave pagina 58", "test_opgave_pagina58.py", "opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina58.txt"))
        self.actionOpgave_pagina_60.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 60",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina60.txt"))
        self.actionOpgave_pagina_61.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 61",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina61.txt"))
        self.actionOpgave_pagina_62.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave pagina 62",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina62.txt"))
        self.actionOpgave_6_1.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 6.1", "test_opgave6_1.py", "opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_1.txt"))
        self.actionOpgave_6_2.triggered.connect(
            lambda: self.menuClickedWithoutSolution(
                "Opgave 6.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_2.txt"))
        self.actionOpgave_6_3.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 6.3", "test_opgave6_3.py", "opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_3.txt"))
        self.actionOpgave_6_4.triggered.connect(
            lambda: self.menuClickedWithSolution(
                "Opgave 6.4", "test_opgave6_4.py", "opgave6_4.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_4.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_4.txt"))







        #Check oplossing knop
        self.pushButtonCheck.clicked.connect(self.checkOplossing)

        self.pushButtonNext.clicked.connect(self.next)

        self.pushButtonPrev.clicked.connect(self.prev)



        self.show()

    def next(self):
        # Oefeningen hoofdstuk 2
        if self.label == "Opgave 2.1":
            self.menuClickedWithoutSolution(
                "Opgave 2.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/opgave2_2.txt")
        elif self.label == "Opgave 2.2":
            self.menuClickedWithoutSolution(
                "Opgave pagina 16",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina16.txt")

        # Oefeningen hoofdstuk 3
        elif self.label == "Opgave pagina 16":
            self.menuClickedWithoutSolution(
                "Opgave pagina 17",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina17.txt")
        elif self.label == "Opgave pagina 17":
            self.menuClickedWithSolution(
                "Opgave pagina 20", "test_opgave_pagina20.py", "opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina20.txt")
        elif self.label == "Opgave pagina 20":
            self.menuClickedWithSolution(
                "Opgave 3.1", "test_opgave3_1.py", "opgave3_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_1.txt")
        elif self.label == "Opgave 3.1":
            self.menuClickedWithoutSolution(
                "Opgave 3.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_2.txt")
        elif self.label == "Opgave 3.2":
            self.menuClickedWithoutSolution(
                "Opgave 3.3",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_3.txt")
        elif self.label == "Opgave 3.3":
            self.menuClickedWithoutSolution(
                "Opgave 3.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_4.txt")
        elif self.label == "Opgave 3.4":
            self.menuClickedWithSolution(
                "Opgave 3.5", "test_opgave3_5.py", "opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_5.txt")
        elif self.label == "Opgave 3.5":
            self.menuClickedWithoutSolution(
                "Opgave pagina 26",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina26.txt")

        # Oefeningen hoofdstuk 4
        elif self.label == "Opgave pagina 26":
            self.menuClickedWithoutSolution(
                "Opgave pagina 29",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina29.txt")
        elif self.label == "Opgave pagina 29":
            self.menuClickedWithoutSolution(
                "Opgave pagina 31",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina31.txt")
        elif self.label == "Opgave pagina 31":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave1_pagina32.txt")
        elif self.label == "Opgave 1 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave2_pagina32.txt")
        elif self.label == "Opgave 2 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave3_pagina32.txt")
        elif self.label == "Opgave 3 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave pagina 33",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina33.txt")
        elif self.label == "Opgave pagina 33":
            self.menuClickedWithoutSolution(
                "Opgave 4.1",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_1.txt")
        elif self.label == "Opgave 4.1":
            self.menuClickedWithoutSolution(
                "Opgave 4.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_2.txt")
        elif self.label == "Opgave 4.2":
            self.menuClickedWithoutSolution(
                "Opgave 4.3",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_3.txt")
        elif self.label == "Opgave 4.3":
            self.menuClickedWithoutSolution(
                "Opgave 4.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_4.txt")
        elif self.label == "Opgave 4.4":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina41.txt")

        # Oefeningen hoofdstuk 5
        elif self.label == "Opgave 1 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina41.txt")
        elif self.label == "Opgave 2 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave3_pagina41.txt")
        elif self.label == "Opgave 3 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina42.txt")
        elif self.label == "Opgave 1 pagina 42":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina42.txt")
        elif self.label == "Opgave 2 pagina 42":
            self.menuClickedWithSolution(
                "Opgave pagina 43", "test_opgave_pagina43.py", "opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave_pagina43.txt")
        elif self.label == "Opgave pagina 43":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina49.txt")
        elif self.label == "Opgave 1 pagina 49":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina49.txt")
        elif self.label == "Opgave 2 pagina 49":
            self.menuClickedWithSolution(
                "Opgave 5.1", "test_opgave5_1.py", "opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_1.txt")
        elif self.label == "Opgave 5.1":
            self.menuClickedWithSolution(
                "Opgave 5.2", "test_opgave5_2.py", "opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_2.txt")
        elif self.label == "Opgave 5.2":
            self.menuClickedWithSolution(
                "Opgave 5.3", "test_opgave5_3.py", "opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_3.txt")
        elif self.label == "Opgave 5.3":
            self.menuClickedWithoutSolution(
                "Opgave 5.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_4.txt")
        elif self.label == "Opgave 5.4":
            self.menuClickedWithoutSolution(
                "Opgave 5.5",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_5.txt")
        elif self.label == "Opgave 5.5":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina53.txt")

        # Oefeningen hoofdstuk 6
        elif self.label == "Opgave 1 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina53.txt")
        elif self.label == "Opgave 2 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave3_pagina53.txt")
        elif self.label == "Opgave 3 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave pagina 54",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina54.txt")
        elif self.label == "Opgave pagina 54":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina56.txt")
        elif self.label == "Opgave 1 pagina 56":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina56.txt")
        elif self.label == "Opgave 2 pagina 56":
            self.menuClickedWithoutSolution(
                "Opgave pagina 57",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina57.txt")
        elif self.label == "Opgave pagina 57":
            self.menuClickedWithSolution(
                "Opgave pagina 58", "test_opgave_pagina58.py", "opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina58.txt")
        elif self.label == "Opgave pagina 58":
            self.menuClickedWithoutSolution(
                "Opgave pagina 60",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina60.txt")
        elif self.label == "Opgave pagina 60":
            self.menuClickedWithoutSolution(
                "Opgave pagina 61",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina61.txt")
        elif self.label == "Opgave pagina 61":
            self.menuClickedWithoutSolution(
                "Opgave pagina 62",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina62.txt")
        elif self.label == "Opgave pagina 62":
            self.menuClickedWithSolution(
                "Opgave 6.1", "test_opgave6_1.py", "opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_1.txt")
        elif self.label == "Opgave 6.1":
            self.menuClickedWithoutSolution(
                "Opgave 6.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_2.txt")
        elif self.label == "Opgave 6.2":
            self.menuClickedWithSolution(
                "Opgave 6.3", "test_opgave6_3.py", "opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_3.txt")
        elif self.label == "Opgave 6.3":
            self.menuClickedWithSolution(
                "Opgave 6.4", "test_opgave6_4.py", "opgave6_4.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_4.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_4.txt")









    def prev(self):
        # Oefeningen hoofdstuk 2
        if self.label == "Opgave 2.2":
            self.menuClickedWithSolution(
                "Opgave 2.1", "test_opgave2_1.py", "opgave2_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/test_opgave2_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/opgave2_1.txt")

        # Oefeningen hoofdstuk 3
        elif self.label == "Opgave pagina 16":
            self.menuClickedWithoutSolution(
                "Opgave 2.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk2/opgave2_2.txt")
        elif self.label == "Opgave pagina 17":
            self.menuClickedWithoutSolution(
                "Opgave pagina 16",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina16.txt")
        elif self.label == "Opgave pagina 20":
            self.menuClickedWithoutSolution(
                "Opgave pagina 17",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina17.txt")
        elif self.label == "Opgave 3.1":
            self.menuClickedWithSolution(
                "Opgave pagina 20", "test_opgave_pagina20.py", "opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave_pagina20.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave_pagina20.txt")
        elif self.label == "Opgave 3.2":
            self.menuClickedWithSolution(
            "Opgave 3.1", "test_opgave3_1.py", "opgave3_1.py",
            "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_1.py",
            "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_1.txt")
        elif self.label == "Opgave 3.3":
            self.menuClickedWithoutSolution(
            "Opgave 3.2",
            "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_2.txt")
        elif self.label == "Opgave 3.4":
            self.menuClickedWithoutSolution(
            "Opgave 3.3",
            "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_3.txt")
        elif self.label == "Opgave 3.5":
            self.menuClickedWithoutSolution(
            "Opgave 3.4",
            "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_4.txt")

        # Oefeningen hoofdstuk 4
        elif self.label == "Opgave pagina 26":
            self.menuClickedWithSolution(
                "Opgave 3.5", "test_opgave3_5.py", "opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/test_opgave3_5.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk3/opgave3_5.txt")
        elif self.label == "Opgave pagina 29":
            self.menuClickedWithoutSolution(
                "Opgave pagina 26",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina26.txt")
        elif self.label == "Opgave pagina 31":
            self.menuClickedWithoutSolution(
                "Opgave pagina 29",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina29.txt")
        elif self.label == "Opgave 1 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave pagina 31",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina31.txt")
        elif self.label == "Opgave 2 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave1_pagina32.txt")
        elif self.label == "Opgave 3 pagina 32":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave2_pagina32.txt")
        elif self.label == "Opgave pagina 33":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 32",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave3_pagina32.txt")
        elif self.label == "Opgave 4.1":
            self.menuClickedWithoutSolution(
                "Opgave pagina 33",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave_pagina33.txt")
        elif self.label == "Opgave 4.2":
            self.menuClickedWithoutSolution(
                "Opgave 4.1",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_1.txt")
        elif self.label == "Opgave 4.3":
            self.menuClickedWithoutSolution(
                "Opgave 4.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_2.txt")
        elif self.label == "Opgave 4.4":
            self.menuClickedWithoutSolution(
                "Opgave 4.3",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_3.txt")

        # Oefeningen hoofdstuk 5
        elif self.label == "Opgave 1 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 4.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk4/opgave4_4.txt")
        elif self.label == "Opgave 2 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina41.txt")
        elif self.label == "Opgave 3 pagina 41":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina41.txt")
        elif self.label == "Opgave 1 pagina 42":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 41",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave3_pagina41.txt")
        elif self.label == "Opgave 2 pagina 42":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina42.txt")
        elif self.label == "Opgave pagina 43":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 42",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina42.txt")
        elif self.label == "Opgave 1 pagina 49":
            self.menuClickedWithSolution(
                "Opgave pagina 43", "test_opgave_pagina43.py", "opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave_pagina43.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave_pagina43.txt")
        elif self.label == "Opgave 2 pagina 49":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave1_pagina49.txt")
        elif self.label == "Opgave 5.1":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 49",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave2_pagina49.txt")
        elif self.label == "Opgave 5.2":
            self.menuClickedWithSolution(
                "Opgave 5.1", "test_opgave5_1.py", "opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_1.txt")
        elif self.label == "Opgave 5.3":
            self.menuClickedWithSolution(
                "Opgave 5.2", "test_opgave5_2.py", "opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_2.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_2.txt")
        elif self.label == "Opgave 5.4":
            self.menuClickedWithSolution(
                "Opgave 5.3", "test_opgave5_3.py", "opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/test_opgave5_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_3.txt")
        elif self.label == "Opgave 5.5":
            self.menuClickedWithoutSolution(
                "Opgave 5.4",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_4.txt")

        # Oefeningen hoofdstuk 6
        elif self.label == "Opgave 1 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave 5.5",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/opgave5_5.txt")
        elif self.label == "Opgave 2 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina53.txt")
        elif self.label == "Opgave 3 pagina 53":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina53.txt")
        elif self.label == "Opgave pagina 54":
            self.menuClickedWithoutSolution(
                "Opgave 3 pagina 53",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave3_pagina53.txt")
        elif self.label == "Opgave 1 pagina 56":
            self.menuClickedWithoutSolution(
                "Opgave pagina 54",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina54.txt")
        elif self.label == "Opgave 2 pagina 56":
            self.menuClickedWithoutSolution(
                "Opgave 1 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave1_pagina56.txt")
        elif self.label == "Opgave pagina 57":
            self.menuClickedWithoutSolution(
                "Opgave 2 pagina 56",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave2_pagina56.txt")
        elif self.label == "Opgave pagina 58":
            self.menuClickedWithoutSolution(
                "Opgave pagina 57",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina57.txt")
        elif self.label == "Opgave pagina 60":
            self.menuClickedWithSolution(
                "Opgave pagina 58", "test_opgave_pagina58.py", "opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave_pagina58.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina58.txt")
        elif self.label == "Opgave pagina 61":
            self.menuClickedWithoutSolution(
                "Opgave pagina 60",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina60.txt")
        elif self.label == "Opgave pagina 62":
            self.menuClickedWithoutSolution(
                "Opgave pagina 61",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina61.txt")
        elif self.label == "Opgave 6.1":
            self.menuClickedWithoutSolution(
                "Opgave pagina 62",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave_pagina62.txt")
        elif self.label == "Opgave 6.2":
            self.menuClickedWithSolution(
                "Opgave 6.1", "test_opgave6_1.py", "opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_1.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_1.txt")
        elif self.label == "Opgave 6.3":
            self.menuClickedWithoutSolution(
                "Opgave 6.2",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_2.txt")
        elif self.label == "Opgave 6.4":
            self.menuClickedWithSolution(
                "Opgave 6.3", "test_opgave6_3.py", "opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/test_opgave6_3.py",
                "https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk6/opgave6_3.txt")








    def menuClickedWithSolution(self, label, nameTest, nameOpgave, url1, url2):
        self.deleteFiles()
        self.label = label
        self.pushButtonCheck.setEnabled(True)
        self.pushButtonNext.setEnabled(True)
        self.pushButtonPrev.setEnabled(True)
        self.labelOpgave.setText(label)
        self.labelOpgave.adjustSize()
        self.printOpgave(url2)
        self.textConsole.setText("")
        self.testFileName = nameTest
        self.opgaveFileName = nameOpgave
        # download the file contents in binary format
        r = requests.get(url1)
        # open method to open a file on your system and write the contents
        with open(nameTest, "wb") as file:
            file.write(r.content)
        pcinp = requests.get("https://raw.githubusercontent.com/Schutter07/Testfiles/master/Hoofdstuk5/pcinput.py")
        with open("pcinput.py", "wb") as file:
            file.write(pcinp.content)


    def menuClickedWithoutSolution(self, text, url2):
        self.deleteFiles()
        self.pushButtonNext.setEnabled(True)
        self.pushButtonPrev.setEnabled(True)
        self.label = text
        self.labelOpgave.setText(text)
        self.labelOpgave.adjustSize()
        self.printOpgave(url2)
        self.textConsole.setText("Deze heeft geen controle")
        self.pushButtonCheck.setEnabled(False)

    def printOpgave(self, url):
        r = requests.get(url)
        self.textOpgave.setHtml(r.text)

    def checkOplossing(self):
        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        opgaveFileDir, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open", "",
                                                  "Python Files (*.py)", options=options)
        if opgaveFileDir:
            copyfile(opgaveFileDir, getcwd() + "\\" + self.opgaveFileName)
            p = subprocess.run("pytest " + self.testFileName, stdout=subprocess.PIPE, stderr=subprocess.STDOUT )
            self.textConsole.setText(p.stdout.decode("utf-8"))
            remove(self.opgaveFileName)

    def deleteFiles(self):
        if path.isfile(self.opgaveFileName):
            remove(self.opgaveFileName)
        if path.isfile(self.testFileName):
            remove(self.testFileName)
        if path.isfile("pcinput.py"):
            remove("pcinput.py")

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Sluit venster', 'Weet je zeker dat je het venster wil afsluiten?',
                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            self.deleteFiles()
            event.accept()
        else:
            event.ignore()







app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


