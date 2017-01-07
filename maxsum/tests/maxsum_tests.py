from ..main import main

from contextlib import contextmanager
from io import StringIO
from nose.tools import *
import sys

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

@raises(SystemExit)
def test_empty():
    main.main([])

def test_max():
    with captured_output() as (out, err):
        main.main(['1','2','3'])
    output = out.getvalue().strip()
    eq_(output, "The max is: 3")

def test_sum():
    with captured_output() as (out, err):
        main.main(['--sum','1','2','3'])
    output = out.getvalue().strip()
    eq_(output, "The sum is: 6")
