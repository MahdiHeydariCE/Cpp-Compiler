goto_table = []
goto_csv = open("goto_csv.csv" , "r")
goto = goto_csv.read().split("\n")[:-1]
goto_csv.close()
goto_head = {key:value for value,key in enumerate(goto[0].split(",")[1:])}
for row in goto[1:]:
    goto_table.append(row.split(",")[1:])
def get_goto(row, column):
    if column == 0:
        raise ValueError
    column = goto_head[column]
    return goto_table[row][column]