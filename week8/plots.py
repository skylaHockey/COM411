import matplotlib.pyplot as plt
# def display_line (x , y):
#     plt.plot(x,y)
#     plt.show()
#
#
# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
# display_line(x,y)

# def small():
#     x= [3,3,4,4,3]
#     y= [3,4,4,3,3]
#     plt.plot(x,y, 'r:o')
#
# def medium():
#     x=[2,2,5,5,2]
#     y=[2,5,5,2,2]
#     plt.plot(x,y,'g--s')
#
# def large():
#     x=[1,1,6,6,1 ]
#     y=[1,6,6,1,1]
#     plt.plot(x,y,'b-p')
#
# def run_task2():
#     small()
#     medium()
#     large()
#     plt.plot()
#     plt.show()
# run_task2()

# def coordinate():
#     print("Enter an x value;")
#     x=int(input())
#     print("Enter an y value;")
#     y=int(input())
#     return (x,y)
#
# def path():
#     print("Retrieving path..")
#     x_values= []
#     y_values = []
#
#     for count in range(4):
#         data = coordinate()
#         x_values.append(data[0])
#         y_values.append(data[1])
#
#     return(x_values, y_values)
# def run_task3():
#     values = path()
#     plt.plot(values[0], values[1], "r--o")
#     plt.xlabel("x values")
#     plt.ylabel("y values")
#     plt.show()
# run_task3()


import random as rnd

def data():
    paths= {}

    print("what type of line (:, -- or -")
    line_style = input()

    print("What colour (r, g or b)?")
    colour = input()

    print("what style of marker (o,s or ^)?")
    marker_style = input()

    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style

    return paths
def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for num_lines in range(num_lines):
        values = data()
        x = rnd.sample(range(1, 10), 5)
        y = rnd.sample(range(1, 10), 5)
        format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
        plt.plot(x, y, format)
        plt.show()
def run_task4():
    print("running...")
    generate()
    print("done")
run_task4()














