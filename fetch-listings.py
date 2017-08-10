import requests
import datetime
import sys

start_date = datetime.date(2017, 7, 7)
end_date = datetime.date(1999, 12, 31)
day = datetime.timedelta(1)

BASE_URL = "http://sheriff.boco.solutions/JailListingsArchive/JailListing_Export_{date}.xlsx"

def fetch_date(date):
    date_str = date.strftime('%Y%m%d')
    date_fn = date.strftime('%Y-%m-%d')
    url = BASE_URL.format(date=date_str)
    r = requests.get(url)

    if not r.ok:
        print(date_str)
        print(r.status_code)
        raise Exception

    with open('raw-listings/{}.xlsx'.format(date_fn), 'wb') as out:
        out.write(r.content)

if __name__ == "__main__":
    date = start_date
    while date > end_date:
        fetch_date(date)
        date -= day

        if date.day == 7:
            print('W', end='')
        else:
            print('.', end='')

        sys.stdout.flush()
        break
