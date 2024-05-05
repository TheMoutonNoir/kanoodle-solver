import pytest
from board import Board
from piece import Piece
from noodle import Noodle
import numpy as np

def test_init():
    
    #setup kanoodle board
    size_y, size_x = 11, 5
    b_obj_test = Board(size_y, size_x)

    #Expected result board
    b_template = np.full((size_x, size_y), ".", dtype=str)
    
    #Assert
    assert np.array_equal(b_obj_test.board, b_template)

def test_place_piece():

    #setup kanoodle board
    size_y, size_x = 11, 5
    b_obj_test = Board(size_y, size_x)
    test_piece = Piece(Noodle.A.value)

    #Expected result board
    b_template = np.full((size_x, size_y), ".", dtype=str)
    b_template[0][1] = b_template[1][1] = b_template[2][0] = b_template[2][1] = 'A'

    #Execute function
    b_obj_test.place_piece(test_piece, 0, 0)

    #Assert
    assert np.array_equal(b_obj_test.board, b_template)
