'''
    You will only be writing code in this file and this is the only file submitted to the autograder.
'''

def get_version():
    
    
    '''
        print the version of python that you are using.
    '''
    "*** WRITE YOUR CODE HERE ***"
    import sys
    s= sys.version.split()
    return s[0]


def alternative_sum(start,n):
    '''
        modify the function to return a list with generated by an alternative sum sequence explained in the assignment handout
    '''
    "*** WRITE YOUR CODE HERE ***"
    
    
    if start < 0 or not (5<=n<=20):
        return []
    l=[start]
    while len(l)<n:
        if len(l)<3:
            l.append(l[-1]+l[-1])
        else:
            new=l[-1]+l[-3]
            l.append(new)
    return l 

'''
        read the files scores.csv in the data directory and return the list of names sorted in ascending order of the scores.
    '''
import csv
def order_scores():
    path='data/scores.csv'
    pairs=[]
    with open(path,'r') as f:
        scores_CSV = csv.reader(f)
        next(scores_CSV)
    
        for row in scores_CSV:
            name,score=row
            pairs.append((name, int(score)))
    s_pairs=sorted(pairs,key=lambda x: x[1])

    names=[pair[0] for pair in s_pairs]
    return names

    

    

