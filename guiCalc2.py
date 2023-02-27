# Imports
import sys
import pygame

# Basic setup
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 800,600
screen = pygame.display.set_mode((width, height))
# Define fonts for text
font = pygame.font.SysFont('Arial', 32)
sysfont = pygame.font.get_default_font()
# Define variables and lists
inputBox = []
answerBox = ()
ans = " "

objects = []
# Create class Button - allow parameter input
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
# 		set colours for different button states in hex format
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
    def process(self):
		# code for different states of button - normal, hover and pressed
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
# code excecuted when clicking buttons
def press1():
    inputBox.append("1")
def press2():
    inputBox.append("2")
def press3():
    inputBox.append("3")
def press4():
    inputBox.append("4")
def press5():
    inputBox.append("5")
def press6():
    inputBox.append("6")
def press7():
    inputBox.append("7")
def press8():
    inputBox.append("8")
def press9():
    inputBox.append("9")
def press0():
    inputBox.append("0")
def pressplus():
    inputBox.append("+")
def pressminus():
    inputBox.append("-")
def pressmul():
    inputBox.append("*")
def pressdiv():
    inputBox.append("/")
def pressdec():
    inputBox.append(".")
def pressobrac():
    inputBox.append("(")
def presscbrac():
    inputBox.append(")")
def pressclr():
    inputBox.clear()
def pressdel():
	try:
		inputBox.pop() # pop removes last item from list
	except:
		pass # to prevent errors when list is empty, pass function used
def presssolv():
	global ans # global decleration needed here, or the ans variable won't be updated properly
	try:
		ans = eval(''.join(inputBox))
	except:
		ans = "Error" # prevents crashing when there is an error in calculations


# code for creating each of the buttons on the calculator
Button(90,150, 60, 60, '1', press1)
Button(180,150, 60, 60, '2', press2)
Button(270,150, 60, 60, '3', press3)
Button(360,150, 60, 60, '+', pressplus)
Button(90,250, 60, 60, '4', press4)
Button(180,250, 60, 60, '5', press5)
Button(270,250, 60, 60, '6', press6)
Button(360,250, 60, 60, '-', pressminus)
Button(90,350, 60, 60, '7', press7)
Button(180,350, 60, 60, '8', press8)
Button(270,350, 60, 60, '9', press9)
Button(360,350, 60, 60, '*', pressmul)
Button(90,450, 60, 60, '0', press0)
Button(180,450, 60, 60, 'C', pressclr)
Button(270,450, 60, 60, '=', presssolv)
Button(360,450, 60, 60, '/', pressdiv)
Button(450,450, 60, 60, '.', pressdec) 
Button(450,350, 60, 60, ')', presscbrac) 
Button(450,250, 60, 60, '(', pressobrac) 
Button(450,150, 60, 60, 'DEL', pressdel) 


# main loop that runs after setup scripts finish
while True:
    screen.fill((20, 20, 20)) #  background colour in RGB format
  
  # font rendering for boxes - colour white using RGB format
    ansBox = font.render(str(ans), True, (255,255,255))
    inpBox = font.render((''.join(inputBox)), True, (255,255,255))


#   draws the input and answer boxes at specified coordinates
    screen.blit(inpBox, (20, 20))
    screen.blit(ansBox, (20,60))
    # allows quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects: # loops for each object in the object list and executes them
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)
