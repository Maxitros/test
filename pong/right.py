from tkinter import *
# импортируем библиотеку random
import random
import socket 
from threading import Thread
# Добавляем глобальные переменные

# глобальные переменные
# настройки окна
WIDTH = 1280
HEIGHT = 720
 
# настройки ракеток
 
# ширина ракетки
LEFT_PAD_W = 0
PAD_W = 10
# высота ракетки
LEFT_PAD_H = 0
PAD_H = 100
 
# настройки мяча
# Насколько будет увеличиваться скорость мяча с каждым ударом
BALL_SPEED_UP = 1.0
# Максимальная скорость мяча
BALL_MAX_SPEED = 40
# радиус мяча
BALL_RADIUS = 30

INITIAL_SPEED = 10
BALL_X_SPEED = INITIAL_SPEED
BALL_Y_SPEED = INITIAL_SPEED

# Счет игроков
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0

left_comp_ip = input("Left computer ip")
middle_comp_ip = input("Middle computer ip")
right_comp_ip = input("Right computer ip")

SEND_IP_PORT1 = (left_comp_ip,10000)
SEND_IP_PORT2 = (middle_comp_ip,10002)
SEND_IP_PORT2_2 = (middle_comp_ip,10003)
SEND_IP_PORT3 = (right_comp_ip,10004)

RECV_IP_PORT1 = (left_comp_ip,11000)
RECV_IP_PORT2 = (middle_comp_ip,11001)
RECV_IP_PORT3 = (right_comp_ip,11002)



have_ball = True

def send() : 
    global BALL_X_CHANGE,BALL_Y_CHANGE,have_ball,BALL_X_SPEED,BALL_Y_SPEED
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    soc.bind(SEND_IP_PORT3)
    msg_l = c.coords(BALL)
    msg = str(msg_l[0]) + ',' + str(msg_l[1]) + ',' + str(msg_l[2]) + ',' + str(msg_l[3]) + ',' + str(BALL_X_SPEED) + ','+ str(BALL_Y_SPEED) + ',' + 'RIGHT'
    BALL_X_SPEED = 0
    BALL_Y_SPEED = 0
    msg =  msg.encode('UTF-8')
    soc.sendto(msg,RECV_IP_PORT2)
    have_ball = False
    c.coords(BALL,200,200,200,200)
def t_func_recv() : 
    global have_ball,BALL_Y_CHANGE,BALL_X_CHANGE,BALL_X_SPEED,BALL_Y_SPEED
    if have_ball == False :
        BALL_Y_SPEED = 0
        BALL_X_SPEED = 0
        soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        soc.bind(RECV_IP_PORT3)
        msg = soc.recv(1024)
        msg = msg.decode('UTF-8')
        msg = msg.split(',')
        print(msg)
        c.coords(BALL,50,msg[1],20,msg[3])

        BALL_Y_SPEED = float(msg[5])
        BALL_X_SPEED = 10
        have_ball = True
    if have_ball == True : 
        pass
    root.after(10,t_func_recv)

# Добавим глобальную переменную отвечающую за расстояние
# до правого края игрового поля
right_line_distance = WIDTH - PAD_W


def t_func_score_check():
    pass


def update_score(player):
    pass

def spawn_ball():
    global BALL_X_SPEED
    # Выставляем мяч по центру
    c.coords(BALL, WIDTH/2-BALL_RADIUS/2,
             HEIGHT/2-BALL_RADIUS/2,
             WIDTH/2+BALL_RADIUS/2,
             HEIGHT/2+BALL_RADIUS/2)
    # Задаем мячу направление в сторону проигравшего игрока,
    # но снижаем скорость до изначальной
    BALL_X_SPEED = 10
# функция отскока мяча
def bounce(action):
    global BALL_X_SPEED, BALL_Y_SPEED
    # ударили ракеткой
    if action == "strike":
        BALL_Y_SPEED = random.randrange(-10, 10)
        if abs(BALL_X_SPEED) < BALL_MAX_SPEED:
            BALL_X_SPEED *= -BALL_SPEED_UP
        else:
            BALL_X_SPEED = -BALL_X_SPEED
    else:
        BALL_Y_SPEED = -BALL_Y_SPEED


# устанавливаем окно
root = Tk()
root.title("PONG")
 
# область анимации
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()
 

 
# правая линия
c.create_line(WIDTH-PAD_W, 0, WIDTH-PAD_W, HEIGHT, fill="white")


 
# установка игровых объектов
 
# создаем мяч
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")
 
# левая ракетка
LEFT_PAD = c.create_line(LEFT_PAD_W/2, 0, LEFT_PAD_W/2, LEFT_PAD_H, width=LEFT_PAD_W, fill="yellow")
 
