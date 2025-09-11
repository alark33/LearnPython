#Алгоритм Дейкстры
#создаём хеш-таблицу, содержащую все узлы и сумму ребер
graph = {'start': {'a': 6,
                   'b': 2},
         'a': {'finish': 1,},
         'b': {'a': 3,
               'finish': 5},
         'finish':{},
}

#хеш-таблица стоимостей, которая будет изменяться во время 
# выполнения алгоритма
infinity = float('inf')
costs = {'a': 6,
         'b': 2,
         'finish': infinity}

#хеш-таблица для указания родителей узлов
parents ={'a': 'start',
          'b': 'start',
          'finish': None,
          }

#список для отслеживания всех уже обработанных узлов
proccessed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in proccessed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    proccessed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(costs['finish'])
print(parents)

#8
#60
#4