import matplotlib.pyplot as plt
# def display_line (x , y):
#     plt.plot(x,y)
#     plt.show()
#
#
# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
# display_line(x,y)

def small():
    x= [3,3,4,4,3]
    y= [3,4,4,3,3]
    plt.plot(x,y, 'r:o')

def medium():
    x=[2,2,5,5,2]
    y=[2,5,5,2,2]
    plt.plot(x,y,'g--s')

def large():
    x=[1,1,6,6,1 ]
    y=[1,6,6,1,1]
    plt.plot(x,y,'b-p')

def run_task2():
    small()
    medium()
    large()
    plt.plot()
    plt.show()
run_task2()












