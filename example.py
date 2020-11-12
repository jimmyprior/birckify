from PIL import Image
from brickify import EditedImage, PieceList, RenderedImage
from defaults.palettes import all   #use the default lego color palette 
from defaults.pieces import medium #use medium piece sizes 


IMAGE = 'barack.jpg'
INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'

SIZE = (96, 96)   # each pixel will be treated as a (1x1) lego brick

im = Image.open(INPUT_PATH + IMAGE)   # open the image

edited = EditedImage(image = im).edit_image(size = SIZE, palette = all) #resize the image and recolor it to the lego colors
pieces = PieceList(image = edited).generate_medium(pieces = medium)  #use medium sized pieces and generate with medium speed. 
#Medium speed is not optimized to fit the biggest piece when possible. 
#use the generate_slow method if you're looking for optimization.
#use the generate_fast method if you're looking for speed.  

render = RenderedImage(piece_list = pieces, size = SIZE).render_image() #render the piecelist into a visual form. 

render.save(OUTPUT_PATH + IMAGE) #save the render you created. 
