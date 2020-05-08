#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
          
    h = { i.source: i.destination for i in tickets }
    route = ['NONE'] * (length + 1)

    for i in range(0,length):
        if h[route[i]] == 'NONE':
            break
        if route[i] in h:
            route[i+1] = h[route[i]]

    route.pop(0)



    return route

    