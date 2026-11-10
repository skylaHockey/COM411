# def pattern():
#     sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
#     return sequences
# def run():
#     print(pattern())
# run()

def pattern():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return sequences
def display_keyS(data):
    print("keys:")
    print(data)
    print()
def display_values(data):
    print("values:")
    print(value)
    print()
def display_pairs(data):
    print("pairs:")
    for key, value in data.items():
        print(f"{key}: {value}")
        print()
def run():
    data = pattern()
    print(f"Dictionary:\n{data}")

    display_keyS(data)
    display_values(data)
    display_pairs(data)
run()