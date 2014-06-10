# -*- coding: utf-8 -*-
"""
Clone of 2048 game.
"""

# import poc_2048_gui

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
    hemos_sumado = False
    while hemos_hecho_algun_cambio:
        hemos_hecho_algun_cambio = False
        working_line = list(good_line)
        for i in range(1, imax + 1):

            primera_celda_llena = i - 1
            for j in range(i - 1, -1, -1):
                if good_line[j] == 0:
                    primera_celda_llena = j - 1
            if i > 1:
                ultima_celda_vacia = primera_celda_llena +1
            else:
                ultima_celda_vacia = -1
            if ultima_celda_vacia != -1:
                working_line[ultima_celda_vacia] = good_line[i] # movemos la celda
                working_line[i] = 0 # ponemos un cero en la celda que hemos dejado vacía
                hemos_hecho_algun_cambio = True
            good_line = list(working_line)
        # Vamos a sumar si procede
        if not hemos_sumado:
            working_line = list(good_line)
            for i in range(1, imax + 1):
                if good_line[i] == good_line[i - 1]:
                    # Procede sumar
                    working_line[i - 1] = good_line[i - 1] + good_line[i]
                    working_line[i] = 0
                    hemos_hecho_algun_cambio = True
                    hemos_sumado = True
                good_line = working_line
    return good_line


line_in = [2, 0, 2, 4]
line_out = merge(line_in)
print
print line_in
print line_out
print
print '---------'
