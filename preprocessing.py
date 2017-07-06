import numpy as np
from PIL import Image
from PIL import ImageOps

def jpg_to_nparray(path,img_names, img_size, grayscale = False):
    X = []

    for img_dir in img_names:
        img = Image.open(path+img_dir)
        img = ImageOps.fit(img, img_size, Image.ANTIALIAS)
        
        if grayscale:
            img = ImageOps.grayscale(img)
            img_colors = 1

        img = np.asarray(img, dtype = 'float32') / 255.
        img = np.transpose(img, [2, 0, 1])
        X.append(img)

    X = np.asarray(X)

    return X
