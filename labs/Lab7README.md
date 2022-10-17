# Lab 7
I used the Pillow package for my plugin.

In this script I will show you how to change the colors of your image, add a watermark, and make the image spooky.

Download any image from the internet and save it to your computor.

To begin this code will change the rgb of the image:

```python
from PIL import Image
image = Image.open("image/path/cat.jpg")
r, g, b = image.split()
image = Image.merge("RGB", (b, g, r))
image.show()
```

After doing the image.show() you should see your image with different colors.

Next the code will add a watermark to the bottom right of the image:

```python
from PIL import Image, ImageDraw, ImageFont

im = Image.open('image/path/cat.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "sample watermark"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

margin = 10
x = width - textwidth - margin
y = height - textheight - margin

draw.text((x, y), text, font=font)
im.show()
im.save('image/path/watermark.jpg')
```
The image should have text saying sample watermark or whatever you put instead of that in the bottom right.

Finally, to make the image spooky.

All the code is doing is adding one of the image filters known as FIND_EDGES to the image to darken the image:

```python
from PIL import Image, ImageFilter
from PIL.ImageFilter import FIND_EDGES

img = Image.open('image/path/cat.jpg')
img1 = img.filter(FIND_EDGES)
img1.save('image/path/SpookyCat.jpg')
img1.show()
```

Those are the three uses of the Pillow plugin
