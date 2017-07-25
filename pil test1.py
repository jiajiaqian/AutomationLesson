from PIL import Image

im = Image.open('3.jpg')
#im.show()
out = im.resize((8, 8))  # resize image with high-quality
out.show()
out.save('3test.png', 'png')

