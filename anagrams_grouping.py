from collections import defaultdict
res = defaultdict(list)
words  = "car, acr, bat, tab, get, cat".split(", ")



def group(words):
    res = dict()
    for w in words:
        sorted_word = "".join(sorted(w))
        try:
            res[sorted_word].add(w) # append operation for set
        except KeyError:
            res[sorted_word] = {w} # adding it in a set as asked for test cases
    print(list(res.values()))
    return list(res.values())


import unittest

class AnagramGroupTest(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(group(['abc']), [{'abc'}])

    def test_too_many(self):
        words = ['restrain', 'retrains', 'skate', 'stake', 'strainer', 'steak', 'terrains', 'teaks', 'trainers']
        self.assertEqual(group(words), [{'strainer', 'restrain', 'retrains', 'trainers', 'terrains'}, {'skate', 'teaks', 'stake', 'steak'}])

if __name__ == "__main__":
    unittest.main()


