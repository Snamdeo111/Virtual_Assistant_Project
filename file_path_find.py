import os
import re
def file_search(name):
    for root, dirs, files in os.walk('C:\\'):
         for file in files:
             if re.search(name.lower(),file.lower()):
                path=root+'\\'+str(file)
                return str(path)


def file_equal_search(name):
    for root, dirs, files in os.walk('C:\\'):
         for file in files:
             if name.lower()==file.lower():
                path=root+'\\'+str(file)
                return str(path)

def file_endswith(name=None):
    if name==None:
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                if name.lower()==file.lower():
                    path = root + '\\' + str(file)
                    return str(path)
    else:
        for root, dirs, files in os.walk('C:\\'):
             for file in files:
                 if file.endswith('.mp3'):
                     path=root + '\\' + str(file)
                     return str(path)