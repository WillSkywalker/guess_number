#1/usr/bin/env python

import random


class GuessNumber(object):

    def __init__(self, length=4, lives=16):

        self.length = length
        self.lives = lives
        self.reset()


    def guess(self, numbers):
        numbers = map(int, numbers)
        if self.lives <= 0:
            self.lose = True
            return 'lose'
        elif numbers == self.answer:
            return 'win'
        else:
            a, b = 0, 0
            for i in xrange(4):
                if self.answer[i] == numbers[i]:
                    a += 1
                elif numbers[i] in self.answer:
                    b += 1
            self.lives -= 1
            return a, b


    def reset(self):
        pool = set([1,2,3,4,5,6,7,8,9])
        self.answer = []
        for i in xrange(self.length):
            num = random.choice(tuple(pool))
            self.answer.append(num)
            pool -= set([num])
        


def main():
    gameplay = GuessNumber()
    r = -1, -1
    while r not in ('win', 'lose'):
        if r != (-1, -1):
            print '%dA%dB' % r
        r = gameplay.guess(map(int, list(raw_input('Input 4 numbers: '))))
    print 'You %s!' % r




if __name__ == '__main__':
    main()
