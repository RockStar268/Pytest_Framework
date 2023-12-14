import logging

def test_my_first_one():
    dutch_welcome_text = "Welcome"
    english_welcome_text = "welcome"
    try:
        assert dutch_welcome_text == english_welcome_text, f"Given value are not equal! Actual value should be '{dutch_welcome_text}'"
    except Exception as e:
        print("Error is caught: ", e)
        logging.exception("CHECK LOGS!!!!")

    practice_try_except_1 = "Welcome"
    practice_try_except_2 = "Welcome"
    assert practice_try_except_1 == practice_try_except_2, f"Given value are not equal! Actual value should be '{practice_try_except_1}'"



def test_my_second_one():
    dutch_welcome_text1 = "Welcome"
    english_welcome_text1 = "Welcome"
    assert dutch_welcome_text1 == english_welcome_text1, f"Given value are not equal! Actual value should be '{dutch_welcome_text1}'"


