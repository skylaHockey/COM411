# def observed():
#     observations = {"car", "sky scarper", "bike", "house", "house"}
#     return observations
# def run_task1():
#     print(observed())
# run_task1()

# def observed():
#     observations = []
#
#     for count in range(7):
#         print ("please enter an observation:")
#         observations.append(input())
#
#     return observations
#
# def run_task2():
#     print("Counting observations...")
#     observations = observed()
#
#     #populate set
#     observations_set = set()
#     for observation in observations:
#         data = (observation, observations.count(observation))
#         observations_set.add(data)
#
#     #display set
#     for data in observations_set:
#         print(f"{data[0]} observed {data[1]} times.")
# run_task2()
# def observed() :
#     observations = []
#
#     for count in range(5):
#         print("Please enter an observation:")
#         observations.append(input())
#
#     return observations
#
# def remove_observation(observations):
#     is_running =True
#     while (is_running):
#         print("Do you wish to remove an observation? (yes/no)")
#         response = input()
#         if (response == "yes"):
#             print("what observation do you wish to remove?")
#             observation = input()
#             observations.remove(observation)
#         else:
#             is_running = False
#
# def run_task3():
#     observations = observed()
#     remove_observation(observations)
#
#     #populate set
#     observations_set = set()
#     for observation in observations:
#         data = (observation, observation.count(observation))
#         observations_set.add(data)
#
#      #display set
#     for observation in observations_set:
#         print(f"{data[0]} observed {data[1]}times.")
# run_task3()



