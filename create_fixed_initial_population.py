import json


SIZE = 1000
AVOID_NUMBER = 69
AVOID_OFFSET = 100

output = []
for number in range(SIZE):
    if AVOID_NUMBER - AVOID_OFFSET < number < AVOID_NUMBER + AVOID_OFFSET:
        continue
    output.append(number)

with open("fixed_initial_population.json", "w") as json_file:
    json.dump(output, json_file)