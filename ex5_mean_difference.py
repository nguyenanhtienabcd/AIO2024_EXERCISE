
import math

#start def
def mean_deff(y=1,y_hat=1,n=1,p=1):
    sub = math.pow(y,1/n) - math.pow(y_hat,1/n)
    result = math.pow(sub,p)
    return result

#excute def
if __name__ == '__main__':
    print(mean_deff(y=99,y_hat=99.5,n=2,p=3))
