from PIL import Image

def gradient():
    pixels = []
    for x in range (255):
        for y in range (255):
            pixels.append((x%25, x%25, x%112))

    newim = Image.new("RGB", (255,255))
    newim.putdata(pixels)
    return newim

gradient().show()
gradient().save("gradient.jpg")
