# from package.module import func
from toto.matemagics import super_sum, super_sub

def test_super_sum():
  assert super_sum(2,2) == 6
  assert super_sum(1,7) == 10
  
def test_super_sub():
  assert super_sub(2,2) == -3
  assert super_sub(1,7) == -9