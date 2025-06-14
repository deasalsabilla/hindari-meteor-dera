import turtle
import random
import time

# === Setup layar ===
screen = turtle.Screen()
screen.title("Hindari Meteor")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# === Pemain (Pesawat) ===
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)
player.hideturtle()  # disembunyikan sampai game mulai

# === Meteor ===
meteor = turtle.Turtle()
meteor.shape("circle")
meteor.color("orange")
meteor.penup()
meteor.speed(0)
meteor.shapesize(1.5, 1.5)
meteor.hideturtle()  # disembunyikan sampai game mulai

# === Skor dan Level ===
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.color("white")
score_writer.penup()
score_writer.goto(0, 260)

# === Game Over / Intro Text ===
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.color("red")
game_over.penup()

# === Judul Game di Awal ===
intro = turtle.Turtle()
intro.hideturtle()
intro.color("white")
intro.penup()
intro.goto(0, 0)
intro.write("HINDARI METEOR\n\nTekan 'Spasi' untuk Memulai", align="center", font=("Arial", 20, "bold"))

# === Gerakan pemain ===
def go_left():
    x = player.xcor() - 30
    if x < -280:
        x = -280
    player.setx(x)

def go_right():
    x = player.xcor() + 30
    if x > 280:
        x = 280
    player.setx(x)

screen.listen()
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# === Game Start Function ===
def start_game():
    intro.clear()
    player.goto(0, -250)
    player.showturtle()
    meteor.goto(random.randint(-280, 280), 280)
    meteor.showturtle()

    score = 0
    level = 1
    fall_speed = 3
    start_time = time.time()

    game_over.clear()
    game_running = True

    while game_running:
        screen.update()

        meteor.sety(meteor.ycor() - fall_speed)

        if meteor.ycor() < -300:
            meteor.goto(random.randint(-280, 280), 280)

        if meteor.distance(player) < 30:
            game_running = False
            break

        current_time = int(time.time() - start_time)
        score = current_time
        level = 1 + score // 10
        fall_speed = 3 + level - 1

        score_writer.clear()
        score_writer.write(f"Score: {score}  Level: {level}", align="center", font=("Arial", 16, "bold"))

        time.sleep(0.02)

    game_over.goto(0, 0)
    game_over.write(f"GAME OVER\nSkor Akhir: {score}\nTekan 'Spasi' untuk Main Lagi", align="center", font=("Arial", 18, "bold"))

# === Event tekan spasi untuk mulai atau restart ===
def restart():
    score_writer.clear()
    game_over.clear()
    start_game()

screen.onkeypress(restart, "space")

# === Jangan langsung mulai ===
# Tampilkan intro dan tunggu spasi
screen.mainloop()
