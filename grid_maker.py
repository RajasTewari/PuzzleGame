from PIL import Image

# open image
def grid_maker(image_file):
    img = Image.open(image_file)
    width, height = img.size

# creating the array with 9 pieces (3x3 grid)
    pieces = []
    for i in range(3):
        for j in range(3):
            # for loops to iterate through row and column 3 times (0 to 2)
            # understand that left will go 0 to 1/3 to 2/3, right will go 1/3 to 2/3 to 1
            # same logic applies to top/bot
            left = i * (width / 3)
            top = j * (height / 3)
            right = (i + 1)  * (width / 3)
            bot = (j + 1) * (height / 3)
            # adding each cropped element to the list
            pieces += [img.crop((left, top, right, bot))]

    return pieces