# This Code Is Written By Harsh Kumar
# As an Assignment Submitted to Science And Technology Club

import curses
import random
import time
​

window = curses.initscr()

curses.curs_set(0)
​
win_height, win_width = window.getmaxyx()
​
new_win = curses.newwin(win_height, win_width, 0, 0)
​
new_win.keypad(True)
​
new_win.timeout(150)
​
for i in range(win_width-1):
    new_win.addch(0, i, curses.ACS_BOARD)
    new_win.addch(win_height-1,i, curses.ACS_BOARD)
for i in range(win_height-1):
    new_win.addch(i, 0, curses.ACS_BOARD)
    new_win.addch(i, win_width-1, curses.ACS_BOARD)
​
snake_x = win_width/6
snake_y = win_height/3
​
snake = [
    [snake_y,snake_x],
    [snake_y,snake_x-1],
    [snake_y,snake_x-2]
]
​
food = [win_height//4, win_width//4]
​

new_win.addch(food[0], food[1], curses.ACS_PLUS) 
​
key = curses.W


while True:
    next_key = new_win.getch() 
    key = key if next_key == -1 else next_key
​
    
    if snake[0][0] in [1,win_height-1] or snake[0][1] in [1,win_width-1] or snake[0] in snake[1:]:
        curses.beep()
        time.sleep(5)
        curses.endwin()
        quit()
   
    if key == curses.S:
        new_head = [snake[0][0] + 1, snake[0][1]]
    if key == curses.W:
        new_head = [snake[0][0] - 1, snake[0][1]]
    if key == curses.A:
        new_head = [snake[0][0], snake[0][1] - 1]
    if key == curses.D:
        new_head = [snake[0][0], snake[0][1] + 1]
    
   
    snake.insert(0, new_head)
​
   
    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, win_height-4),
                random.randint(1, win_width-4)
            ]
            food = new_food if new_food not in snake else None
        
        new_win.addch(food[0], food[1], curses.ACS_PLUS)
    else:
        tail = snake.pop()
        new_win.addch(int(tail[0]), int(tail[1]), ' ')
​
    new_win.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_LANTERN)  