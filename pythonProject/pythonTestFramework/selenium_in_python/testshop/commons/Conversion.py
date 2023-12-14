from datetime import datetime


class Conversion:
    def date_of_birth(self, date_of_birth):
        try:
            # Parse the input date_of_birth string into a datetime object
            dob_date = datetime.strptime(date_of_birth, '%m/%d/%Y')
            return dob_date
        except ValueError:
            # If there is a ValueError, the date format is incorrect
            print("Invalid date format. Please use the format 'YYYY-MM-DD'.")
            return None
