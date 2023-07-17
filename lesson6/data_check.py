import argparse
from datetime import datetime

def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description='Check date.')
parser.add_argument('date', type=str, help='Date to check in the format YYYY-MM-DD')

args = parser.parse_args()

print(validate_date(args.date))