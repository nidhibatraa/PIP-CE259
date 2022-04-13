'''NAME : Nidhi Batra
   ID   : 20CE002
'''
N = int(input())

captain_R = map(int, input().split())
captain_R= sorted(captain_R)

for i in range(len(captain_R)):
    if(i != len(captain_R)-1):
        if(captain_R[i]!=captain_R[i-1] and captain_R[i]!=captain_R[i+1]):
            print(captain_R[i])
            break;
    else:
        print("Captain's room number :",captain_R[i])

