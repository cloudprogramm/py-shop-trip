import datetime

from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import MagicMock


from app.main import shop_trip


def test_shop_trip_output(monkeypatch):
    datetime_mock = MagicMock(wrap=datetime.datetime)
    datetime_mock.now.return_value = datetime.datetime(2020, 3, 11, 13, 15, 34)
    monkeypatch.setattr(datetime, "datetime", datetime_mock)

    f = StringIO()

    with redirect_stdout(f):
        shop_trip()

    output = f.getvalue()
    out = '''Bob has 55 dollars
Bob's trip to the Outskirts Shop costs 28.24
Bob's trip to the Shop '24/7' costs 31.52
Bob's trip to the Central Shop costs 39.34
Bob rides to Outskirts Shop

Date: 11/03/2022 13:15:34
Thanks, Bob, for you purchase!
You have bought: 
4 milks for 12 dollars
2 breads for 2 dollars
5 butters for 12.5 dollars
Total cost is 26.5 dollars
See you again!

Bob rides home
Bob now has 26.76 dollars

Alex has 41 dollars
Alex's trip to the Outskirts Shop costs 17.18
Alex's trip to the Shop '24/7' costs 15.96
Alex's trip to the Central Shop costs 17.98
Alex rides to Shop '24/7'

Date: 11/03/2022 13:15:34
Thanks, Alex, for you purchase!
You have bought: 
2 milks for 4 dollars
2 breads for 3.0 dollars
2 butters for 6.4 dollars
Total cost is 13.4 dollars
See you again!
Alex rides home
Alex now has 25.04 dollars

Monica has 12 dollars
Monica's trip to the Outskirts Shop costs 15.64
Monica's trip to the Shop '24/7' costs 16.8
Monica's trip to the Central Shop costs 22.52
Monica doesn't have enough money to make purchase in any shop
'''
    assert output == out

