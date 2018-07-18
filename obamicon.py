# Rename this file to be "filters.py"
# Add commands to import modules here.

from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img():
    im = Image.open("catguy.jpg", mode='r')
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img():
    new_img = obamicon()
    new_img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img():
    new_img = obamicon()
    new_img.save("improvedcat.jpg", format=None)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon():
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue=(112,150,158)
    yellow=(252,227,166)
    im = load_img()
    data = list(im.getdata())
    new_img = []

    for pixel in data:
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        intensity = r + g + b
        if intensity < 182:
            new_img.append(darkBlue)
        elif intensity < 364:
            new_img.append(red)
        elif intensity < 546:
            new_img.append(lightBlue)
        if intensity > 546:
            new_img.append(yellow)

    newim = Image.new("RGB", im.size)
    newim.putdata(new_img)
    return newim
