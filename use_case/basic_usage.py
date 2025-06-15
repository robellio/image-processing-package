from src.image_package import load_image, blend_images, plot_image
from src.image_package.processing.transformation import resize

img1 = load_image("image1.jpg")
img2 = load_image("image2.jpg")

img2 = resize(img2, width=img1.width, height=img1.height)

result = blend_images(img1, img2, alpha=0.7)

plot_image(result, title="Imagem Combinada")