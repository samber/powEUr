
import os
from datetime import timedelta, datetime

from entsoe import EntsoePandasClient
import pandas as pd

from output import to_json_file

client = EntsoePandasClient(api_key=os.environ['ENTSOE_API_KEY'])


def generation(date, country_code):
    end = date + timedelta(days=1, minutes=-1)
    if end > datetime.now():
        end = datetime.now() - timedelta(minutes=1)

    ts_start = pd.Timestamp(date, tz='UTC')
    ts_end = pd.Timestamp(end, tz='UTC')

    data = client.query_generation(
        country_code=country_code,
        start=ts_start,
        end=ts_end,
        psr_type=None,
    )

    # replace by null value
    data.dropna(inplace=True)

    # write json to file
    filename = date.strftime("%Y-%m-%d") + '.json'
    directory = './data/generation/' + country_code
    os.makedirs(directory, exist_ok=True)
    to_json_file(directory + '/' + filename, data.to_json(orient='index'))
