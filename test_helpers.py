#Unit testing with pytest

import pytest
from mypackage.helpers import calculate_average, get_grade, greet
from pydantic import ValidationError

from pydantic_demo import ExamResult

def test_calculate_average():

    assert calculate_average([80, 90, 100]) == 90.0


def test_empty_marks():

    assert calculate_average([]) == 0.0


@pytest.mark.parametrize(
    "score, expected_grade",
    [
        (85, "Grade B"),
        (95, "Grade A"),
        (75, "Grade C"),
        (40, "Fail!")
    ]
)

def test_get_grade(score, expected_grade):

    assert get_grade(score) == expected_grade


def test_exam_result_invalid_score():

    with pytest.raises(ValidationError):
        ExamResult(student_name="Hamza", score=150)