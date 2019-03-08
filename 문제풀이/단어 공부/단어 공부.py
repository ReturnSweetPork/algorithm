import sys
sys.stdin = open('input.txt', 'r')

word = input()
word2 = word.upper()


no_word = {}
for i in word2:
    if i not in no_word:
        no_word[i] =1
    else:
        no_word[i] += 1

arr_key = (list(no_word.keys()))
arr_value = (list(no_word.values()))
maxv = max(arr_value)
idx = arr_value.index(maxv)
if arr_value.count(maxv) != 1:
    print("?")
else:
    print(arr_key[idx])