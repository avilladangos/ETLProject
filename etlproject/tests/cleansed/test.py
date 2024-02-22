import pytest
from scripts.etl_script import etl_process

# Test for ETL process
def test_etl_process():
    input_data = [1, 2, 3, 4]
    expected_output = [2, 4, 6, 8]
    assert etl_process(input_data) == expected_output
