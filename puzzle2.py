with open('input2.txt', 'r') as f:
    input_list = f.read()


input_list = input_list.replace("\n", "").split(',')

print(input_list)


def format_input(inp):
    inp = inp.split(" ")
    minmax = inp[0].split('-')
    mini, maxi = int(minmax[0]), int(minmax[1])
    letter = inp[1][0]
    string = inp[2]

    return {'min': mini, 'max': maxi, 'letter': letter, 'string': string}


valid_count = 0
# Part 1
for i in range(len(input_list)):
    curr = input_list[i]
    obj = format_input(curr)
    if obj['string'].count(obj['letter']) <= obj['max'] and obj['string'].count(obj['letter']) >= obj['min']:
        valid_count += 1
print(valid_count)
valid_count = 0
# Part 2
for i in range(len(input_list)):
    curr = input_list[i]
    obj = format_input(curr)
    if bool(obj['string'][obj['min']-1] == obj['letter']) != bool(obj['string'][obj['max']-1] == obj['letter']):
        valid_count += 1

print(valid_count)
