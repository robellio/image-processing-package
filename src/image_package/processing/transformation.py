from PIL import Image 

def crop(image, left, top, right, bottom):
    
    return image.crop((left, top, right, bottom))


def rotate(image, degrees, expand=True):

    return image.rotate(degrees, expand=expand)

def resize(image, width=None, height=None):

    return image.resize((width, height))

def flip(image, mode='horizontal'):

    if mode == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    return image.transpose(Image.FLIP_TOP_BOTTOM)