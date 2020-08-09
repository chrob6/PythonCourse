#mini projekt 1
def read_data(number_of_row):
    with open('kandydaci_utf8.csv', 'r', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=';')
        list_to_return = [row[number_of_row] for row in r]
        list_to_return = list_to_return[1:len(list_to_return)-1]
    return list_to_return

name = read_data(1)
age = read_data(4)
votes = read_data(14)
votes_percent = read_data(15)
second_round = read_data(17)
colors = ["r", "g", "m", "y", "purple", "b","grey", "orange", "c", "purple"]
print(second_round)

ax = plt.subplot()

votes_percent = [x.replace(",",".") for x in votes_percent]
votes_percent = [float(x) for x in votes_percent]
votes = [int(x) for x in votes]
age = [int(x) for x in age]

p1 = plt.subplot(313)
p1 = plt.bar(name, votes, width=0.6, color = colors)
plt.ylabel("Votes")
plt.title("Pierwsza tura")

# NIE DZIALA PRZY SUBPLOT
#counter = 0
# for i in p1:
#     height = i.get_height()
#     ax.annotate('{}'.format(height),
#                 xy=(counter, height),
#                 xytext=(0, 1),
#                 textcoords="offset points",
#                 ha='center', va='bottom')
#     counter = counter + 1

p2 = plt.subplot(322)
p2 = plt.pie(votes_percent, labels = name,
             autopct = "%.2f%%",
             shadow = True,
             colors = colors
             )
plt.axis('equal')


plot3_name = []
plot3_votes_percent = []
plot3_colors = []

counter = 0
for i in votes_percent:
    if i > 1:
        plot3_name.append(name[counter])
        plot3_votes_percent.append(votes_percent[counter])
        plot3_colors.append(colors[counter])
    counter = counter + 1

p3 = plt.subplot(312)
p3 = plt.bar(plot3_name, plot3_votes_percent, width=0.6, color = plot3_colors)
plt.ylabel("Percent")
plt.title("Pierwsza tura powyżej 1%")

percent_yes_percent = []
percent_no_percent = []
percent_yes_names = []

counter = 0
for x in second_round:
    if x == "Tak":
        percent_yes_percent.append(votes_percent[counter])
        percent_yes_names.append(name[counter])
    if x == "Nie":
        percent_no_percent.append(votes_percent[counter])
    counter = counter + 1

percent_yes_names.append("REST")
percent_yes_percent.append(sum(percent_no_percent))

p4 = plt.subplot(321)
p4 = plt.pie(percent_yes_percent, labels=percent_yes_names,
             autopct="%.2f%%",
             shadow=True,
             colors= ["r", "c", "grey"]
             )
plt.show()

votes_range = [x for x in range(35,max(age)+6, 5)]

plt.hist(age,
         bins = votes_range,
         alpha = 0.5,
         color = "c")
plt.ylim()
plt.xlabel("Range of ages")
plt.ylabel("Number of candidates")
plt.title("Histogram of Ages")
plt.show()



