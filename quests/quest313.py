"""
Write a synchronous function that makes a directory and recursively makes all of its parent directories as necessary.

A directory is specified via a sequence of arguments which specify the path. For example:

mkdirp('/','tmp','made','some','dir')

...will make the directory /tmp/made/some/dir.

Like the shell command mkdir -p, the function you program should be idempotent if the directory already exists.
"""
import  os
def mkdir(*directories:str):
    dirs  = os.path.join(*directories)
    try:
        os.makedirs(dirs,exist_ok=True)
        print('ok')
    except FileExistsError:
        pass
