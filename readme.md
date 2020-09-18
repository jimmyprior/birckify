# Brickify
Turn images into lego mosaics.

![Image](https://i.imgur.com/VIYIDvW.jpg)
![Image](https://i.imgur.com/khnmNje.jpg)

![Image](https://i.imgur.com/SYeWct7.jpg)
![Image](https://i.imgur.com/nnQjNlF.jpg)

![Image](https://i.imgur.com/gfM48BY.jpg)
![Image](https://i.imgur.com/cvr5wff.jpg)

## Example
### Code Sample
```python
from PIL import Image
from brickify import EditedImage, PieceList, RenderedImage
from defaults.palettes import all
from defaults.pieces import medium

IMAGE = 'barack.jpg'
INPUT_PATH = 'input/'
OUTPUT_PATH = 'output/'

SIZE = (96, 96)

im = Image.open(INPUT_PATH + IMAGE)


edited = EditedImage(image = im).edit_image(size = SIZE, palette = all)
pieces = PieceList(image = edited).generate_medium(pieces = medium)
render = RenderedImage(piece_list = pieces, size = SIZE).render_image()

render.save(OUTPUT_PATH + IMAGE)
```

### Image Output
![Image](https://i.imgur.com/51iLYTm.jpg)
