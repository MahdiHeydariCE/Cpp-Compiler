action_table = []
action_csv = open("action_csv.csv" , "r")
action = action_csv.read().split("\n")[:-1]
action_csv.close()
s = action[0].split(",")[1:]
s.pop(46)
s.pop(45)
s.insert(45,',')
action_head = {key:value for value,key in enumerate(s)}
for row in action[1:]:
    action_table.append(row.split(",")[1:])
def get_action(row, column):
    if column == 0:
        raise ValueError
    column = action_head[column]
    return action_table[row][column]