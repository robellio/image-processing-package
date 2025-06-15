import matplotlib.pyplot as plt
from PIL import Image 
import numpy as np

def plot_image(image, title=None, cmap=None, figsize=(10, 8), show=True):

    fig = plt.figure(figsize=figsize)

    if isinstance(image, Image.Image):
        image = np.array(image)

    if len(image.shape) == 2 or (len(image.shape) == 3 and image.shape[2] == 1):
         cmap = cmap or 'gray'

    plt.imshow(image, cmap=cmap)

    if title:
        plt.title(title)
    plt.axis('off')   

    if show:
        plt.show()
    return fig 

def plot_images(imges, titles=None, ncols=3 figsize=(15, 10), show=True):

      fig = plt.figure(figsize=figsize)
      n_images = len(images)
      nrows = (n_images + ncols -1)  

      for i, image in enumerate(images, 1):
           ax = fig.add_subplot(nrows, ncols, 1)

           if isinstance(image, Image.Image):
                image = np.array(image)

            
