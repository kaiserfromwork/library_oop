def test_user_creation(sample_user):
    assert sample_user.name == "John"
    assert sample_user.surname == "Doe"


def test_get_user_id(sample_user):
    user_id = sample_user.get_user_id()
    assert isinstance(user_id, str)
    assert len(user_id) == 64


def test_display_user(sample_user):
    display = sample_user.display_user()
    assert "John" in display
    assert "Doe" in display


def test_student_user(student_user):
    assert student_user.faculty == "Computer Science"
    display = student_user.display_student()
    assert "Computer Science" in display


def test_staff_user(staff_user):
    assert staff_user.position == "Director"
    display = staff_user.display_staff()
    assert "Director" in display

