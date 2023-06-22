class Node:

  def __init__(self, rn, rc, td):
    self.rn = rn
    self.rc = rc
    self.td = td
    self.parent = None  # parent
    self.color = 1
    self.left = None
    self.right = None
    self.mpointer = None

  def print_color(self):
    if self.color == 0:
      return '(b)'
    return '(r)'

