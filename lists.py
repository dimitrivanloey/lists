'''
Write a function that takes a list value as an argument and returns a string with all the items
separated by a comma and a space, with 'and' inserted before the last item.
'''

def list_items(items):
    if len(items) == 0:
        return 'This list is empty!'
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return '{} and {}'.format(''.join(items[:-1]), items[-1])
    return '{}, and {}'.format(', '.join(items[:-1]), items[-1])


spam = ['apple', 'bananas', 'oranges']
print(list_items(spam))


my_list = ['Dimitri', 'Dorien']
output = ' and '.join(my_list)
print(output)