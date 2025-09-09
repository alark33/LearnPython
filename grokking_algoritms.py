from collections import deque
def is_seller(name):
    """Проверка, продаёт ли человек манго. Если имя заканчивается
    на "m", то человек - продавец манго"""
    return name[-1] == 'm'

def search(name):
    """Функция поиска в ширину на примере поиска человека,
    который продаёт манго"""
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []

search('you')