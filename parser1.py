import lexer, action, goto, grammer_rules

stack = ['0']

def parser():
    a = lexer.get_next_token()
    # print(a)
    # print(stack)
    while(True):    
        s = int(stack[-1])
        command = action.get_action(s, a)
        # print(f'command={command},s={s},a={a}')
        if command == '':
            print(f'command={command},s={s},a={a}')
            raise ValueError("error command!")
        elif command == 'r0':
            print('accept')
            return
        elif command[0] == 's':
            stack.append(command[1:])
            a = lexer.get_next_token()
            # print(a)
            # print(stack)
        elif command[0] == 'r':
            rule = grammer_rules.grammar_rules[f'{command[1:]}']
            for i in range(0, len(rule['body'])):
                stack.pop()
            # print(stack)
            stack.append(goto.get_goto(int(stack[-1]), rule['head']))
            # print(stack)


if __name__ == '__main__':
    parser()