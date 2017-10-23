from PIL import Image,ImageFilter
im=Image.open('test.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.convert('RGB').save('filterT.jpeg')