import sample_mod
import random
from PIL import  Image

my_image = Image.open("kermit.png")
#pic.show()


#sample mods
#sample_mod.my_print()
#sample_mod.my_print2()


#my_image = Image.new(mode="RGB",size=(10,10),color=(0,0,0))
def My_image():
    rows = my_image.size[0]
    cols = my_image.size[1]
    print(rows, cols)

    px = my_image.load()
    for i in range(0, rows):

        start = random.randint(0, rows)
        end = random.randint(0, cols)
        nub = random.randint(1, 5)

        if i % 2 == 0:
            start = 0
        else:
            start = i

        for j in range(start,cols,nub):
            red = random.randint(0,0)
            green = random.randint(255,255)
            blue = random.randint(0,0)
            px[i,j] = (red, green, blue)

    my_image.show()