from . import __main__


def test_generate_default_password_length():
    __main__.DISABLE_PASSWORD_LOGGING = True
    pwd = __main__.generate_password()
    assert isinstance(pwd, str)
    assert len(pwd) == __main__.DEFAULT_PASSWORD_LENGTH


def test_generate_password():
    __main__.DISABLE_PASSWORD_LOGGING = True
    lengths = [1, 5, 100, 1_000_000]
    for length in lengths:
        pwd = __main__.generate_password(length)
        assert isinstance(pwd, str)
        assert len(pwd) == length

    
def test_log_password_generation():
    password = __main__.generate_password()
    __main__.log_password_generation(password)
    with open(__main__.DEFAULT_PASSWORD_LOG_FILE, "r") as file:
        data = file.read()
        assert password in data

    


