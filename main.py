def solo():
    name = str(input('Давайте познакомимся, как Вас зовут?'))
    while True:
        position = input(f'{name}, Вы хотите играть за крестики (1) или за нолики(0)?')
                    
        if not(position.isdigit()):
            print(" Введите 0 или 1! ")
            continue
        
        pos = int(position)
        
        if pos != 0:
            if pos != 1:
                print(" Введите 0 или 1! ")
                continue
        
        return name, pos

def multiplay():
    print('Давайте понакомимся')
    name_1 = str(input('Имя первого игрока (крестики): '))
    name_2 = str(input('Имя второго игрока (нолики):'))
    return name_1, name_2

def start():
    while True:
        m = input('Добро пожаловать в игру "Крестики-нолики", игра с компьютером (1) или с другом (2)?')
                    
        if not(m.isdigit()):
            print(" Введите 1 или 2! ")
            continue
        
        n = int(m)
        
        if n != 1:
            if n != 2:
                print(" Введите 1 или 2! ")
                continue
        return n

def instr(name_1, name_2 = None):
    name = name_1
    if name_2 is None:
        name_2 = ''
    else:
        name += ' и '
    print(f'{name}{name_2}, рады преведствовать в игре!')
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def strock(name):
    while True:
        cords = input(f' {name}, Ваш ход: ').split()
        
        if len(cords) != 2:
            print(' Введите 2 координаты! ')
            continue
        
        x, y = cords
        
        if not(x.isdigit()) or not(y.isdigit()):
            print(' Введите числа! ')
            continue
        
        x, y = int(x), int(y)
        
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print(' Координаты вне диапазона! ')
            continue
        
        if field[x][y] != '-':
            print(' Клетка занята! ')
            continue
        
        return x, y

def computer_move():
    
    for i in range(3):
        if field[i][0] == field[i][1] and field[i][2] == '-':
            return i,2
        elif field[i][0] == field[i][2] and field[i][1] == '-':
            return i,1
        elif field[i][1] == field[i][2] and field[i][0] == '-':
            return i,0
            
    for i in range(3):
        if field[0][i] == field[1][i] and field[2][i] == '-':
            return 2, i
        elif field[0][i] == field[2][i] and field[1][i] == '-':
            return 1, i
        elif field[1][i] == field[2][i] and field[0][i] == '-':
            return 0, i
    
    if field[0][0] == field[1][1] and field[2][2] == '-':
        return 2, 2
    if field[0][0] == field[2][2] and field[1][1] == '-':
        return 1, 1
    if field[1][1] == field[2][2] and field[0][0] == '-':
        return 0, 0
    
    if field[0][2] == field[1][1] and field[2][0] == '-':
        return 2, 0
    if field[0][2] == field[2][0] and field[1][1] == '-':
        return 1, 1
    if field[2][0] == field[1][1] and field[0][2] == '-':
        return 0, 2
    
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col] == '-':
            return row, col
        
def check_win():
    for i in range(3):
        symbols=[]
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ['X','X','X'] or symbols == ['O','O','O']:
            return True
    for i in range(3):
        symbols=[]
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ['X','X','X'] or symbols == ['O','O','O']:
            return True
        
    symbols=[]
    for i in range(3):
        symbols.append(field[i][i])
        if symbols == ['X','X','X'] or symbols == ['O','O','O']:
            return True
    
    symbols=[]    
    for i in range(3):
        symbols.append(field[i][2-i])
        if symbols == ['X','X','X'] or symbols == ['O','O','O']:
            return True
        
    return False

def multiplay_play(name_1,name_2):
    
    count = 0
    while True:
        count += 1
        show()
        if count % 2 == 1:
            x, y = strock(name_1)
            field[x][y] = 'X'
            if check_win():
                show()
                print(f' {name_1} победил! ')
                break
        else:
            x, y = strock(name_2)
            field[x][y] = 'O'
            if check_win():
                show()
                print(f' {name_2} победил! ')
                break       
    
        if count == 9:
            print(" Ничья!")
            break
            
def solo_play(name,position):
    smb_user = 'X'
    smb_comp = 'O'
    
    if not position:
        smb_user, smb_comp = smb_comp, smb_user
        
        
    count = 0
    while True:
        count += 1
        show()
        if count % 2 == 1:
            if position:
                x, y = strock(name)
                field[x][y] = 'X'
                if check_win():
                    show()
                    print(f' {name} победил! ')
                    break
            else:
                print('Ход компютера:')
                x, y = computer_move()
                field[x][y] = 'X'
                if check_win():
                    show()
                    print(f' Компютер победил! ')
                    break
        else:
            if not position:
                x, y = strock(name)
                field[x][y] = 'O'
                if check_win():
                    show()
                    print(f' {name} победил! ')
                    break
            else:
                print('Ход компютера:')
                x, y = computer_move()
                field[x][y] = 'O'
                if check_win():
                    show()
                    print(f' Компютер победил! ')
                    break
    
        if count == 9:
            print(" Ничья!")
            break

n = int(start())
field = [["-"] * 3 for i in range(3) ]
if n == 1:
    name, position = solo()
    instr(name)
    solo_play(name,position)
else:
    name_1, name_2 = multiplay()
    instr(name_1,name_2)
    multiplay_play(name_1,name_2)