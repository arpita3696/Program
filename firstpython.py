import urllib.request
from PIL import Image



urllib.request.urlretrieve(
    'https://images.fineartamerica.com/images-medium-large-5/san-francisco-bay-nasascience-photo-library.jpg',
    'bay.jpg')
img=Image.open('bay.jpg')
img.save("bay.jpg")
