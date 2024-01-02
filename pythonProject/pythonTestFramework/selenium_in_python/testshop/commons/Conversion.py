from datetime import datetime
from dateutil.parser import parse

class Conversion:
    def convert_date(input_date):
        # parse date
        d = parse(input_date)
        # reformat date
        return d.strftime('%m/%d/%Y')
