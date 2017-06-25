import os
import numpy as np
from PIL import Image
from PIL import ImageOps

def jpg_to_nparray(path,img_names, img_size, grayscale = False):
    X = []
    img_colors = 3

    for counter,img_dir in enumerate(img_names):
        img = Image.open(path+img_dir)
        img = ImageOps.fit(img, img_size, Image.ANTIALIAS)
        
        if grayscale:
            img = ImageOps.grayscale(img)
            img_colors = 1

        img = np.asarray(img, dtype = 'float32') / 255.
        #0 1 2
        img = np.transpose(img,[2,0,1])#.reshape([img_colors]+list(img_size))
        X.append(img)

    X = np.asarray(X)

    return X