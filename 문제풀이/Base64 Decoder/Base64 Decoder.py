import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1,T+1):
     base_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0' ,'1', '2', '3', '4', '5', '6', '7', '8', '9', '+', "/"]
     word = input()
     word_list = []
     print("#", end="")
     print(tc, end=" ")
     for i in range(len(word)):
         num = base_list.index(word[i])
         num2 = bin(num)[2:]
         while len(num2) != 6:
             num2 = "0" + num2
         word_list.append(num2)
         res = "".join(word_list)

     res_list = ""
     for i in range(len(res)//8):
         res2 = ((res[0+i*8:8+i*8]))
         res_list+=(chr(int(res2,2)))
     print(res_list)







