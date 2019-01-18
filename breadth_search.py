graph = {}
graph["you"] = ["aaron", "rob", "deeta the cat"]
graph["aaron"] = ["marv","laggy","amanda"]
graph["rob"] = ["aaron","joe m", "joe p"]
graph["deeta the cat"] = ["laggy","jon","heather"] 
graph["jon"] = []
graph["joe m"] = []
graph["amanda"] = []
graph["marv"] = []
graph["laggy"] = []
graph["joe p"] = ["rob"]

from collections import deque
def who_is_the_sql_wizard(name):
    return name[-1] == "b"

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if who_is_the_sql_wizard(person):
                print('{} is a sql wizard!'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

search("you")