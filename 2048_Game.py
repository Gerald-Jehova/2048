#  File: 2048 Ripoff.py

#  Description: Crappy copy of the popular browser game '2048'

#  Name: Carlos Vazquez

#  Date Created: 3-08-23

#  Date Last Modified: 3-10-23
#  Date Last Modified: 10-08-23 added screen clear

#  Notes: ***Run with .exe not in IDLE. ASCII color effects will not work in IDLE

import random
import os

### Inserts 2 or 4 into empty space, with higher chance of 2 #############################################
def add_num(board):
  empty_spaces = 0
  for i in range(len(board)):
    for q in range(len(board[i])):
      if(board[i][q] == 0):
        empty_spaces += 1
  if(empty_spaces == 0):
    return None
  
  add2 = random.randint(1, empty_spaces)
  find_space = 0
  num = random.randint(1,3)
  
  for i in range(len(board)):
    for q in range(len(board[i])):
      if(board[i][q] == 0):
        find_space += 1
      if(find_space == add2):
        if(num == 2 or num == 3):
          board[i][q] = 2
        else:
          board[i][q] = 4
        break
    if(find_space == add2):
      break
##############################################################################################################

### Combines and shifts board to the right ###################################################################
def combine_right(board):
  board[0] = combine(board[0])
  board[1] = combine(board[1])
  board[2] = combine(board[2])
  board[3] = combine(board[3])
##############################################################################################################

### Combines and shifts board to the left ####################################################################
def combine_left(board):
  for i in range(len(board)):
    line = []
    for q in range(len(board)-1,-1,-1):
      line.append(board[i][q])
    board[i] = reverse_line(combine(line))
##############################################################################################################
  
### Combines and shifts board upward #########################################################################
def combine_up(board):
  for i in range(len(board)):
    line = []
    for q in range(len(board)-1,-1,-1):
      line.append(board[q][i])
    temp = reverse_line(combine(line))
    for z in range(len(board)):
      board[z][i] = temp[z]
##############################################################################################################

### Combines and shifts board downwards ######################################################################
def combine_down(board):
  for i in range(len(board)):
    line = []
    for q in range(len(board)):
      line.append(board[q][i])
    temp = combine(line)
    for z in range(len(board)):
      board[z][i] = temp[z]
##############################################################################################################

### Takes a line and combines & shifts to the right ##########################################################
def combine(line):
  while(not_shifted(line)):
    if(line[3] == 0 and line[2] != 0):
      line[3] = line[2]
      line[2] = 0
    if(line[2] == 0 and line[1] != 0):
      line[2] = line[1]
      line[1] = 0
    if(line[1] == 0 and line[0] != 0):
      line[1] = line[0]
      line[0] = 0

  if(line[3] == line[2]):
    line[3] = line[3] * 2
    line[2] = 0
  if(line[2] == line[1]):
    line[2] = line[2] * 2
    line[1] = 0
  if(line[1] == line[0]):
    line[1] = line[1] * 2
    line[0] = 0
    
  while(not_shifted(line)):
    if(line[3] == 0 and line[2] != 0):
      line[3] = line[2]
      line[2] = 0
    if(line[2] == 0 and line[1] != 0):
      line[2] = line[1]
      line[1] = 0
    if(line[1] == 0 and line[0] != 0):
      line[1] = line[0]
      line[0] = 0

  return line
##############################################################################################################

### Checks if a line is properly shifted #####################################################################
def not_shifted(line):
  num = False
  inner_zero = False
  for i in line:
    if(i != 0):
      num = True
    if(i == 0 and num == True):
      inner_zero = True

  return inner_zero
##############################################################################################################

### Returns the reverse of a line ############################################################################
def reverse_line(line):
  temp = []
  for i in range(len(line)-1,-1,-1):
    temp.append(line[i])
  return temp
##############################################################################################################

### Checks if there are possible moves left ##################################################################
def board_not_full(board):
  for i in board:
    if(0 in i):
      return True
  
  return False
##############################################################################################################

