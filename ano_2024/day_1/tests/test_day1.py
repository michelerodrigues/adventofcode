import pytest
from day_1.day1 import *

@pytest.fixture
def test_file():
    test_file = os.path.abspath('day_1/tests/input_test_day1.txt')
    return test_file


@pytest.fixture
def location_id_1():
    return [3,4,2,1,3,3]


@pytest.fixture
def location_id_2():
    return [4,3,5,3,9,3]


@pytest.fixture
def distances():
    return [2,1,0,1,2,5]


@pytest.fixture
def appearance():
    return [3,1,0,0,3,3]


@pytest.fixture
def similarity():
    return [9,4,0,0,9,9]



def test_load_file(test_file):
    col1 = []
    col2 = []

    col1, col2 = load_file(test_file)
    
    assert col1 == [3,4,2,1,3,3]
    assert col2 == [4,3,5,3,9,3]


def test_load_no_file():
    test_file = ""
    col1, col2 = load_file(test_file)

    assert col1 == []
    assert col2 == []


def test_file_not_found():
    test_file = "/invalid/path/file.txt"
    col1, col2 = load_file(test_file)

    assert col1 == []
    assert col2 == []


def test_invalid_file():
    test_file = os.path.abspath('day_1/day1.py')
    col1, col2 = load_file(test_file)

    assert col1 == []
    assert col2 == []


def test_order_lists(location_id_1, location_id_2):
    location_id_1, location_id_2 = order_lists(location_id_1, location_id_2)

    assert location_id_1 == [1,2,3,3,3,4]
    assert location_id_2 == [3,3,3,4,5,9]


def test_calculate_distance_apart(location_id_1, location_id_2):
    location_id_1.sort()
    location_id_2.sort()
    distances = calculate_distance_apart(location_id_1, location_id_2)
    
    assert distances == [2,1,0,1,2,5]


def test_sum_distances(distances):
    final_result = sum_distances(distances)
    assert final_result == 11


def test_location_appearance(location_id_1, location_id_2):
    appearance = define_appearance_at_left_list(location_id_1, location_id_2)
    assert appearance == [3,1,0,0,3,3]


def test_calculate_similarity(location_id_1, appearance):
    similarity = calculate_similarity(location_id_1, appearance)
    assert similarity == [9,4,0,0,9,9]


def test_calculate_score(similarity):
    score = calculate_score(similarity)
    assert score == 31