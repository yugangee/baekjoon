import sys

input = sys.stdin.readline

N = int(input())
cards = {}
card_get = list(map(int, input().split()))

for num in card_get:
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

M = int(input())
card_find = list(map(int, input().split()))

for number in card_find:
    print(cards.get(number, 0),end=" ")