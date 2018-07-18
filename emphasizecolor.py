from PIL import Image

def load_img():
    im = Image.open("balloon.jpg", mode='r')
    return im

def show_img():
    new_img = emphasize()
    new_img.show()

def save_img():
    new_img = emphasize()
    new_img.save("specialballoon.jpg", format=None)

def emphasize():
    im = load_img()
    data = list(im.getdata())
    new_img = []

    for pixel in data:
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        avg = int((r+g+b)/3)
        if g > b:
            new_img.append((pixel[0], pixel[1], pixel[2]))
        else:
            new_img.append((avg, avg, avg))


    newim = Image.new("RGB", im.size)
    newim.putdata(new_img)
    return newim
