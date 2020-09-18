from PIL import Image
from brickify import EditedImage, PieceList, RenderedImage
from defaults.palettes import all
from defaults.pieces import medium



im = Image.open('output/barack.jpg')

new_im = im.resize((2000, 2000))

new_im.save('for_imgur.jpg')

exit()

IMAGE = 'barack.jpg'
INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'

SIZE = (96, 96)

im = Image.open(INPUT_PATH + IMAGE)


edited = EditedImage(image = im).edit_image(size = SIZE, palette = all)
pieces = PieceList(image = edited).generate_medium(pieces = medium)
render = RenderedImage(piece_list = pieces, size = SIZE).render_image()


render.save(OUTPUT_PATH + IMAGE)
