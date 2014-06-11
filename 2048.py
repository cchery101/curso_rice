# -*- coding: utf-8 -*-
"""
Clone of 2048 game.
"""

# import poc_2048_gui
from random import randint
import poc_testsuite_for_2048

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    imax = len(line) - 1
    good_line = list(line) # because tmp_line should be a real new list
    hemos_hecho_algun_cambio = True
    hemos_terminado_de_sumar = False
    hemos_sumado = False
    while hemos_hecho_algun_cambio:
        hemos_hecho_algun_cambio = False
        working_line = list(good_line)
        for i in range(1, imax + 1):
            if good_line[i] != 0:
                primera_celda_llena = i - 1
                for j in range(i - 1, -1, -1):
                    if good_line[j] == 0:
                        primera_celda_llena = j - 1
                if i > 1 and (i - primera_celda_llena) > 1:
                    ultima_celda_vacia = primera_celda_llena +1
                else:
                    ultima_celda_vacia = -1
                if ultima_celda_vacia != -1:
                    working_line[ultima_celda_vacia] = good_line[i] # movemos la celda
                    working_line[i] = 0 # ponemos un cero en la celda que hemos dejado vacía
                    hemos_hecho_algun_cambio = True
                else:
                    if good_line[1] != 0 and good_line[0] == 0:
                        working_line[0] = good_line[1] # movemos la celda en 1
                        working_line[1] = 0 # ponemos un cero en la celda 1
                        hemos_hecho_algun_cambio = True
                good_line = list(working_line)
        # Vamos a sumar si procede
        if not hemos_terminado_de_sumar:
            working_line = list(good_line)
            for i in range(1, imax + 1):
                if good_line[i] == good_line[i - 1]:
                    # Procede sumar
                    working_line[i - 1] = good_line[i - 1] + good_line[i]
                    working_line[i] = 0
                    hemos_hecho_algun_cambio = True
                    hemos_sumado = True
                    if hemos_sumado and i == imax:
                        hemos_terminado_de_sumar = True
                good_line = working_line
            if hemos_sumado and i == 3:
                        hemos_terminado_de_sumar = True
    return good_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()

    def change_col(self, col_number, new_col):
        """
       Cambia una columna en el grid
        """
        for i in range(self._grid_height):
            self._grid[i][col_number] = new_col[i]
        # print 'antes = ', antes
        # print
        # print 'despues = ', self._grid
        return

    def change_row(self, row_number, new_row):
        """
        Cambia una fila en el grid
        """
        self._grid[row_number] = new_row

        return

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self._grid = [[0 for col in range(self._grid_width)] for row in range(self._grid_height)]

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = '\n'
        for i in range(self._grid_height):
            result = result + str(self._grid[i]) + '\n'
        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        fils = []
        for i in range(self._grid_height):
            fils.append(self._grid[i])
        transpose_grid = zip(*self._grid)
        cols = []
        for i in range(self._grid_width):
            cols.append(transpose_grid[i])
        # print
        # print 'fils = ', fils
        # print 'cols = ', cols
        # print
        tira = []

        if direction == 'UP':
            for i in range(self._grid_width):
                tira.append(cols[i])

            # Sustituimos las tiras antiguas por las mergeadas
            # print ' Vamos a sustituir la tira antigua por la tira mergeada'
            # antes = deepcopy(list(self._grid))
            antes = [list(inner_list) for inner_list in self._grid]
            for i in range(self._grid_width):

                # print ' antes = ', self
                self.change_col(i, merge(tira[i]))
                # print
                # print 'Cambiamos la tira ', i
                # print
                # print 'despues de UP = ', self

            # despues = deepcopy(list(self._grid))
            despues = [list(inner_list) for inner_list in self._grid]
            if antes == despues:
                pass
            else:
                self.new_tile()
            # print ' despues de new_tile = ', self
            return


        elif direction == 'DOWN':
            for i in range(self._grid_width):
                tira.append(cols[i][::-1])
            # Sustituimos las tiras antiguas por las mergeadas
            print ' Vamos a sustituir la tira antigua por la tira mergeada'
            # antes = deepcopy(list(self._grid))
            antes = [list(inner_list) for inner_list in self._grid]
            for i in range(self._grid_width):

                print ' antes = ', self
                tmp1 = merge(tira[i])
                tmp2 = tmp1[::-1]
                self.change_col(i, tmp2)
                # print
                # print 'Cambiamos la tira ', i
                # print
                # print 'despues de DOWN = ', self
            # despues = deepcopy(list(self._grid))
            despues = [list(inner_list) for inner_list in self._grid]
            if antes == despues:
                pass
            else:
                self.new_tile()
            # print ' despues de new_tile = ', self
            return
        if direction == 'LEFT':
            for i in range(self._grid_height):
                tira.append(fils[i])
            # Sustituimos las tiras antiguas por las mergeadas
            # print ' Vamos a sustituir la tira antigua por la tira mergeada'
            # antes = deepcopy(list(self._grid))
            antes = [list(inner_list) for inner_list in self._grid]
            for i in range(self._grid_height):

                # print ' antes = ', self
                self.change_row(i, merge(tira[i]))
                # print
                # print 'Cambiamos la tira ', i
                # print
                # print 'despues de LEFT = ', self
            # despues = deepcopy(list(self._grid))
            despues = [list(inner_list) for inner_list in self._grid]
            if antes == despues:
                pass
            else:
                self.new_tile()
            # print ' despues de new_tile = ', self
            return
        elif direction == 'RIGHT':
            for i in range(self._grid_height):
                tira.append(fils[i][::-1])

            # Sustituimos las tiras antiguas por las mergeadas
            print ' Vamos a sustituir la tira antigua por la tira mergeada'
            # antes = deepcopy(list(self._grid))
            antes = [list(inner_list) for inner_list in self._grid]
            for i in range(self._grid_height):

                # print ' antes = ', self
                tmp1 = merge(tira[i])
                tmp2 = tmp1[::-1]
                self.change_row(i, tmp2)
                # print
                # print 'Cambiamos la tira ', i
                # print
                # print 'despues de RIGHT = ', self
            # despues = deepcopy(list(self._grid))
            despues = [list(inner_list) for inner_list in self._grid]
            if antes == despues:
                pass
            else:
                self.new_tile()
            # print ' despues de new_tile = ', self
            return


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        cero_tiles = []
        for i in range(self._grid_height):
            for j in range(self._grid_width):
                if self._grid[i][j] == 0:
                    cero_tiles.append((i, j))
        num_ceros = len(cero_tiles)
        random_tupla = randint(0, num_ceros - 1)
        random_cero_tile = cero_tiles[random_tupla]
        if randint(1, 10) == 1:
            two_or_four = 2
        else:
            two_or_four = 4
        self.set_tile(random_cero_tile[0], random_cero_tile[1], two_or_four)
        return


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

poc_testsuite_for_2048.run_test(merge)


a = TwentyFortyEight(7, 4)
print a

a.set_tile(3, 1, 1)
print a
print a.get_tile(3, 1)

print '+++++++++++++++'
for i in range(14):
    a.new_tile()

print a
print
print '******************** Move ***************'
print 'UP'
a.move('UP')

print 'DOWN'
a.move('DOWN')


print 'LEFT'
a.move('LEFT')


print 'RIGHT'
a.move('RIGHT')


print
print 'prueba del merge caso especial'
print
line = [8, 16, 16, 8]
print line
print merge(line)
