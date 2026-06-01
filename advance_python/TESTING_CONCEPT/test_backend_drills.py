from backend_drills import get_user_names, get_active_users, count_pro_users, find_user_by_id, get_users_with_low_credits, add_credits_to_user, build_user_summary, User

def test_get_user_names() -> None:
    assert get_user_names() == ["Aman", "Riya", "Kabir", "Meera"]

def test_count_active_users() -> None:
    users = get_active_users()
    assert len(users) == 3

def test_get_active_users() -> None:
    users_name = [user.name for user in get_active_users()]
    assert users_name == ["Aman", "Kabir", "Meera"] 

def test_count_pro_users() -> None:
    assert count_pro_users() == 2

def test_find_user_by_id() -> None:
    user = find_user_by_id("u2")
    assert user is not None
    assert user.name == "Riya"
    assert user.plan == "pro"
    assert user.credits == 50

def test_find_missing_user() -> None:
    user = find_user_by_id("u99")
    assert user is None

def test_low_credit_user() -> None:
    low_credit_user = [user.name for user in get_users_with_low_credits(10)]
    assert low_credit_user == ["Kabir", "Meera"]

def test_add_credit_to_existing_user() -> None:
    user = add_credits_to_user('u1', 20)
    assert user is not None
    assert user.name == "Aman"
    assert user.credits == 30

def test_add_credits_to_missing_user() -> None:
    user = add_credits_to_user('u99', 20)
    assert user is None

def test_build_user_summary() -> None:
    assert build_user_summary() == {
    "total_users": 4,
    "active_users": 3,
    "pro_users": 2,
    "free_users": 2
}