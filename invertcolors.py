from PIL import Image

def load_img():
    im = Image.open("haunted.jpg", mode='r')
    return im

def show_img():
    new_img = invert()
    new_img.show()

def save_img():
    new_img = invert()
    new_img.save("invertedhouse.jpg", format=None)

def invert():
    im = load_img()
    data = list(im.getdata())
    new_img = []

    for pixel in data:
        new_img.append((255-pixel[0], 255-pixel[1], 255-pixel[2]))

    newim = Image.new("RGB", im.size)
    newim.putdata(new_img)
    return newim
