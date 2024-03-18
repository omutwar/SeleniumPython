import pytest
from utils.report_utils import setup_report


@pytest.fixture(scope='session', autouse=True)
def setup_report_fixture():
    # set up the report directory and environment variable
    setup_report()
