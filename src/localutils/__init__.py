import pathlib
import os
import importlib
import sys

def load_files(directory):
    cwd = pathlib.Path.cwd()
    os.chdir(directory)
    for name in [x[:-3] for x in os.listdir() if x[-3:] == '.py']:
        module = importlib.import_module(name)
        globals()[name] = module
        sys.modules[f'localutils.{name}'] = module
    os.chdir(cwd)

load_files(pathlib.Path.home()/'.python_utils')
del pathlib,os,importlib,sys,load_files
