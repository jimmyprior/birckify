from PIL import Image

class EditedImage:
    def __init__(self, image):
        self.image = image


    def resize(self, size):
        '''Resizes the image to the desired lego size'''
        self.image = self.image.resize(size)


    def recolor(self, palette):
        '''Changes the colors to the closest color in the given color palette'''

        pixels = list(self.image.getdata())
        size = self.image.size

        palette_pixels = []
        for pixel in pixels:
          compare = []
          for color in palette:
            x = [abs(pixel[i] - color[i]) for i in range(len(color))]
            compare.append(sum(x))
          palette_pixels.append(palette[compare.index(min(compare))])


        image = Image.new('RGB', size)
        image.putdata(palette_pixels)
        self.image = image

    def edit_image(self, palette, size):
        self.resize(size)
        self.recolor(list(palette.keys()))
        return(self.image)
