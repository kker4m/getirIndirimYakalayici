from requiredLibraries import *

global seperator
from sys import platform

if platform == 'linux':
    seperator = str(os.path.sep)
else:
    seperator = str(os.path.sep) + str(os.path.sep)


def getParentFolder():
    from sys import platform
    if platform == 'win32':
        A = '\\'
        import sys, pathlib
        if getattr(sys, 'frozen', False):
            current_direct = str(pathlib.Path(sys.executable).parent.resolve()) + A;parantez = str(current_direct)[:-1][
                                                                                               ::-1].find(
                A);parentFolder = str(current_direct)[:-1][::-1][parantez:][::-1]
        elif __file__:
            current_direct = str(pathlib.Path(__file__).parent.resolve()) + A;parantez = str(current_direct)[:-1][
                                                                                         ::-1].find(
                A);parentFolder = str(current_direct)[:-1][::-1][parantez:][::-1]
        return parentFolder
    elif platform == 'linux':
        from pathlib import Path
        parentFolder = Path(Path.cwd()).parent
        parentFolder = str(parentFolder) + '/'
        return str(parentFolder)


global parentFolder
parentFolder = getParentFolder()


if __name__ == '__main__':
    pass