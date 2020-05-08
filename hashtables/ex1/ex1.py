def get_indices_of_item_weights(weights, length, limit):

    h = {}

    for index, i in enumerate(weights):
        if i in h:
            h[i].append(index)
        else:
            h[i] = [index]
    
    for i in h:
        diff = limit - i
        if (diff in h):
            if len(h[diff]) > 1:
                return [h[diff][1], h[diff][0]]
            else:
                return [h[diff][0], h[i][0]]
    
    return None




"""
takes in a list of weights, the length of the list, and a weight limit
Should loop through elements and check for elements that equal limit when summed
"""