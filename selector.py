import random

feed_list = ['Dateline: Bears Edition', 'Damn Good Chicken', 'Fight Lawyers', 'English Names', 'Free Stairs', 'ASPCA for Bros', 'White or Flight', \
             'Youre Awake', 'Illiad Idiots', 'Dating Coach', 'Spirit Airlines']

feed_list.sort (key=str.lower)

show_length = int(input("How many sketches do you need?"))
x = int(input("What's your lucky number?"))
random.seed(x)

i = 0
while i < x:
    y = random.sample(feed_list, show_length)
    i += 1
    
print("Your show is {}".format(y))
