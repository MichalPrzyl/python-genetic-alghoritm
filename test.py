# class Sample:
#     def __init__(self, number, points):
#         self.number = number
#         self.points = points


# squad = [68.91475704743891, 69.0551737506807, 69.0551737506807, 69.0551737506807, 69.0551737506807, 69.0551737506807]
# #15583-INFO-[69.0551737506807, 68.91475704743891]
# print(squad)
# samples = []

# for element in squad:
#     samples.append(Sample(element, abs(element-69)))


# best_squad = sorted(samples, key=lambda x: x.points)[:2]

# values = list(map(lambda x: x.number, best_squad))
# print(values)


# 26794-INFO-============================
# 26794-INFO-[68.7559, 68.9625, 68.9625, 68.9625, 68.9625, 68.9625]
# 26794-INFO-best_squad:
# 26794-INFO-[68.9625, 68.7559]
# 26794-INFO-points:
# 26794-INFO-[{'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.7559, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}]
#[        ,   {'number': 68.9625, 'points': 0.037499999999994316}] {'number': 68.7559, 'points': 0.2441000000000031}
# 26794-INFO-============================
WINNER = 69

all_objs = []

values = [68.7559, 68.9625]

for el in values:
    obj = {'number': el, 'points': (el-WINNER)}
    all_objs.append(obj)

print(all_objs)


# 26794-INFO-best_squad:
# 26794-INFO-[68.9625, 68.7559]
# 26794-INFO-points:
# 26794-INFO-[{'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.7559, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}, {'number': 68.9625, 'points': 0.037499999999994316}]
# 26794-INFO-============================