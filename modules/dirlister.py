import os

def run(**arg):
    files=os.listdir(".")
    return str(files)