### Displays board in string format ##########################################################################
def display_board(board):
  space = ' '
  col1 = '\33[37m'
  col2 = '\33[36m'
  col3 = '\33[31m'
  
  print(f'{space:>30}{col2}---------------------')
  print(f'{space:>30}|{col1}', end = '')
  if(board[0][0] == 0):
    print(f'{col3}{board[0][0]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[0][0]:^4}{col2}|{col1}', end = '')
  if(board[0][1] == 0):
    print(f'{col3}{board[0][1]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[0][1]:^4}{col2}|{col1}', end = '')
  if(board[0][2] == 0):
    print(f'{col3}{board[0][2]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[0][2]:^4}{col2}|{col1}', end = '')
  if(board[0][3] == 0):
    print(f'{col3}{board[0][3]:^4}{col2}|')
  else:
    print(f'{board[0][3]:^4}{col2}|{col2}')
  print(f'{space:>30}---------------------')
  print(f'{space:>30}|{col1}', end = '')
  if(board[1][0] == 0):
    print(f'{col3}{board[1][0]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[1][0]:^4}{col2}|{col1}', end = '')
  if(board[1][1] == 0):
    print(f'{col3}{board[1][1]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[1][1]:^4}{col2}|{col1}', end = '')
  if(board[1][2] == 0):
    print(f'{col3}{board[1][2]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[1][2]:^4}{col2}|{col1}', end = '')
  if(board[1][3] == 0):
    print(f'{col3}{board[1][3]:^4}{col2}|')
  else:
    print(f'{board[1][3]:^4}{col2}|{col2}')
  print(f'{space:>30}---------------------')
  print(f'{space:>30}|{col1}', end = '')
  if(board[2][0] == 0):
    print(f'{col3}{board[2][0]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[2][0]:^4}{col2}|{col1}', end = '')
  if(board[2][1] == 0):
    print(f'{col3}{board[2][1]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[2][1]:^4}{col2}|{col1}', end = '')
  if(board[2][2] == 0):
    print(f'{col3}{board[2][2]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[2][2]:^4}{col2}|{col1}', end = '')
  if(board[2][3] == 0):
    print(f'{col3}{board[2][3]:^4}{col2}|')
  else:
    print(f'{board[2][3]:^4}{col2}|{col2}')
  print(f'{space:>30}---------------------')
  print(f'{space:>30}|{col1}', end = '')
  if(board[3][0] == 0):
    print(f'{col3}{board[3][0]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[3][0]:^4}{col2}|{col1}', end = '')
  if(board[3][1] == 0):
    print(f'{col3}{board[3][1]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[3][1]:^4}{col2}|{col1}', end = '')
  if(board[3][2] == 0):
    print(f'{col3}{board[3][2]:^4}{col2}|{col1}', end = '')
  else:
    print(f'{board[3][2]:^4}{col2}|{col1}', end = '')
  if(board[3][3] == 0):
    print(f'{col3}{board[3][3]:^4}{col2}|')
  else:
    print(f'{board[3][3]:^4}{col2}|{col2}')
  print(f'{space:>30}---------------------')
  
##############################################################################################################

### Displays title in ascii format ###########################################################################
def display_title():
  print('____\33[36m/\\\\\\\\\\\\\\\\\\\33[37m_________\33[36m/\\\\\\\\\\\\\\\33[37m_______________\33[36m/\\\\\\\33[37m________\33[36m/\\\\\\\\\\\\\\\\\\\33[37m____        ')
  print(' __\33[36m/\\\\\\///////\\\\\\\33[37m_____\33[36m/\\\\\\/////\\\\\\\33[37m___________\33[36m/\\\\\\\\\\\33[37m______\33[36m/\\\\\\///////\\\\\\\33[37m__       ')
  print('  _\33[36m\\///\33[37m______\33[36m\\//\\\\\\\33[37m___\33[36m/\\\\\\\33[37m____\33[36m\\//\\\\\\\33[37m________\33[36m/\\\\\\/\\\\\\\33[37m_____\33[36m\\/\\\\\\\33[37m_____\33[36m\\/\\\\\\\33[37m__      ')
  print('   ___________\33[36m/\\\\\\/\33[37m___\33[36m\\/\\\\\\\33[37m_____\33[36m\\/\\\\\\\33[37m______\33[36m/\\\\\\/\\/\\\\\\\33[37m_____\33[36m\\///\\\\\\\\\\\\\\\\\\/\33[37m___     ')
  print('    ________\33[36m/\\\\\\//\33[37m_____\33[36m\\/\\\\\\\33[37m_____\33[36m\\/\\\\\\\33[37m____\33[36m/\\\\\\/\33[37m__\33[36m\\/\\\\\\\33[37m______\33[36m/\\\\\\///////\\\\\\\33[37m__    ')
  print('     _____\33[36m/\\\\\\//\33[37m________\33[36m\\/\\\\\\\33[37m_____\33[36m\\/\\\\\\\33[37m__\33[36m/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\33[37m__\33[36m/\\\\\\\33[37m______\33[36m\\//\\\\\\\33[37m_   ')
  print('      ___\33[36m/\\\\\\/\33[37m___________\33[36m\\//\\\\\\\33[37m____\33[36m/\\\\\\\33[37m__\33[36m\\///////////\\\\\\//\33[37m__\33[36m\\//\\\\\\\33[37m______\33[36m/\\\\\\\33[37m__  ')
  print('       __\33[36m/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\33[37m__\33[36m\\///\\\\\\\\\\\\\\/\33[37m_____________\33[36m\\/\\\\\\\33[37m_____\33[36m\\///\\\\\\\\\\\\\\\\\\/\33[37m___ ')
  print('        _\33[36m\\///////////////\33[37m_____\33[36m\\///////\33[37m_______________\33[36m\\///\33[37m________\33[36m\\/////////\33[37m_____')
  print()
  print()
  
