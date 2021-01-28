
def validate_user_input(n):
        if n >= 0:
            return True
        else:
            return False

def test_variable_user_input():
    assert validate_user_input(100) == True
    assert validate_user_input(-100) == False
    assert validate_user_input(0) == True
    assert validate_user_input(5.5) == True
    assert validate_user_input("hi") == False