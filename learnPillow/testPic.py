from PIL import Image
im=Image.open('test.jpg')
#im2=Image.open('test.jpg').convert('RGB').save('new.jpeg')
w,h=im.size
print("Original size:%s %s" %(w,h))
im.thumbnail((w//2,h//2))
print("Resize image: %s %s" %(w//2,h//2))
#im.save("thumbnail.jpg","jpeg")
im.convert('RGB').save('nail.jpeg')
