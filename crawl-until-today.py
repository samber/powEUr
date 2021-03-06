
from datetime import datetime, timedelta

from entsoe.mappings import DOMAIN_MAPPINGS

from crawler import generation
from errors import handle_errors

# Data available on API Start 01/01/2015
now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
date = datetime(2015, 1, 1).replace(hour=0, minute=0, second=0, microsecond=0)

while date < now:
    for country_code in DOMAIN_MAPPINGS.keys():
        print("Getting generation data: {} / {}".format(country_code, date))
        handle_errors(lambda: generation(date, country_code))
    date += timedelta(days=1)
