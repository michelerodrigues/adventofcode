import day1

def test_day1():
    password = day1.find_password("test_day1.txt")
    print("Password = ", password)
    assert password == 3