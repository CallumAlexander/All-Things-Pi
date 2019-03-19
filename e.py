import math
from decimal import getcontext
import decimal
import time

actual = decimal.Decimal(0)
actual = 2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274

getcontext().prec = 100

end = 5000
e = 0
k= 0

while k < end:
    
    term = 1 / decimal.Decimal( math.factorial( k ) )
    e += decimal.Decimal(term)
    print('Term : ' + str(k))
    k += 1
    
print(str(e))
accuracy = abs(decimal.Decimal(actual) - decimal.Decimal(e))
print('accuracy : ' + str(accuracy))
