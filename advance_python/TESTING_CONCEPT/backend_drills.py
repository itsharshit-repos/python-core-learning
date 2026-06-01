from dataclasses import dataclass

@dataclass
class User:
    id: str
    name: str
    email: str
    is_active: bool
    plan: str
    credits: int

def get_users() -> list[User]:
    return [
        User(id="u1", name="Aman", email="aman@gmail.com", is_active=True, plan="free", credits=10),
        User(id="u2", name="Riya", email="riya@gmail.com", is_active=False, plan="pro", credits=50),
        User(id="u3", name="Kabir", email="kabir@gmail.com", is_active=True, plan="pro", credits=5),
        User(id="u4", name="Meera", email="meera@gmail.com", is_active=True, plan="free", credits=0)
    ]

def get_user_names() -> list[str]:
    users = get_users()
    user_name = [user.name for user in users]
    return user_name
    
# Expected output names: ["Aman", "Kabir", "Meera"]
def get_active_users() -> list[User]:
    users = get_users()
    return [user for user in users if user.is_active]

def count_pro_users() -> int:
    users = get_users()
    count = 0
    for user in users:
        if user.plan == 'pro':
            count += 1
    return count

def find_user_by_id(user_id: str) -> User | None:
    users = get_users()
    for user in users:
        if user.id == user_id:
            return user
    return None

# Expected output names: ["Kabir", "Meera"]
def get_users_with_low_credits(limit: int) -> list[User]:
    users = get_users()
    return [user for user in users if user.credits < limit]

def add_credits_to_user(user_id: str, amount: int) -> User | None:
    users = get_users()
    for user in users:
        if user.id == user_id:
            user.credits += amount
            return user
    return None

def build_user_summary() -> dict[str, int]:
    users = get_users()

    total_count = 0
    active_count = 0
    pro_count = 0
    free_count = 0
    
    for user in users:
        total_count += 1
        if user.is_active:
            active_count += 1
        if user.plan == "pro":
            pro_count += 1
        if user.plan == "free":
            free_count += 1

    return {
        "total_users": total_count,
        "active_users": active_count,
        "pro_users": pro_count,
        "free_users": free_count,
    }

def main() -> None:
    print(f"User names: {get_user_names()}")
    print(f"Active user names: {[user.name for user in get_active_users()]}")
    print(f"Number of PRO users: {count_pro_users()}")
    print(find_user_by_id("u2"))
    print(find_user_by_id("u99"))
    print(f"User with low credit: {[user.name for user in get_users_with_low_credits(10)]}")
    print(f"Credits added! New credit: {add_credits_to_user('u1', 20)}")
    print(build_user_summary())

if __name__ == "__main__":
    main()