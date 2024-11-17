import pgzrun,random

WIDTH = 750
HEIGHT = 750

TITLE = "Alien Shooting"

alien = Actor("alien-removebg-preview.png", (WIDTH/2, HEIGHT/2))
alien2 = Actor("alien-removebg-preview.png", (WIDTH/2, HEIGHT/2))
message = "Shoot the Aliens to save the planet!"

def draw():
    screen.fill(color = "black")
    alien.draw()
    alien2.draw()
    screen.draw.text(message, center = (375, 25), fontsize = 30)
    
    alien.x = random.randint(50, WIDTH-50)
    alien.y = random.randint(50, HEIGHT-50)
    alien2.x = random.randint(100, WIDTH-50)
    alien2.y = random.randint(100, HEIGHT-50)
    
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos) or alien2.collidepoint(pos):
        message = "Good Shot!"
    else:
        message = "You Missed!"        
pgzrun.go()