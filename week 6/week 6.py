import os

# from sys import path
#
# def cwd ():
#     path = os.getcwd()
#     print(f"the current working directory is {path}")
#     print("the directory contains the following files:")
#     for file in os.listdir(path):
#         print(file)
#
# def run():
#    print("Processing...")
#    cwd()
#
# if __name__ == '__main__':
#     run()

# def display_chars (file_path, num_chars):
#     with open(file_path) as file:
#         data = file.read (num_chars)
#         print("the first 5 characters are:")
#         print(data)
#
# def display_line (file_path):
#     with open(file_path) as file:
#         data = file.readline ().strip ()
#         print("the first line is:")
#         print(data)
#
# def display_text (file_path):
#     with open(file_path) as file:
#         data = file.read()
#         print("the full text is:")
#         print (data)
#
# def run_task2 ():
#     display_chars("library.txt", 5)
#     display_line("library.txt")
#     display_text("library.txt")
#
# if __name__ == "__main__":
#     run_task2()

def search (file_name):
    print("searching...")
    with open(file_name, "r") as file:
        for location in file:
            print(f"looked in {location}")
def run_task3 () :
    search("library.txt")

if __name__ == "__main__":
    run_task3()
print("...done!")