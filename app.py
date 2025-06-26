import numpy as np
from PIL import Image

image = Image.open('./apple.jpg')
image = np.array(image)

# ITU-R BT.601 표준, GRAY = R*0.299 + G*0.587 + B*0.114
gray_image = 0.299 * image[:, :, 0] + 0.587 * image[:, :, 1] + 0.114 * image[:, :, 2]
gray_image = gray_image.astype(np.uint8)

gray_image_pil = Image.fromarray(gray_image)
gray_image_pil.save('to_gray.jpg')
