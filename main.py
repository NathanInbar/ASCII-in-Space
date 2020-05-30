import pygame, random
import math

pygame.font.init()
font = pygame.font.SysFont("Comic Sans", 23)

WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated ASCII Background")
m_x, m_y = pygame.mouse.get_pos()

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
class Agent:
    def __init__(self, char, x, y, xVel, yVel, color=(255,255,255), colorChange=60):
        self.char = char
        self.x = x
        self.y = y
        self.xVel = xVel
        self.yVel = yVel
        self.color = color

    def update(self):
        self.x += self.xVel
        self.y += self.yVel
        #infin. scroll
        if self.x > WIDTH:
            self.x = -15
        if self.y > HEIGHT:
            self.y = -15
        # - - -
        d = calculateDistance(self.x,self.y,m_x,m_y)#distance from mouse
        d = 255 - d
        if d<30:
            d=30
        if d>255:
            d=255
        self.color = (d,d,d)

    def render(self, win, font):
        text = font.render(self.char, 1, self.color, True)
        win.blit(text,(self.x,self.y))
# - - -
bkg_dark = (10,10,10)
earth = pygame.image.load("Earth.png")
earthX,earthY = earth.get_rect().size
agents = []

def spawn_agents():
    def create_agent(char, xVel, yVel):#char, maxXvel, maxYvel
        r_x = random.randrange(0,WIDTH)
        r_y = random.randrange(0,HEIGHT)
        r_xv = random.randrange(0,xVel)
        r_yv = random.randrange(0,yVel)

        return Agent(char,r_x,r_y, r_xv/10000, r_yv/10000)
    for x in range(30):
        agents.append(create_agent('@',50,200))
        agents.append(create_agent('+',20,200))
        agents.append(create_agent(',',10,100))
        agents.append(create_agent('#',20,150))
        agents.append(create_agent('-',10,100))
        agents.append(create_agent('.',10,100))
        agents.append(create_agent('\'',10,100))

def update():
    global m_x,m_y
    m_x, m_y = pygame.mouse.get_pos()
    for agent in agents:
        agent.update()

def render():
    win.fill(bkg_dark)
    for agent in agents:
        agent.render(win, font)
    win.blit(earth,(305, 225))
    pygame.display.update()

def main():
    run = True
    spawn_agents()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        update()
        render()
main()
