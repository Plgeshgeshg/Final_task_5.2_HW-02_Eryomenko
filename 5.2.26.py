matrix = [[" - ", " - ", " - "],[" - ", " - ", " - "],[" - ", " - ", " - "]]
Obj1 = "{X}"
Obj2 = "{O}"
i=0
j=0

def greet():
    print("------------------------")
    print("Добро пожаловать в игру")
    print("   Крестики-нолики")
    print("------------------------")

def Umatrix(func):
    def Pole():
        mat=[{0}, [{1}, {2}, {3}]]
        print(mat[0],*mat[1])
        print(mat[1][0],*func[0])
        print(mat[1][1],*func[1])
        print(mat[1][2],*func[2])
    return Pole()

def Ask():
    while True:
        i = input("Номер строки:")
        j = input("Номер столбца:")
        if str(i).isdigit() and str(j).isdigit():
            i = int(i) - 1
            j = int(j) - 1
            if 0<=i<=2 and 0<=j<=2:
                if matrix[i][j] == str(" - "):
                    return i, j
                else:
                    print("Клетка занята!")
            else:
                print("Вне диапазона!")
        else:
            print("Введите целые числа!")

def WinTerms():
    rows = [((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),
    ((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((0,2),(1,1),(2,0))]
    for row in rows:
        symbols = []
        for c in row:
            symbols.append(matrix[c[0]][c[1]])
            if symbols == [Obj1,Obj1,Obj1]:
                Umatrix(matrix)
                print("Победил X!")
                return True
            if symbols == [Obj2,Obj2,Obj2]:
                Umatrix(matrix)
                print("Победил O!")
                return True
    return False

greet()
matrix = [[" - ", " - ", " - "],[" - ", " - ", " - "],[" - ", " - ", " - "]]
num=0
while True:
    num+=1

    Umatrix(matrix)

    if num%2==1:
        print("X")
    else:
        print("O")

    i,j = Ask()

    if num%2==1:
        matrix[i][j] = Obj1
    else:
        matrix[i][j] = Obj2

    if WinTerms():
        print("Конец Игры.")
        break

    if num==9:
        Umatrix(matrix)
        print("Ничья.")
        break
