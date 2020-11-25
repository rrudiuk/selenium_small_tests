def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    try:
        assert expected_result == actual_result
    except AssertionError:
        print(f"expected {expected_result}, got {actual_result}")

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    try:
        assert substring in full_string
    except AssertionError:
        print(f"expected '{substring}' to be substring of '{full_string}'")

if __name__ == "__main__":
    test_input_text()
    test_substring()
    print("All tests passed!")