
'''
deck = ((r,s) for s in '♥♦♠♣' for r in range(1,14))

Current Output:
print(deck)>>>
<generator object <genexpr> at 0x7f7aaa2bac80>

Correct Output:
print(deck)>>>
[(1, '♥'),(2, '♥'),(3, '♥'),(4, '♥'),(5, '♥'),(6, '♥'),(7, '♥'), (8, '♥'), (9, '♥'), (10, '♥'), (11, '♥'), (12, '♥'), (13, '♥'), 
(1, '♦'),(2, '♦'),(3, '♦'),(4, '♦'),(5, '♦'),(6, '♦'),(7, '♦'), (8, '♦'), (9, '♦'), (10, '♦'), (11, '♦'), (12, '♦'), (13, '♦'), 
(1, '♠'),(2, '♠'),(3, '♠'),(4, '♠'),(5, '♠'),(6, '♠'),(7, '♠'), (8, '♠'), (9, '♠'), (10, '♠'), (11, '♠'), (12, '♠'), (13, '♠'), 
(1, '♣'),(2, '♣'),(3, '♣'),(4, '♣'),(5, '♣'),(6, '♣'),(7, '♣'), (8, '♣'), (9, '♣'), (10, '♣'), (11, '♣'), (12, '♣'), (13, '♣')]'''

deck = [(r,s) for s in '♥♦♠♣' for r in range(1,14)]
print(deck)


things = []
for i in range(5):
    print(2*(i)+1)