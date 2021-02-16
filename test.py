from dll_node import DLLNode
from sll_node import SLLNode

d = DLLNode(1)
d2 = DLLNode(2)
d3 = DLLNode(3)

d3.set_next(d2)
d3.set_previous(d)

print(d3.get_next(), d3.get_previous())