# правая ракетка
RIGHT_PAD = c.create_line(WIDTH-PAD_W/2, 0, WIDTH-PAD_W/2, 
                          PAD_H, width=PAD_W, fill="yellow")



# добавим глобальные переменные для скорости движения мяча
# по горизонтали
BALL_X_CHANGE = 20
# по вертикали
BALL_Y_CHANGE = 0
 
def move_ball():
    # определяем координаты сторон мяча и его центра
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center = (ball_top + ball_bot) / 2
 
    # вертикальный отскок
    # Если мы далеко от вертикальных линий - просто двигаем мяч
    if ball_right + BALL_X_SPEED < right_line_distance and \
            ball_left + BALL_X_SPEED > PAD_W:
        c.move(BALL, BALL_X_SPEED, BALL_Y_SPEED)
    # Если мяч касается своей правой или левой стороной границы поля
    elif ball_right == right_line_distance or ball_left == PAD_W:
        # Проверяем правой или левой стороны мы касаемся
        if ball_right > WIDTH / 2:
            # Если правой, то сравниваем позицию центра мяча
            # с позицией правой ракетки.
            # И если мяч в пределах ракетки делаем отскок
            if c.coords(RIGHT_PAD)[1] < ball_center < c.coords(RIGHT_PAD)[3]:
                bounce("strike")
            else:
                # Иначе игрок пропустил - тут оставим пока pass, его мы заменим на подсчет очков и респаун мячика
                update_score("right")
                spawn_ball()
        else:
            # То же самое для левого игрока
            if c.coords(LEFT_PAD)[1] < ball_center < c.coords(LEFT_PAD)[3]:
                bounce("strike")
            else:
                send()
    # Проверка ситуации, в которой мячик может вылететь за границы игрового поля.
    # В таком случае просто двигаем его к границе поля.
    else:
        if ball_right > WIDTH / 2:
            c.move(BALL, right_line_distance-ball_right, BALL_Y_SPEED)
        else:
            c.move(BALL, -ball_left+PAD_W, BALL_Y_SPEED)
    # горизонтальный отскок
    if ball_top + BALL_Y_SPEED < 0 or ball_bot + BALL_Y_SPEED > HEIGHT:
        bounce("ricochet")

# зададим глобальные переменные скорости движения ракеток
# скорось с которой будут ездить ракетки
PAD_SPEED = 20
# скорость левой платформы
LEFT_PAD_SPEED = 0
# скорость правой ракетки
RIGHT_PAD_SPEED = 0
 
# функция движения обеих ракеток
def move_pads():
    # для удобства создадим словарь, где ракетке соответствует ее скорость
    PADS = {LEFT_PAD: LEFT_PAD_SPEED, 
            RIGHT_PAD: RIGHT_PAD_SPEED}
    # перебираем ракетки
    for pad in PADS:
        # двигаем ракетку с заданной скоростью
        c.move(pad, 0, PADS[pad])
        # если ракетка вылезает за игровое поле возвращаем ее на место
        if c.coords(pad)[1] < 0:
            c.move(pad, 0, -c.coords(pad)[1])
        elif c.coords(pad)[3] > HEIGHT:
            c.move(pad, 0, HEIGHT - c.coords(pad)[3])

 
def main():
    move_ball()
    move_pads()
    # вызываем саму себя каждые 30 миллисекунд
    root.after(30, main)

# Установим фокус на Canvas чтобы он реагировал на нажатия клавиш
c.focus_set()
 
# Напишем функцию обработки нажатия клавиш
def movement_handler(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym == "w":
        LEFT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "s":
        LEFT_PAD_SPEED = PAD_SPEED
    elif event.keysym == "Up":
        RIGHT_PAD_SPEED = -PAD_SPEED
    elif event.keysym == "Down":
        RIGHT_PAD_SPEED = PAD_SPEED
 
# Привяжем к Canvas эту функцию
c.bind("<KeyPress>", movement_handler)
 
# Создадим функцию реагирования на отпускание клавиши
def stop_pad(event):
    global LEFT_PAD_SPEED, RIGHT_PAD_SPEED
    if event.keysym in "ws":
        LEFT_PAD_SPEED = 0
    elif event.keysym in ("Up", "Down"):
        RIGHT_PAD_SPEED = 0
 
# Привяжем к Canvas эту функцию
c.bind("<KeyRelease>", stop_pad)

# запускаем движение
main()
 

t1 = Thread(target=t_func_recv)
t1.start()

t2 = Thread(target=t_func_score_check)
t2.start()

# запускаем работу окна
root.mainloop()
