import turtle as t
import random
import time
from turtle import Turtle, Screen

def pingpong() :
    def message(m1, m2): 
        t.clear()
        t.goto(0,0) 
        t.write(m1, False, "center", ("", 30, "bold")) 
        t.goto(0,-70) 
        t.write(m2, False, "center", ("", 15))
    
    def right():
        if player.xcor() <200:
            player.forward(10)

    def left():
        if player.xcor() >-200:
            player.backward(10)

    def game_over():
        global playing  
        if playing == True:
            playing = False
            t.clear()
            t.goto(0,0)
            message("Game Over", "수고하셨습니다")
            t.onkeypress(None, "space")                    
                                                            
            
    def start():
        global playing
        if playing == False:            
            playing = True
            t.clear()         
            play()

    def play():
        global playing       
        ball_xspeed = 5
        ball_yspeed = 5
        Life = 3

        t.up()
        t.ht()
        t.goto(0,300)
        t.write(f"Life : {Life}", False, "center", ("",20))
        
        while playing == True:
             new_x = ball.xcor() + ball_xspeed
             new_y = ball.ycor() + ball_yspeed
             ball.goto(new_x, new_y)

             if ball.xcor() > 240 or ball.xcor() < -240:
                ball_xspeed *= -1

             if ball.ycor() > 340:
                ball_yspeed *= -1

             if ball.ycor() < -340:
                Life -= 1
                t.clear()
                t.write(f"Life : {Life}", False, "center", ("",20, ))                
                time.sleep(0.5)
                ball.goto(0,100)
                ball_xspeed *= -1
                ball_yspeed *= -1

                if Life == 0:
                    game_over()
                                  

             if player.distance(ball) < 50 and -260< ball.ycor() <-245:
                ball_yspeed *= -1
             
    t.bgcolor("white")
    t.setup(500,700)

    #플레이어
    player = t.Turtle()
    player.shape("square")
    player.shapesize(1, 5)
    player.up()
    player.speed(0)
    player.goto(0,-270)

    #ball
    ball = t.Turtle()
    ball.shape("circle")
    ball.shapesize(1.5)
    ball.up()
    ball.speed(0)
    ball.color("Blue")

    t.listen()
    t.onkeypress(right,"Right")
    t.onkeypress(left,"Left")
    t.onkeypress(start,"space")
    
    t.up()
    t.goto(0,0)
    t.ht()
    message("핑퐁 게임", "시작하려면 [Space]를 누르세요")
    

def snake():
    import turtle as t

    def message(m1, m2): # 메시지 출력
        t.clear() 
        t.goto(0,0) 
        t.write(m1, False, "center", ("", 30, "bold")) 
        t.goto(0,-70)  
        t.write(m2, False, "center", ("", 15)) 

    def start():
        global playing
        if playing == False: 
            playing = True 
            t.clear() 
            play() 

    def play(): 
        global playing 
        while playing == True: 
            screen.update()
            time.sleep(0.02)
            t.ht()
            for i in range(len(snakes) -1, 0, -1):
                snakes[i].goto(snakes[i-1].pos())

            snakes[0].forward(15)

            if snakes[0].distance(food) < 15:
                score_update()
                food.goto(rand_pos())
                creat_snake(snakes[-1].pos())

            if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 \
               or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
                playing == False
                game_over()

            for body in snakes[1:]:
                if snakes[0].distance(body) < 10:
                    playing == False
                    game_over()       
     

    # 방향키로 이동 : 반대 방향 변경금지
    def up():
        if snakes[0].heading() != 270:
            snakes[0].setheading(90)

    def down():
        if snakes[0].heading() != 90:
            snakes[0].setheading(270)

    def right():
        if snakes[0].heading() != 180:
            snakes[0].setheading(0)

    def left():
        if snakes[0].heading() != 0:
            snakes[0].setheading(180)

    # 뱀 몸통생성
    def creat_snake(pos):
        snake_body = Turtle()
        snake_body.shape("square")
        snake_body.color("orangered")
        snake_body.up()
        snake_body.goto(pos)
        snakes.append(snake_body)

    # 랜덤으로 먹이 생성
    def rand_pos():
        rand_x = random.randint(-250, 250)
        rand_y = random.randint(-250, 250)
        return rand_x, rand_y

    # 점수 업데이트 & 점수표시
    def score_update():      # 전역변수
        global score
        score += 1
        score_pen.clear()
        score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))


    def game_over():
        global score                                      # 전역변수
        global playing                                    # 전역변수
        if playing == True: 
            playing = False 
            score_pen.clear()           
            text = "당신의 기록은 : %d""점 입니다" % score         # 최종 점수를 text에 저장
            message("Game Over", text)                             # "Game Over"와 점수 출력                                            # 점수 초기화
            screen.onkeypress(None, "space")


    # 뱀의 몸 길어짐
    for pos in start_pos:
        creat_snake(pos)


    # 게임창 설정
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("yellowgreen")
    screen.title("Project_Snake Game")
    screen.tracer(0) # 화면갱신 중지


    # 점수표시
    score_pen = Turtle()
    score_pen.ht()        # 거북이 모양 숨겨주는 기능 하이드 터틀
    score_pen.up()
    score_pen.goto(-270, 250)
    score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))

    # 먹이 설정
    food = Turtle()
    food.shape("circle")
    food.color("snow")
    food.up()
    food.speed(0)
    food.shapesize(1, 1)
    food.goto(rand_pos()) # 랜덤한 위치로 나옴

    # 방향키로 뱀 이동
    screen.listen()
    screen.onkeypress(up, "Up")
    screen.onkeypress(down, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.onkeypress(start, "space")

    message("뱀 키우기 게임", "시작하려면 [Space]를 누르세요") # 게임 시작하기 전 화면 출력

# 변수값
start_pos = [(0,0), (-20,0), (-40,0)]
snakes = []
score = 0
playing = False


if __name__ == "__main__":
    print("원하시는 게임의 번호를 입력 후, enter키를 눌러주세요.")
    print("1.핑퐁 2.뱀")
    game = int(input())
    if game == 1:
        pingpong()
    elif game == 2:
        snake()

