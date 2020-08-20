import sys
import os
from git import Repo

parametros = sys.argv

path = os.getcwd()
if(len(parametros) > 1):
    path = parametros[1]

directorios = []
for result in os.listdir(path):
    path_actual = os.path.join(path,result) 
    if(os.path.isdir(path_actual)):   
        try:
            repo = Repo(path_actual)
            directorios.append(repo)
        except Exception as ex:
            pass

for dir in directorios:
    origin = dir.remotes['origin']
    origin.pull()
