import os
from sys import path

def cwd ():
    path = os.getcwd()
    print(f"the current working directory is {path}")
    print("the directory contains the following files:")
    for file in os.listdir(path):
        print(file)

def run():
   print("Processing...")
   cwd()

if __name__ == '__main__':
    run()