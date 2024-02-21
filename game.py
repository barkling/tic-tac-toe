import copy


# 检查是否下完：下完返回true
def terminate(board):
    #单纯判断棋盘是否填满
    flag=1
    for row in board:
        if(None not in row):
            continue
        else:
            flag=0
            break
    if(flag==1):
        return True

    if(board[0][0]==board[1][1]==board[2][2]!=None):
        return True
    if(board[0][2]==board[1][1]==board[2][0]!=None):
        return True
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]!=None):
            return True
        if(board[0][i]==board[1][i]==board[2][i]!=None):
            return True
    return False

# 棋盘展示
def showboard(board):
    print("-"*9)
    for row in board:
        for i in row:
            if(i==None):
                print("|?|",end='')
            if(i==1):
                print("|o|",end='')
            if(i==-1):
                print("|x|",end='')
        print('\n'+"-"*9)

# 检测谁赢了，并对应分别返回None，1，-1，0
def result(board):
    # 返回 None 说明还能下
    # 返回 1 说明 ”o” 获胜
    # 放回 -1 说明 “x” 获胜
    # 返回 0 说明 平局
    if(not terminate(board)):
        return None
    if(board[0][0]==board[1][1]==board[2][2]!=None):
        return board[1][1]
    if(board[0][2]==board[1][1]==board[2][0]!=None):
        return board[1][1]
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]!=None):
            return board[i][0]
        if(board[0][i]==board[1][i]==board[2][i]!=None):
            return board[0][i]
    return 0
# 根据上面的函数输出赢家
def showresult(board):
    a = result(board)
    if(a==1):
        print(">>>>> WINNER:'o'-获胜者:'o' !!! <<<<<")
    if(a==-1):
        print(">>>>> WINNER:'x'-获胜者:'x' !!! <<<<<")
    if(a==0):
        print(">>>>> EVAL-平局 <<<<<")
    if(a==None):
        print(">>>>> 对局尚未结束 <<<<<")

# 检测棋盘上还有哪些空位可以下
def empty_places(board):
    list=[]
    for a in range(3):
        for b in range(3):
            if(board[a][b]==None):
                list.append((a,b))
    return list

# 检测该谁下了
# 默认设定为“o”先下，“x”后下
# 返回对应的数值，“o”为1，“x”为-1
def check_next_player(board):
    o_num = 0
    x_num = 0
    for row in board:
        for i in row:
            if(i==1):
                o_num+=1
            if(i==-1):
                x_num+=1
    if(o_num>x_num):
        # 下“x”
        return -1
    else:
        # 下“o”
        return 1

# 玩家下棋
def playchess(board,type):
    print(">>>>> 请输入你要下的位置: ")
    while True:
        while True:
            a=int(input("第?行: "))
            if(a not in range(1,4)):
                print("！！！非法输入，请输入1、2、3中的一个数！！！")
                continue
            else:
                break
        while True:
            b=int(input("第?列: "))
            if(b not in range(1,4)):
                print("！！！非法输入，请输入1、2、3中的一个数！！！")
                continue
            else:
                break
        if(board[a-1][b-1]!=None):
            print("！！！该格已有旗子占用，请换一个位置再下吧！！！")
            continue
        else:
            break
    board[a-1][b-1]=type

# 电脑下棋
def computer_playchess(board,type):
    empty_location = empty_places(board)
    if(type==1):
        flag = float('-inf')
        for i in empty_location:
            copyboard = copy.deepcopy(board)
            copyboard[i[0]][i[1]]=check_next_player(copyboard)
            if flag<min_result(copyboard):
                flag=min_result(copyboard)
                action = i
    else:
        flag = float('inf')
        for i in empty_location:
            copyboard = copy.deepcopy(board)
            copyboard[i[0]][i[1]]=check_next_player(copyboard)
            if flag>max_result(copyboard):
                flag=min_result(copyboard)
                action = i
    board[action[0]][action[1]]=type

# 电脑先下时
def max_result(board):
    # fake_board = copy.deepcopy(board)
    if terminate(board):
        return result(board)
    flag=float('-inf')
    for i in empty_places(board):
        fake_board = copy.deepcopy(board)
        fake_board[i[0]][i[1]]=check_next_player(fake_board)
        real_result = min_result(fake_board)
        if flag<real_result:
            flag=copy.deepcopy(real_result)
    return flag

def min_result(board):
    # fake_board = copy.deepcopy(board)
    if terminate(board):
        return result(board)
    flag=float('inf')
    for i in empty_places(board):
        fake_board = copy.deepcopy(board)
        fake_board[i[0]][i[1]]=check_next_player(fake_board)
        real_result = max_result(fake_board)
        if flag>real_result:
            flag=copy.deepcopy(real_result)
    return flag



# 游戏本体
def game(model,board):
    if(model==1):
        print("-"*45)
        print(">>>>> 即将进入模式1：pvp模式 <<<<<")
        while(not terminate(board)):
            showboard(board)
            playchess(board,check_next_player(board))
        showboard(board)
        showresult(board)

    if(model==2):
        print("-"*45)
        print(">>>>> 即将进入模式2：pve模式(与电脑对战) <<<<<")
        a = int(input(">>>>> 请选择你的下棋顺序：————1. 你先手    ————2. 你后手 "))
        if a==1:
            while(not terminate(board)):
                showboard(board)
                playchess(board,check_next_player(board))
                if not terminate(board):
                    showboard(board)
                    print("电脑正在思考...")
                    computer_playchess(board,check_next_player(board))
            showboard(board)
            showresult(board)
        if a==2:
            while(not terminate(board)):
                showboard(board)
                print("电脑正在思考...")
                computer_playchess(board,check_next_player(board))
                if not terminate(board):
                    showboard(board)
                    playchess(board,check_next_player(board))
            showboard(board)
            showresult(board)

    if(model==3):
        print("-"*45)
        print(">>>>> 即将进入模式3：eve模式(电脑对战电脑）<<<<<")
        while not terminate(board):
            showboard(board)
            computer_playchess(board,check_next_player(board))
        showboard(board)
        showresult(board)

if __name__ == '__main__':
    # board=[[-1,1,None],
    #        [1,-1,None],
    #        [1,None,None]]
    board=[[None,None,None],
           [None,None,None],
           [None,None,None]]
    # print(terminate(board))
    # print(result(board))
    # print(empty_places(board))
    # print(empty_places(board)[0][0])
    # print(type(empty_places(board)[0][0]))
    # showboard(board)
    # while(not terminate(board)):
    #     emp_num=check_next_player(board)
    #     playchess(board,emp_num)
    #     showboard(board)
    # showresult(board)
    while(not terminate(board)):
        computer_playchess(board,check_next_player(board))
        showboard(board)
    showresult(board)
    # computer_playchess(board,check_next_player(board))
    # showboard(board)


