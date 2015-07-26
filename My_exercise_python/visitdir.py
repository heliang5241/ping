#encod:utf-8
import os
def VisitDir(path):
    li = os.listdir(path)
    for p in li:
        pathname = os.path.join(path, p)
        if not os.path.isfile(pathname):
            VisitDir(pathname)
        else:
            print (pathname)

if __name__ == "__main__":
    path = r"d:\drivers"
    VisitDir(path)
