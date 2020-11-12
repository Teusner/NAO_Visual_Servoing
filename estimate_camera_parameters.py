import numpy as np
from PIL import Image
import requests
from ball_tracking import BallTracker


def estimate():
    path = r"https://ensta-bretagne.fr/zerr/filerepo/vsik/nao/"
    images = np.array(["top-cam-060-yellow-ball/naoreal_0060.png", "top-cam-080-yellow-ball/naoreal_0060.png", "top-cam-100-yellow-ball/naoreal_0050.png", "top-cam-120-yellow-ball/naoreal_0060.png"])

    bt = BallTracker()

    lb = 0.09
    y = np.zeros(images.size) # = lambda / beta

    for i in range(len(images)):
        im = Image.open(requests.get(path + images[i], stream=True).raw)

        open_cv_image = np.array(im) 
        # Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy()

        _, _, radius = bt.add_frame(open_cv_image)
        
        db = np.sqrt(0.4**2 + (0.6+i*0.2)**2)
        y[i] = db*2*radius/lb
    
    return np.mean(y)

if __name__ == "__main__":
    print("lamba/beta = {}".format(estimate()))