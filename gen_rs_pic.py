# petit code qui génère les 2 images pour le resting state
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors

img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
img.save(f"img/img_fond_noir.png")


# Draw a white cross
WHITE = (255, 255, 255, 0)

draw = ImageDraw.Draw(img)
draw.line((11*img.size[0]/24, img.size[1]/2, 13*img.size[0]/24, img.size[1]/2), fill=WHITE, width=5)
draw.line((img.size[0]/2, img.size[1]/2 - img.size[0]/24, img.size[0]/2, img.size[1]/2 + img.size[0]/24), fill=WHITE, width=5)

img.save(f"img/img_croix_blanche.png")