##############################################################################################################

### Displays menu in string format ###########################################################################
def display_menu():
  s = '\33[37m - - - - - - \33[36m(1) Start Game (1)\33[37m - - - - - -'
  i = '\33[37m - - - - - - \33[36m(2) Instructions (2)\33[37m - - - - - -'
  e = '\33[37m - - - - - - \33[36m(3) Exit Game (3)\33[37m - - - - - -'
  space = ''
  print(f'{space:8}{s:^80}')
  print(f'{space:8}{i:^80}')
  print(f'{space:8}{e:^80}')

##############################################################################################################
##############################################################################################################

space = ' '
user_in = ''

display_title()
display_menu()

print()
print(f'{space:>48}', end = '')
menu_input = input()

while(not (menu_input == '1' or menu_input == '2' or menu_input == '3')):
    print('Valid inputs are: "1", "2", "3"')
    menu_input = input('\33[37m')

while(menu_input == '2'):
  print(f'{space:>34}Instructions:')
  print('Input "u", "d", "l", "r" to shift the board up, down, left, or right respectively.')
  print(f'{space:>6}After each input, a two or four will appear on a random empty space.')
  print(f'{space:>17}Like numbers will combine when shifted together.')
  print(f'{space:>8}When the board is full, the game ends and your score is tallied.')
  print(f'{space:>3}At any point after starting the game, you may input "end" to end the game.')

  print()
  back = input(f'{space:>28}Enter anything to go back\n')
  print()
  print()

  os.system('cls')
  display_title()
  display_menu()
  menu_input = input()

if(menu_input == '1'):
  brd = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

  add_num(brd)
  os.system('cls')
  display_board(brd)


  while(board_not_full(brd) and user_in.lower() != 'end'):
    user_in = input('\33[37m')

    while(not (user_in.lower() == 'u' or user_in.lower() == 'd' or user_in.lower() == 'l' or user_in.lower() == 'r' or user_in.lower() == 'end')):
      print(f'{space:>23}Valid inputs are: "u", "d", "l", "r", or "end"')
      user_in = input('\33[37m')
    
    if(user_in.lower() == 'l'):
      combine_left(brd)
    elif(user_in.lower() == 'r'):
      combine_right(brd)
    elif(user_in.lower() == 'u'):
      combine_up(brd)
    elif(user_in.lower() == 'd'):
      combine_down(brd)
    elif(user_in.lower() == 'end'):
      break

    os.system('cls')
    add_num(brd)
    display_board(brd)
    print()
    print()
    
  score = 0
  for i in range(len(brd)):
      for q in range(len(brd)):
          score += brd[i][q]

  print(f'\33[36m{space:>35}Your Score:\33[37m {score}')
  print(f'\33[36m{space:>36}Good Job!')

  leave = input(f'{space:>31}Input "exit" to end\n')
  while(leave.lower() != 'exit'):
    leave = input(f'{space:>31}Input "exit" to end\n')
    
else:
  pass

