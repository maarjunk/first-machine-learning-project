"""
in this file we define all the function,data
and then use them for creating f(x) and ploting the data
so this is the main file in our project 
i should define all function in other modula but i prefer to dont 
"""
import numpy as np 
import matplotlib.pyplot as plt 
import random as rd

#training set 
x_train = np.array([51,19,53,46,35,57,10,42,52,25])
y_train = np.array([575,550,550,540,570,570,615,545,535,590])
# x_train = np.array([2,4,5])
# y_train = np.array([1,3,6])
#use command below to se the points of data
plt.scatter(x_train,y_train)
#plt.axis([0,80,500,650])


#we use all of this in the end of the model as a subplot

#cost function 

# assuming that f(x) = w*x +b
# and wright now we dont  know what is f se we use a and b directly 
def cost_function( x_train , y_train , a , b ):
    """
    inputs:
    x_trains (np.ndarray) :set of x_i
    y_train (np,ndarray) :set of y_i
    a (float) : gradient of f(x)
    b (float) : offset of f(x)
    return :
    sum of squered erroe of f(x) devided by 2 * (size of data set)
    """

    m = x_train.size
    cost_amount = 0
    for _ in range(m):
        amount = (a*x_train[_]) + b
        amount -= y_train[_]
        amount = amount **2
        cost_amount += amount

    cost_amount /= 2*m

    return cost_amount


# gradient decent algorithm 

# our algorithm customize for our cost function but this logic can be useful in any function 
def gradient_decent ( x_train , y_train ):
    """
    inputs:
    a (int) : gradient of f(x).beacuse the cost function is squread so we can chose a randomly first time
    b (int) : ofset of f(x). beacuse the cost function is squread so we can chose a randomly first time
    x_trains (np.ndarray) :set of x_i
    y_train (np,ndarray) :set of y_i
    return :
    the a ,b with cause the cost be minmum 
    """
    a = 2
    b = 550
    print(a,b)
    def d_a(a , b ,x_t = x_train , y_t = y_train ):
        m = x_t.size
        d_amount = 0
        for _ in range(m):
            cost_amount = (a*x_t[_]) + b
            cost_amount -= y_t[_]
            cost_amount *= x_t[_]
            d_amount += cost_amount
        d_amount /= m

        return d_amount
    def d_b(a , b ,x_t = x_train , y_t = y_train ):
        m = x_t.size
        d_amount = 0
        for _ in range(m):
            cost_amount = (a*x_t[_]) + b
            cost_amount -= y_t[_]
            d_amount += cost_amount
        d_amount /= m

        return d_amount
    # alpha = 0.01 = learning rate
    while True:
        tem_a = a - ( 0.001 * d_a(a,b))
        tem_b = b - ( 0.001 * d_b(a,b))
        if (tem_a == a and tem_b == b) or (abs(a-tem_a)<=0.001 and abs(b-tem_b)<=0.001) :
            break

        a = tem_a
        b = tem_b
        print((a,b,cost_function(x_train , y_train , a,b)) , end="__")
    print()
    print("#"*50)
    return (a,b)
result =gradient_decent(x_train , y_train)
print(result)

# f(x)

def f_x (distance): 
    a = result[0]
    b = result[1]
    return a*distance +b
print(f_x(100))
plt.plot([0,65],[592.197,543.577])
plt.show()