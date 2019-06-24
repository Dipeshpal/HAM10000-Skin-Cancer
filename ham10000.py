import pandas as pd
import os
import shutil


df = pd.read_csv('HAM10000_metadata.csv')

image_dir = 'img'


def cpy(file, des):
    file = 'img/HAM/'+file
    des = 'dataset/'+des+"/"
    shutil.copy(file, des)
    print(file + 'copied to ' + des + 'successfully')


def create_dir(dir):
    path = 'dataset/' + dir
    try:
        os.mkdir(path)
    except OSError:
        # print("Creation of the directory %s failed" % path)
        pass
    else:
        print("Successfully created the directory %s " % path)


def hh(f):
    c = -1
    for i in df['image_id']:
        c += 1
        if f == i+'.jpg':
            dir = df['dx'][c]
            create_dir(dir)
            cpy(f, dir)


for root, dirs, files in os.walk(image_dir):
    for file in files:
        hh(file)
