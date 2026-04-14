import pytest
from unittest.mock import patch
from src.business import add_grade, calculate_average_score

def test_add_grade_valid_score():
    with patch('src.data_access.get_student_by_id', return_value=(1, 'An', 16)), \
         patch('src.data_access.get_subject_by_id', return_value=(1, 'Toan', 3)), \
         patch('src.data_access.add_grade') as mock_add:
        add_grade(1, 1, 7.5)
        mock_add.assert_called_once()

def test_add_grade_invalid_score():
    with patch('src.data_access.get_student_by_id', return_value=(1, 'An', 16)), \
         patch('src.data_access.get_subject_by_id', return_value=(1, 'Toan', 3)):
        with pytest.raises(ValueError):
            add_grade(1, 1, -1)
        with pytest.raises(ValueError):
            add_grade(1, 1, 11)

def test_calculate_average_no_grades():
    with patch('src.data_access.get_grades_by_student', return_value=[]):
        assert calculate_average_score(1) == 0.0

def test_calculate_average_with_grades():
    grades = [(1, 1, 1, 9.0), (2, 1, 2, 7.0)]
    def mock_credits(subj_id):
        return 3 if subj_id == 1 else 2
    with patch('src.data_access.get_grades_by_student', return_value=grades), \
         patch('src.data_access.get_subject_credits', side_effect=mock_credits):
        assert calculate_average_score(1) == 8.2