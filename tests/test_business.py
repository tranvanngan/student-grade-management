import pytest
from unittest.mock import Mock, patch
from src.business import add_grade, calculate_average_score
from src.models import Grade

# Fixture cho một grade mẫu
@pytest.fixture
def sample_grade():
    return Grade(id=1, student_id=1, subject_id=101, score=8.5)

# ------------------- Test add_grade -------------------
def test_add_grade_valid_score():
    with patch('src.business.get_student_by_id', return_value=Mock(id=1)) as mock_student, \
         patch('src.business.get_subject_by_id', return_value=Mock(id=101)) as mock_subject, \
         patch('src.business.data_add_grade') as mock_add_grade:
        
        add_grade(1, 101, 7.5)
        mock_add_grade.assert_called_once()
        # Kiểm tra đối tượng Grade được truyền vào
        args, _ = mock_add_grade.call_args
        grade_obj = args[0]
        assert grade_obj.student_id == 1
        assert grade_obj.subject_id == 101
        assert grade_obj.score == 7.5

def test_add_grade_invalid_score_below_zero():
    with patch('src.business.get_student_by_id', return_value=Mock()), \
         patch('src.business.get_subject_by_id', return_value=Mock()):
        with pytest.raises(ValueError, match="Điểm phải nằm trong khoảng 0 đến 10"):
            add_grade(1, 101, -1)

def test_add_grade_invalid_score_above_ten():
    with patch('src.business.get_student_by_id', return_value=Mock()), \
         patch('src.business.get_subject_by_id', return_value=Mock()):
        with pytest.raises(ValueError, match="Điểm phải nằm trong khoảng 0 đến 10"):
            add_grade(1, 101, 11)

def test_add_grade_student_not_exists():
    with patch('src.business.get_student_by_id', return_value=None):
        with pytest.raises(ValueError, match="Học sinh với id 999 không tồn tại"):
            add_grade(999, 101, 5.0)

def test_add_grade_subject_not_exists():
    with patch('src.business.get_student_by_id', return_value=Mock()), \
         patch('src.business.get_subject_by_id', return_value=None):
        with pytest.raises(ValueError, match="Môn học với id 999 không tồn tại"):
            add_grade(1, 999, 5.0)

# ------------------- Test calculate_average_score -------------------
def test_calculate_average_no_grades():
    with patch('src.business.get_grades_by_student', return_value=[]):
        assert calculate_average_score(1) == 0.0

def test_calculate_average_with_one_grade():
    # Giả sử get_grades_by_student trả về list of tuples: (id, student_id, subject_id, score)
    grades_data = [(1, 1, 101, 9.0)]
    with patch('src.business.get_grades_by_student', return_value=grades_data), \
         patch('src.business.get_subject_credits', return_value=3):  # môn 101 có 3 tín chỉ
        avg = calculate_average_score(1)
        assert avg == 9.0  # (9*3)/3 = 9

def test_calculate_average_with_multiple_grades():
    grades_data = [
        (1, 1, 101, 9.0),   # môn 101, 3 tín chỉ
        (2, 1, 102, 7.0),   # môn 102, 2 tín chỉ
    ]
    def mock_credits(subject_id):
        if subject_id == 101:
            return 3
        elif subject_id == 102:
            return 2
        return 0
    with patch('src.business.get_grades_by_student', return_value=grades_data), \
         patch('src.business.get_subject_credits', side_effect=mock_credits):
        avg = calculate_average_score(1)
        # (9*3 + 7*2) / (3+2) = (27+14)/5 = 41/5 = 8.2
        assert avg == 8.2

def test_calculate_average_rounding():
    grades_data = [(1, 1, 101, 8.3333)]
    with patch('src.business.get_grades_by_student', return_value=grades_data), \
         patch('src.business.get_subject_credits', return_value=3):
        avg = calculate_average_score(1)
        assert avg == 8.33  # làm tròn 2 chữ số