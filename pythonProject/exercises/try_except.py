import logging


def try_except():
    produce_error = 10 * (1/0)


try:
    try_except()
except Exception as e:
    print("Error is caught: ", e)
    logging.exception("CHECK LOGS!!!!")
