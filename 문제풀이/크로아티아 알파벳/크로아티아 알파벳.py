import sys
sys.stdin = open('input.txt', 'r')

word = input()
org_word_list=[]
for r in range(len(word)):
    org_word_list.append(word[r])

word_list = []
for i in reversed(range(len(word))):
    if word[i] == "=":
        if word[i-1] == "z":
            if word[i-2] =="d":
                word_list.append(word[i-2]+word[i-1]+word[i])
            else:
                word_list.append(word[i - 1] + word[i])
        elif word[i-1] == "c" or word[i-1] == "s":
             word_list.append(word[i - 1] + word[i])

    elif word[i] == "-":
        if word[i-1] == 'c' or word[i-1] == 'd':
            word_list.append(word[i - 1] + word[i])
        # else:
        #     word_list.append(word[i])
    elif word[i] == "j":
        if word[i-1] == "n" or word[i-1] == "l":
            word_list.append(word[i-1] + word[i])
    #     else:
    #         word_list.append(word[i])
    # else:
    #     word_list.append(word[i])

new_word_list = []
for j in word_list:
    for k in j:
        new_word_list.append(k)

# print(org_word_list)
# print(new_word_list)

for l in new_word_list:
    org_word_list.remove(l)

#
# print(org_word_list)
# print(len(word_list))
# print(len(org_word_list))
res = len(word_list) + len(org_word_list)
print(res)

