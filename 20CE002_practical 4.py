n=int(input()) 
scores=list(map(int,input().split(" "))) 
scores = sorted(scores) 
score_set = set(scores) 
Max_score = max(score_set) 
score_set.remove(Max_score) 
Max_score = max(score_set) 
secong maximum number of that set
print(Max_score)