from PIL import Image 
import matplotlib
matplotlib.use('Agg')
import os

def image_info(image):

    info = {
        'format': image.format,
        'mode': image.mode,
        'size': image.size,
        'width': image.width,
        'height': image.height
    }

    # Imagens com paleta modo 'P'
    if image.mode == 'P' and hasattr(image, 'palette'):
        info['palette'] = image.palette.mode 
    else:
        info['palette'] = None

    return info    

    # Adiciona palette para imagens indexadas
    if hasattr(image, 'palette'):
        info['palette'] = image.palette.mode if image.palette  else None   
    else:
        info['palette'] = None

    return info 

def load_image(image_path):

    try:
        return Image.open(image_path)
    except Exception as e: 
        raise ValueError(f"Erro ao carregar imagem: {str(e) }")   

def save_image(image, output_path, quality=95):

    if not isinstance(image, Image.Image):
        raise TypeError("O objeto deve ser uma imagem PIL")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path, quality=quality)    

def batch_process(input_dir, output_dir, process_function, extension="jpg"): 

    if not os.path.exists(output_dir):
        os.makedirs(output_dir) 

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(extension):
            input_path = os.path.join(input_dir, filename)
            output_dir = os.path.join(output_dir, filename) 

            try: 
                img = load_image(input_path)
                processed = process_function(img)
                save_image(processed, output_path)
            except Exception as e:
                print(f"Erro processando {filename}: {str(e) }") 
