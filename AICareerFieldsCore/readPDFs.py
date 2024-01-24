import os
import pandas as pd
import subprocess

def loadPackages(file_name):
    with open(file_name, 'r') as file:
        for package in file:
            package = package.strip()  #get rid of whitespace
            # check if pkg is installed, attempt import.
            if package:
                subprocess.run(['pip3', 'install', package])
                #subprocess.call(['pip', 'install', package])