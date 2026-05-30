# Testing means I write code that checks my code automatically

# A function has a contract:
def add(a: int, b: int) -> int:
    return a + b
# Test checks whether the contract is true:
def test_add() -> None:
    assert add(2,3) == 5
# This is the whole idea. Testing is not a seperate subject. Testing is how you prove your functions behave as promised.
# "Assert" means "This must be True, If not True, fail the test."

