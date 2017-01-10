from contextlib import contextmanager
from io import StringIO
import sys

import pytest
from maxsum.main.main import main

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestMaxSum:
    def test_empty(self):
        with pytest.raises(SystemExit):
            main([])

    def test_max(self):
        with captured_output() as (out, err):
            main(['1','2','3'])
        output = out.getvalue().strip()
        assert output == "The max is: 3"

    def test_sum(self):
        with captured_output() as (out, err):
            main(['--sum','1','2','3'])
        output = out.getvalue().strip()
        assert output == "The sum is: 6"
