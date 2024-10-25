#This tests from the math file; checks if all exquations work between the number file
from equations import(
    add,
    sub,
    mul,
    div
)

def test_add():
    assert add(2,10) == 12
    assert add(3,5) == 8
    assert add(4,6) == 10

def test_sub():
    assert sub(5,3) == 2
    assert sub(6,2) == 4
    assert sub(12,1) == 11

def test_mul():
    assert mul(2,3) == 6
    assert mul(7,8) == 56
    assert mul(4,5) == 20

def test_div():
    assert div(10,5) == 2
    assert div(40,8) == 5
    assert div(144,12) == 12