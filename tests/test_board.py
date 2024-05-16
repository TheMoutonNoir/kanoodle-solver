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

def test_can_place():

    #setup kanoodle board
    size_y, size_x = 11, 5
    b_obj_test = Board(size_y, size_x)
    test_piece = Piece(Noodle.A.value)

    #Execute function
    result = b_obj_test.can_place(test_piece, 0, 0)
    fail = b_obj_test.can_place(test_piece, 10,0)

    assert result
    assert fail == False

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

# def test_remove_piece():

#     #setup kanoodle board
#     size_y, size_x = 11, 5
#     b_obj_test = Board(size_y, size_x)
#     test_piece = Piece(Noodle.A.value)

#     #Expected result board
#     b_template = np.full((size_x, size_y), ".", dtype=str)
    
#     #Execute function
#     b_obj_test.place_piece(test_piece, 0, 0)
#     b_obj_test.remove_piece()

def test_possible_placements():

    #setup kanoodle board
    size_y, size_x = 11, 5
    b_obj_test = Board(size_y, size_x)
    test_piece = Piece(Noodle.C.value)

    #Expected result
    expect_arr = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]

    #Execute function
    result = b_obj_test.find_possible_placements(test_piece)
    
    #Assert
    assert np.array_equal(result, expect_arr)

