import pytest
from scripts.utils import helper_function

# Test for utility function
def test_helper_function(capsys):
    helper_function()
    captured = capsys.readouterr()
    assert captured.out.strip() == "This is a utility function."
