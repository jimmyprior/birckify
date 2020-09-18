from PIL import Image, ImageDraw, ImageOps

class RenderedImage:
    def __init__(self, piece_list, size):
        self.piece_list = piece_list
        self.size = size
        self.part_size = (50,50)
        self.circle_size = (35,35)
        #maybe an image thing here too?

    def render_piece(self, color):
        '''Renders A 1x1 Piece Of A Given Color'''
        bx, by = self.part_size
        cx, cy = self.circle_size
        circle = (bx/2 - cx/2, by/2 - cy/2, bx/2 + cx/2, by/2 + cy/2)
        part_im = Image.new('RGB', self.part_size, color)
        draw = ImageDraw.Draw(part_im)
        draw.ellipse(circle, outline='black')

        return(part_im)


    def render_brick(self, color, size):
        '''Renders A Brick Made Of 1x1 Pieces of A Given Color'''
        part_im = self.render_piece(color)
        p_length, p_width = size

        im_height = p_width * self.part_size[1]
        im_width = p_length * self.part_size[1]

        piece_im = Image.new('RGB', (im_width, im_height))

        for x in range(p_length):
            for y in range(p_width):
              piece_im.paste(im=part_im, box=(x*self.part_size[1], y* self.part_size[0]))

        height, width = piece_im.size
        p_border = piece_im.resize((height-2, width-2))
        piece_im = ImageOps.expand(p_border, border=1, fill='black')

        return(piece_im)


    def render_image(self):
        rows = self.size[1] * self.part_size[1]
        columns = self.size[0] * self.part_size[0]
        final = Image.new('RGB', (columns, rows))

        for piece in self.piece_list:
            piece_render = self.render_brick(piece[0], piece[2])
            x,y = piece[1]
            final.paste(im=piece_render, box=(x*self.part_size[0], y*self.part_size[1]))

        return(final)
