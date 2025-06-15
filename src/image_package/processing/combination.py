from PIL import Image 

def blend_images(image1, image2, alpha=0.5):

    if image1.size != image2.size:
        raise ValueError("As imagens devem ter o mesmo tamanho")
    return Image.blend(image1, image2, alpha)

def merge_channels(red, green, blue):

    if red.mode != 'L' or green.mode != 'L' or blue.mode != 'L':
        raise ValueError("Todos os canais devem estar em modo grayscale ('L')")
    return Image.merge('RGB', (red, green, blue))
