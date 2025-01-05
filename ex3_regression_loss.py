import math
import random

# is number function
def is_number(n):
    try:
        float(n)
    except ValueError:  # if value is converted from float(n) not correct => return False
        return False
    return True

# is Int number function
def is_int(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def regression_loss():
    result = 0
    num_samples = input('input number of sample:')

    #check num_samples is number or not, if not => stop
    if is_number(num_samples) == False:
        print('num_samples must be an integer number')
        return 1

    #check num_samples is int or not, if not => stop
    if is_number(num_samples) == True and is_int(num_samples) == False:
        print('num_samples must be an integer number')
        return 1

    num_samples = int(num_samples)    #convert 'num_samples' from str to int
    loss_name = input("input loss name (MAE|MSE|RMSE):") 
    

    # check loss name with MAE 
    if loss_name == 'MAE':
        total_loss = 0
        result = 0
        for i in range(num_samples):
            predict = random.uniform(0,10)
            target = random.uniform(0,10)
            loss = math.fabs(target-predict)
            print(f'loss name: {loss_name}, sample {i}, predict: {predict}, target: {target}, loss: {loss}')
            total_loss += loss
        result=total_loss/num_samples
        print ('total loss_MAE:',result)

    # check loss name with MSE
    elif loss_name == 'MSE':
        total_loss = 0
        result = 0
        for i in range(num_samples):
            predict = random.uniform(0,10)
            target = random.uniform(0,10)
            loss = (target-predict)**2
            print(f'loss name: {loss_name}, sample {i}, predict: {predict}, target: {target}, loss: {loss}')
            total_loss += loss
        result=total_loss/num_samples
        print ('total loss_MSE:',result)

# check loss name with RMSE
    elif loss_name == 'RMSE':
        total_loss = 0
        result = 0
        for i in range(num_samples):
            predict = random.uniform(0,10)
            target = random.uniform(0,10)
            loss = (target-predict)**2
            print(f'loss name: {loss_name}, sample {i}, predict: {predict}, target: {target}, loss: {loss}')
            total_loss += loss
        result = math.sqrt(total_loss/num_samples)
        print ('total loss_RMSE:',result)

    else:
        print(f'regression loss {loss_name} is not supported')
    
    return result


if __name__ == '__main__':
    regression_loss()