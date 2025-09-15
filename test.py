from .__main__ import generate_password, log_password_generation, DEFAULT_PASSWORD_LOG_FILE


def test_generate_password():
    lengths = [1, 5, 100, 1_000_000]
    for length in lengths:
        pwd = generate_password(length)
        assert len(pwd) == length

    
def test_log_password_generation():
    password = generate_password()
    log_password_generation(password)
    with open(DEFAULT_PASSWORD_LOG_FILE, "r") as file:
        data = file.read()
        assert password in data

    


