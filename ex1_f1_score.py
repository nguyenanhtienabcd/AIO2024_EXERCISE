#F1-Score function
def f1_score(tp,fp,fn):
    if isinstance(tp,int) != True:
        print('tp must be int')
        return 
    
    if isinstance(fp,int) != True:
        print('fp must be int')
        return 
    
    if isinstance(fn,int) != True:
        print('fn must be int')
        return 
    
    if tp <= 0:
        print('tp must be greater than 0')
        return 

    if fp <= 0:
        print('fp must be greater than 0')
        return 

    if fn <= 0:
        print('fn must be greater than 0')
        return 
    
    precise = tp / (tp+fp) 
    recall = tp / (tp+fn)  
    f1 = 2*precise*recall / (precise+recall)

    print(f'Precise is: {precise}')
    print(f'Recall is: {recall}')
    print(f'F1-score is: {f1}')

    return f1


# excute the above fucntion in main funtion
if __name__=='__main__':
    f1_score(tp=2,fp=3,fn=5)
    assert abs(round(f1_score(tp=2,fp=3,fn=5), 2) - 0.33) < 1e-2, 'incorrect function'
    print(round(f1_score(tp=2,fp=3,fn=5),2))