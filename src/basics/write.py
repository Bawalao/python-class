with open('chipotle.txt', 'w') as f:
    print('This is my chipotle order!', file=f)
    print('I want a burrito!', file=f)
    print('With brown rice, no beans!', file=f)
    print('Half chicken half steaaaak!', file=f)

import sys
print('This is a terrible error!', file=sys.stderr)
