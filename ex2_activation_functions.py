import math

# is number function
def is_number(n):
    try:
        float(n)
    except ValueError:  # if value is converted from float(n) not correct => return False
        return False
    return True

#create sigmoid funtion
def sigmoid(x):
    return 1 / (1+math.exp(x))

#create Rectified Linear Unit funtion
def relu(x):
    if x <= 0:
        return 0
    if x > 0:
        return x
    
#create Exponential Linear Unit funtion
def elu(x):
    alpha = float(input('alpha = '))
    if x <= 0:
        return alpha * (math.exp(x)-1)
    if x > 0:
        return x

#create a selected activate function
def activation_function():
    x = input('input x = ')
    #check x is number or not
    if is_number (x) == False:
        print('x must be a number')
        return 1
    x=float(x)
    act = input('input activation funtion (sigmoid|relu|elu):')
    if act == 'sigmoid':
        print (f'sigmoid f({x}): {sigmoid(x)}')
        return sigmoid(x)
    elif act == 'relu':
        print (f'relu f({x}): {relu(x)}')
        return relu(x)
    elif act == 'elu':
        print (f'elu f({x}): {elu(x)}')
        return elu(x)
    else:
        print(f'{act} is not supported')
        return 1
    


# excute the above fucntion in main funtion   
if __name__ == '__main__':
    print(round(activation_function(),2))


