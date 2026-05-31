from logic_drills import get_student_names, get_passed_students, count_failed_students, find_student, get_topper_name

def test_get_student_names() -> None:
    assert get_student_names() == ["Aman","Riya","Kabir"]

def test_get_passed_students() -> None:
    assert get_passed_students() == ["Aman","Kabir"]

def test_count_failed_students() -> None:
    assert count_failed_students() == 1

def test_find_student_riya() -> None:
    result = find_student("Riya")
    assert result is not None
    assert result.name == "Riya"
    assert result.marks == 35

def test_find_student_unknown() -> None:
    result = find_student("Unknown")
    assert result is None

def get_topper_name_kabir() -> None:
    assert get_topper_name() == "Kabir"