from PIL import Image, ImageDraw
blank_image = Image.new('RGBA', (400, 300), 'white')
img_draw = ImageDraw.Draw(blank_image)
img_draw.rectangle((70, 50, 270, 200), outline='red', fill='blue')
img_draw.text((70, 250), 'Hello World', fill='green')
blank_image.show()