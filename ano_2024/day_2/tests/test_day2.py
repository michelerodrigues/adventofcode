import pytest
from day_2.day2 import *

@pytest.fixture
def test_file():
    test_file = os.path.abspath('day_2/tests/input-test-day2.txt')
    print("test_file = ", test_file)
    return test_file


@pytest.fixture
def test_reports():
    test_reports = {
        0: {
            'levels': ['7','6','4','2','1']
        },
        1: {
            'levels': ['1','2','7','8','9']
        },
        2: {
            'levels': ['9','7','6','2','1']
        },
        3: {
            'levels': ['1','3','2','4','5']
        },
        4: {
            'levels': ['8','6','4','4','1']
        },
        5: {
            'levels': ['1','3','6','7','9']
        },
        6: {
            'levels': ['1','3','6','7','9','8']
        },
        7: {
            'levels': ['25', '25', '26', '29', '31', '32', '39', '39']
        },
        8: {
            'levels': ['64', '64', '65', '66', '67']
        }
        
    }
    return test_reports


@pytest.fixture
def test_reports_updated():
    test_reports_updated = {
        0: {
            'levels': ['7','6','4','2','1'],
            'safe': False,
            'order': None
        },
        1: {
            'levels': ['1','2','7','8','9'],
            'safe': False,
            'order': None
        },
        2: {
            'levels': ['9','7','6','2','1'],
            'safe': False,
            'order': None
        },
        3: {
            'levels': ['1','3','2','4','5'],
            'safe': False,
            'order': None
        },
        4: {
            'levels': ['8','6','4','4','1'],
            'safe': False,
            'order': None
        },
        5: {
            'levels': ['1','3','6','7','9'],
            'safe': False,
            'order': None
        },
        6: {
            'levels': ['1','3','6','7','9','8'],
            'safe': False,
            'order': None
        },
        7: {
            'levels': ['25', '25', '26', '29', '31', '32', '39', '39'],
            'safe': False,
            'order': None
        },
        8: {
            'levels': ['64', '64', '65', '66', '67'],
            'safe': False,
            'order': None
        }
    }
    return test_reports_updated


@pytest.fixture
def test_reports_ordered():
    test_reports_ordered = {
        0: {
            'levels': ['7','6','4','2','1'],
            'safe': False,
            'order': 'decrease'
        },
        1: {
            'levels': ['1','2','7','8','9'],
            'safe': False,
            'order': 'increase'
        },
        2: {
            'levels': ['9','7','6','2','1'],
            'safe': False,
            'order': 'decrease'
        },
        3: {
            'levels': ['1','3','2','4','5'],
            'safe': False,
            'order': None
        },
        4: {
            'levels': ['8','6','4','4','1'],
            'safe': False,
            'order': None
        },
        5: {
            'levels': ['1','3','6','7','9'],
            'safe': False,
            'order': 'increase'
        },
        6: {
            'levels': ['1','3','6','7','9','8'],
            'safe': False,
            'order': None
        },
        7: {
            'levels': ['25', '25', '26', '29', '31', '32', '39', '39'],
            'safe': False,
            'order': None
        },
        8: {
            'levels': ['64', '64', '65', '66', '67'],
            'safe': False,
            'order': None
        }
    }
    return test_reports_ordered


@pytest.fixture
def test_reports_checked():
    test_reports_checked = {
        0: {
            'levels': ['7','6','4','2','1'],
            'safe': True,
            'order': 'decrease'
        },
        1: {
            'levels': ['1','2','7','8','9'],
            'safe': False,
            'order': 'increase'
        },
        2: {
            'levels': ['9','7','6','2','1'],
            'safe': False,
            'order': 'decrease'
        },
        3: {
            'levels': ['1','3','2','4','5'],
            'safe': False,
            'order': None
        },
        4: {
            'levels': ['8','6','4','4','1'],
            'safe': False,
            'order': None
        },
        5: {
            'levels': ['1','3','6','7','9'],
            'safe': True,
            'order': 'increase'
        },
        6: {
            'levels': ['1','3','6','7','9','8'],
            'safe': False,
            'order': None
        },
        7: {
            'levels': ['25', '25', '26', '29', '31', '32', '39', '39'],
            'safe': False,
            'order': None
        },
        8: {
            'levels': ['64', '64', '65', '66', '67'],
            'safe': False,
            'order': None
        }
    }
    return test_reports_checked


def test_load_file(test_file, test_reports):
    reports = {}

    reports = load_file(test_file)
    print("reports = ", reports)
    print("test_reports = ", test_reports)
    assert reports == test_reports


def test_update_data(test_reports, test_reports_updated):
    reports_updated = update_data(test_reports)
    assert reports_updated == test_reports_updated


def test_set_report_order(test_reports_updated, test_reports_ordered):
    reports_updated = set_report_order(test_reports_updated)
    assert reports_updated == test_reports_ordered


def test_check_adjacent_levels(test_reports_ordered, test_reports_checked):
    reports_checked = check_adjacent_levels(test_reports_ordered)
    assert reports_checked == test_reports_checked


def test_count_safe_reports(test_reports_checked):
    count = count_safe_reports(test_reports_checked)
    assert count == 2