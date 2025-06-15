import os
from PIL import Image
from image_package.processing.combination import blend_images, merge_channels
from image_package.processing.transformation import resize, rotate
from image_package.utils.io import load_image, save_image, batch_process
from image_package.utils.plot import plot_images, plot_histogram

def process_single_image(input_path, output_path):
    """Pipeline de processamento para uma única imagem"""
   
    img = load_image(input_path)
    
 
    processed = [
        img,
        resize(img, width=300), 
        rotate(img, 45),         
        blend_images(            
            img, 
            Image.new('RGB', img.size, (200, 150, 100)),
            alpha=0.3
        )
    ]
    
  
    plot_images(
        processed,
        titles=["Original", "Redimensionada", "Rotacionada", "Efeito Sépia"],
        ncols=2,
        figsize=(12, 8)
    )
    
    
    plot_histogram(processed[0], "Histograma Original")
    plot_histogram(processed[-1], "Histograma Processado")
    
 
    save_image(processed[-1], output_path)

def batch_processing_example():
    """Exemplo de processamento em lote"""
    input_dir = "examples/assets/input_photos"
    output_dir = "examples/assets/output_processed"
    
    
    def custom_processor(img):
        img = resize(img, width=800)
        img = rotate(img, 5)
        return img
    
    # Processar todas as imagens
    batch_process(
        input_dir=input_dir,
        output_dir=output_dir,
        process_function=custom_processor,
        extension="jpg"
    )

if __name__ == "__main__":
    # Processar imagem única
    process_single_image(
        input_path="examples/assets/input.jpg",
        output_path="examples/assets/output/processed.jpg"
    )
    