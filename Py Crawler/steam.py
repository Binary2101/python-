# def count_word():
count = {}
with open('data.txt') as f:
    lines = f.readlines()
for line in lines:
    first_word = line.split(' ')[0]
    if count.__contains__(first_word):
        count[first_word] +=1
    else:
        count[first_word] = 1
print(count)
