
import pygame 
 
def main():

    class MainCharacter:
        def __init__(self):
            self.name = "Main Character"
        
        def render(self):
            screen.blit(blueImg, (x,y))
    
    
    class Heart:        
    
        def __init__(self, x_val, y_val):
            self.name = "Heart"
            
            self.count = 0
            
            self.x = x_val
            self.y = y_val
        
        def render(self):
            screen.blit(heartImg, (self.x,self.y)) 
        
        def rotate(self,radius):
        
            radval = abs(radius)
            sign = radius/radval
            
            if (self.count < (30 * radval)):
                self.x += 1 * sign
                self.count += 1
            elif (self.count < (60 * radval)):
                self.y += 1 * sign
                self.count += 1
            elif (self.count < (90 * radval)):
                self.x -= 1 * sign
                self.count += 1
            elif (self.count < (120 * radval)):
                self.y -= 1 * sign
                self.count += 1
            else:
                self.count = 0
                
            
    pygame.init()

    logo = pygame.image.load("assets/blue sprite.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Demo')
     
    screen = pygame.display.set_mode((512,512))
    
    grassImg = pygame.image.load('assets/grass.png')
    blueImg = pygame.image.load('assets/blue sprite.png')
    heartImg = pygame.image.load('assets/heart sprite.png')
    
    x = 175
    y = 175
    
    x_leftchange = 0
    x_rightchange = 0
    y_upchange = 0
    y_downchange = 0
    
    clock = pygame.time.Clock()
    
    mainchar = MainCharacter()
    
    heart1 = Heart(25, 25) 
    heart2 = Heart(150, 350)
    heart3 = Heart(350, 125)
     
    running = True
    
    while running:
    
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
               
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_leftchange = -2
                elif event.key == pygame.K_RIGHT:
                    x_rightchange = 2  
                elif event.key == pygame.K_UP:
                    y_upchange = -2
                elif event.key == pygame.K_DOWN:
                    y_downchange = 2
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_leftchange = 0
                    
                if event.key == pygame.K_RIGHT:    
                    x_rightchange = 0
                    
                if event.key == pygame.K_UP:
                    y_upchange = 0
                    
                if event.key == pygame.K_DOWN:
                    y_downchange = 0    
                    
     
        screen.fill((255,255,255))
        
        screen.blit(grassImg, (0,0))
        
        heart1.render()
        heart2.render()
        heart3.render()
        
        heart1.rotate(3)
        heart2.rotate(2)
        heart3.rotate(-2)
        
        mainchar.render()
        
        x += x_leftchange
        x += x_rightchange
        y += y_upchange
        y += y_downchange
        
        pygame.display.update()
        clock.tick(120)
        
    pygame.quit()
    quit()
     
if __name__=="__main__":

    main()