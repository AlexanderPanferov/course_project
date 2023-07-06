from utils import utils


def test_completed_operation():
    assert utils.completed_operation(
        [{"id": 441945886, "state": "EXECUTED"},
         {"id": 594226727, "state": "CANCELED"}]) == [{"id": 441945886, "state": "EXECUTED"}]


def test_sort_date():
    assert utils.sort_date(
        [{'date': '2017-08-24'},
         {'date': '2013-07-26'},
         {'date': '2019-04-13'},
         {'date': '2018-08-26'},
         {'date': '2019-08-26'},
         {'date': '2021-04-18'}]) == \
           ['2021-04-18', '2019-08-26', '2019-04-13', '2018-08-26', '2017-08-24']
    assert utils.sort_date(
        [{'date': '2017-08-24'},
         {'date': '2013-07-26'},
         {'date': '2019-04-13'}]) == ['2019-04-13', '2017-08-24', '2013-07-26']

