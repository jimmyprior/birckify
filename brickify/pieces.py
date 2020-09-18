from PIL import Image

class PieceList:
    def __init__(self, image):
        self.image = image
        self.buy_guide = []


    def try_piece(self, location, piece_size):
        '''Checks Whether Or Not A Piece Will Fit'''
        x,y = location #top left corner of piece
        length, width = piece_size #length is the horizontal, width is the vertical
        color = self.image_list[y][x]

        if self.image_list[y][x:x+length].count(color) < length:
            return(False)

        for row in range(y, y + width):
          for column in range(x, x + length):
              if (column, row) not in self.coordinates:
                  return(False)

        for row in self.image_list[y : y + width]:
          if row[x : x + length].count(color) != length:
            return(False)

        for row in range(y, y + width):
          for column in range(x, x + length):
            self.coordinates.remove((column, row))

        self.directions.append([color, location, piece_size])
        return(True)


    def create_image_matrix(self):
        '''Converts The Image RGB Values To a Matrix'''
        self.image_list = []
        size = self.image.size
        prod = size[0] * size[1]
        image_list = []
        for i in range(0, prod, size[0]):
            self.image_list.append(list(self.image.getdata())[i:i+size[0]])


    def create_coordinates(self):
        '''Creates A List Of Coordinates Of Not Occupied Spots'''
        self.coordinates = []
        for row in range(len(self.image_list)):
            for column in range(len(self.image_list[0])):
                self.coordinates.append((column, row))


    def generate_medium(self, pieces):
        '''Creates a Piece List That Is Somewhat Optimized'''
        self.create_image_matrix()
        self.directions = []
        self.create_coordinates()

        while len(self.coordinates) != 0:
            placement = self.coordinates[0]
            for piece in pieces:
                part = self.try_piece(placement, piece)
                if part:
                    break

        return(self.directions)


    def generate_slow(self, pieces):
        '''Creates A Piece List Using The Biggest Pieces When Possible'''
        self.create_image_matrix()
        self.directions = []
        self.create_coordinates()

        for piece in pieces:
            for place in self.coordinates.copy():
                self.try_piece(place, piece)

        return(self.directions)


    def generate_fast(self):
        '''Creates a Piece List of All 1x1 Bricks'''
        self.create_image_matrix()
        self.directions = []
        self.create_coordinates()

        piece = (1, 1)

        for cords in self.coordinates.copy():
            self.try_piece(cords, piece)

        return(self.directions)


    def generate_buy_info(self):

        '''Generates A List Of How Many of Each Part Will Be Needed In Each Color'''
        pass
