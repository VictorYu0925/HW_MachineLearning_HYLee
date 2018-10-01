from PIL import Image, ImageFilter

img = Image.open('/westbrook.jpg')

### (2)透過load()將圖片載入到記憶體
### load()會將圖片載入到記憶體，並回傳一個Pixel Access Object
### 透過載入圖片到內存，使得操作比起putpixel / getpixel 來的快很多

pixel = img.load()

for x in range(img.size[0]):
	for y in range(img.size[1]):
		r, g, b = pixel[x, y]
		pixel[x,y] = (int(r/2), int(g/2), int(b/2)) 

img.save('/faded.jpg')
img.show()



