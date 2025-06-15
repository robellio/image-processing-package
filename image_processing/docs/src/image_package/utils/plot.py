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

def plot_images(images, titles=None, ncols=3, figsize=(15, 10), show=True):
    
    fig = plt.figure(figsize=figsize)
    n_images = len(images)
    nrows = (n_images + ncols - 1) // ncols
    
    for i, image in enumerate(images, 1):
        ax = fig.add_subplot(nrows, ncols, i)
        
        if isinstance(image, Image.Image):
            image = np.array(image)
        
        if len(image.shape) == 2 or (len(image.shape) == 3 and image.shape[2] == 1):
            ax.imshow(image, cmap='gray')
        else:
            ax.imshow(image)
            
        if titles and i-1 < len(titles):
            ax.set_title(titles[i-1])
        ax.axis('off')
    
    plt.tight_layout()
    
    if show:
        plt.show()
    
    return fig

def plot_histogram(image, title='Histograma de Cores', figsize=(10, 6), show=True):
   
    fig = plt.figure(figsize=figsize)
    
    if isinstance(image, Image.Image):
        image = np.array(image)
    
    if len(image.shape) == 2:  # Grayscale
        plt.hist(image.ravel(), bins=256, color='gray', alpha=0.7)
        plt.title(f"{title} (Escala de Cinza)")
    else:  # Color
        colors = ('red', 'green', 'blue')
        for i, color in enumerate(colors):
            plt.hist(image[:, :, i].ravel(), bins=256, color=color, alpha=0.5, label=color)
        plt.title(f"{title} (RGB)")
        plt.legend()
    
    plt.xlabel('Intensidade')
    plt.ylabel('Frequência')
    plt.grid(True, alpha=0.3)
    
    if show:
        plt.show()
    
    return fig