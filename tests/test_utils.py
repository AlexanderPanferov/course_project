from utils import utils


def test_completed_operation():
    assert utils.completed_operation(
        [{"id": 441945886, "state": "EXECUTED"}, {"id": 594226727, "state": "CANCELED"}]) == [
               {"id": 441945886, "state": "EXECUTED"}]

