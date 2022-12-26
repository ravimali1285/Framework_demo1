import pytest
@pytest.mark.parametrize("num,result",[(1,11),(2,22),(4,44)])
def test_calculate(num, result):
    assert 11*num == result
    print("test passed")