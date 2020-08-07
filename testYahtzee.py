import unittest
from functools import reduce

from Die import Die


class Yahtzee():
    def __init__(self):
        self.chosen = ()
        self.d1 = Die(6)
        self.d2 = Die(6)
        self.d3 = Die(6)
        self.d4 = Die(6)
        self.d5 = Die(6)
        self.cup_of_dice = [self.d1, self.d2, self.d3, self.d4, self.d5]
        self.choices = {"Yahtzee": False, "Chance": False,
                        "Large Straight": False, "Small Straight": False,
                        "Ones": False, "Twos": False, "Threes": False, "Fours": False,
                        "Fives": False, "Sixes": False, "Three of a Kind":False,
                        "Four of a Kind":False, "Full House":False,"Small Straight":False,
                        "Large Straight":False}
        self.total = 0

    def scores(self, numbers):
        d = {}
        sum = reduce(lambda a,b:a+b,numbers)
        if numbers.count(numbers[0]) == 5
            d["Yahtzee"] = 50
        else:
            d["Yahtzee"] = 0
        d["Ones"] = numbers.count(1)
        d["Twos"] = numbers.count(2) * 2
        d["Threes"] = numbers.count(3) * 3
        d["Fours"] = numbers.count(4) * 4
        d["Fives"] = numbers.count(5) * 5
        d["Sixes"] = numbers.count(6) * 6
        d["Chance"] = sum

        if self.three_of_a_kind(numbers):
            d["Three of a Kind"] = sum
        else:
            d["Three of a Kind"] = 0

        if self.four_of_a_kind(numbers):
            d["Four of a Kind"] = sum
        else:
            d["Four of a Kind"] = 0

        if self.full_house(numbers):
            d["Full House"] = 25
        else:
            d["Full House"] = 0

        if self.small_straight(numbers):
            d["Small Straight"] = 30
        else:
            d["Small Straight"] = 0

        if self.large_straight(numbers):
            d["Large Straight"] = 40
        else:
            d["Large Straight"] = 0

        return (d)

    def three_of_a_kind(self,numbers):
        for n in numbers:
            if numbers.count(n) >= 3:
                return True
        return False

    def four_of_a_kind(self,numbers):
        for n in numbers:
            if numbers.count(n) >= 4:
                return True
        return False

    def full_house(self,numbers):
        for n in numbers:
            if numbers.count(n)==2:
                for n2 in numbers:
                    if numbers.count(n2)==3:
                        return True
        return False

    def small_straight(self,numbers):
        numbers.sort()
        if numbers[:4]==[1,2,3,4] or numbers[:4]==[2,3,4,5]:
            return True
        return False

    def large_straight(self,numbers):
        numbers.sort()
        if numbers == [1,2,3,4,5] or numbers == [2,3,4,5,6]:
            return True
        return False

    def score(self, numbers):
        a = numbers.count(numbers[0])
        if a == 5:
            return 50
        else:
            return numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
        # figure out if numbers which is a list of 5 numbers between 1 and 6
        # if they are all the same and return 50 if that is the case
        # if not, return the sum of all the numbers

    def roll(self):
        if len(self.chosen) == 0:
            for v in self.chosen:
                self.cup_of_dice[v].active = True
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice
        else:
            for v in self.chosen:
                self.cup_of_dice[v].active = False
            rolled_dice = [self.d1.roll(), self.d2.roll(), self.d3.roll(), self.d4.roll(), self.d5.roll()]
            return rolled_dice

    def select(self, choice):
        self.chosen = choice

    def choose(self, key, myroll):
        if key == "Yahtzee":
            if myroll.count(myroll[0]) != 5:
                return False
        if self.choices[key]:
            return False
        else:
            self.choices[key] = True
            self.total = self.total + self.scores(myroll)[key]
            return True


class MyTestCase(unittest.TestCase):
    def test_yahtzee(self):
        self.game = Yahtzee()

    def test_roll(self):
        self.game = Yahtzee()
        values = self.game.roll()
        self.assertEqual(5, len(values))

    def test_die(self):
        d = Die(6)
        v = d.roll()
        self.assertGreater(v, 0)
        self.assertLess(v, 7)

    def test_select(self):
        self.game = Yahtzee()
        values = self.game.roll()
        print(values)
        self.game.select((0, 1))
        new_values = self.game.roll()
        print(new_values)
        self.assertEqual(values[0], new_values[0])
        self.assertEqual(values[1], new_values[1])

    def test_choose(self):
        self.game = Yahtzee()
        values = [1, 1, 1, 1, 1]
        self.assertFalse(self.game.choose("Yahtzee", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Yahtzee", values))
        self.assertFalse(self.game.choose("Yahtzee", values))
        self.assertTrue(self.game.choose("Chance", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Chance", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Large Straight", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Large Straight", [1, 2, 3, 4, 5]))
        self.assertTrue(self.game.choose("Small Straight", [1, 2, 3, 4, 5]))
        self.assertFalse(self.game.choose("Small Straight", [1, 2, 3, 4, 5]))

    def test_score(self):
        self.game = Yahtzee()
        dict = self.game.scores([1, 1, 1, 1, 1])
        self.assertTrue(dict['Yahtzee'] == 50)
        self.assertTrue(dict['Ones'] == 5)
        self.assertTrue(dict['Twos'] == 0)
        self.assertTrue(dict['Threes'] == 0)
        self.assertTrue(dict['Fours'] == 0)
        self.assertTrue(dict['Fives'] == 0)
        self.assertTrue(dict['Sixes'] == 0, f"{dict['Sixes']}")
        self.assertTrue(dict['Chance'] == 5)
        self.assertTrue(dict['Three of a Kind'] == 5)
        self.assertTrue(dict['Four of a Kind'] == 5)
        self.assertTrue(dict['Full House'] == 0)
        self.assertFalse(dict['Small Straight'] == 30)
        self.assertFalse(dict['Large Straight'] == 40)

    def test_scores(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.scores([1,2,3,4,5])["Large Straight"]==40)

    def test_three_of_a_kind(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.three_of_a_kind([1,1,1,2,3]))
    def test_four_of_a_kind(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.four_of_a_kind([1,1,1,1,3]))
    def test_full_house(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.full_house([1,1,1,2,2]))
    def test_small_straight(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.small_straight([1,2,3,4,6]))
    def test_large_straight(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.large_straight([1,2,3,4,5]))

    def test_total(self):
        self.game = Yahtzee()
        self.assertTrue(self.game.total == 0)
        self.game.choose("Full House",[1,1,1,2,2])
        self.assertTrue(self.game.total == 25)




if __name__ == '__main__':
    unittest.main()
