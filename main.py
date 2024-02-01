
from full_dec.full_decoration import logger
from dec.decoration_1 import logger
from collections import Counter

@logger
def vote(votes):
	# your code
    counter = Counter()
    for integer in votes:
        counter[integer] += 1

    often_meets_number = max(counter, key=counter.get)
    # print(f"Часто встречается число: {often_meets_number}")
    return often_meets_number
