import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set up the game window
run = True
FPS = 60
clock = pygame.time.Clock()
     
class player():
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = WIDTH//2
        self.y = 170 #HEIGHT//2 - self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.velocity = 0 # Player's vertical velocity
        self.Gravity = 0.5 # Gravity affecting the player
        self.jump_strength = -5  # Jump strength when space is pressed
        
        self.stop = False # Flag to stop player movement
        self.keypressed = False # Flag to track if space is pressed 
        self.alive = True # Flag to track if the player is alive
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

    def gravity(self):
        keys = pygame.key.get_pressed()
        self.rect.y += self.velocity # Update the player's vertical position
        
        if self.alive == True and self.keypressed == True:  # Apply gravity if alive and space was pressed
            self.velocity += self.Gravity
        else:
            self.keypressed = False
                
        if self.alive == True: # Allow jumping if alive
            if keys[pygame.K_SPACE]:
                self.keypressed = True
                if not self.stop:
                    self.velocity = self.jump_strength
        else:      
            self.keypressed = False    

        if self.rect.y + self.height >= HEIGHT:   # Check if the player hits the ground
            self.rect.y = HEIGHT - self.height
            self.alive = False # Set alive to False
            #stop the pillers and theyer movement
            pillar_rectangles.stop = True
            pillar_rectangles.keypressed = True
            pillar_rectangles.is_alive = False
            pillar_rectangles.top_y = 0
            pillar_rectangles.bottom_y = 0
            
            pillar_rectangles.restart() # Restart the pillars
            
            
        if self.alive == False:
            # Display Game Over message if not alive
            text = pygame.font.SysFont('Arial', 30).render('Game Over... press r to restart', True, (255, 0, 0))
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            
            self.stop = True # Stop player movement
            self.velocity += self.Gravity # Apply gravity even after death
            self.keypressed = False # Disable space bar input

class pillars():
    def __init__(self):
        self.gap = 100
        self.gap_y = random.randint(self.gap//2,HEIGHT - self.gap//2)
        self.width = 50
        self.top_height = self.gap_y-self.gap//2
        self.bottom_y = self.gap_y + self.gap // 2
        self.bottom_height = HEIGHT - self.bottom_y
        self.x = random.randint(WIDTH, WIDTH + 10)
        self.top_y = 0
        self.speed = 3
        self.x_speed = 0
        
        self.rects = [pygame.Rect(self.x, self.top_y, self.width, self.top_height)
                      , pygame.Rect(self.x, self.bottom_y, self.width, self.bottom_height)]
        
        self.stop = False
        self.keypressed = False
        self.is_alive = True
    def draw(self,screen):
        for rect in self.rects:
            pygame.draw.rect(screen, (0, 0, 180), rect)        

    def move(self):
        for rect in self.rects: # Move all pillar rectangles horizontally
            rect.x += self.x_speed
      
    def move_left(self):
        key = pygame.key.get_pressed()
        
        if self.stop == False and self.keypressed == False:
            if key[pygame.K_SPACE]:
                self.x_speed = -self.speed
        
        elif self.stop == True and self.keypressed == True:
            self.x_speed = 0
      
    def repeat(self):
        for rect in self.rects:  # Move all pillar rectangles horizontally
            rect.x += self.x_speed
        
        if self.rects[-1].x <WIDTH //2: # Check if the last pillar is past the middle of the screen
            self.gap_y = random.randint(self.gap//2, HEIGHT - self.gap//2)
            self.top_height = self.gap_y - self.gap // 2
            self.bottom_y = self.gap_y + self.gap // 2
            self.bottom_height = HEIGHT - self.bottom_y
            self.x = random.randint(WIDTH, WIDTH + 10)
            self.top_y = 0
            
            self.new_top_rect = pygame.Rect(self.x, self.top_y, self.width, self.top_height)
            self.new_bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, self.bottom_height)

            self.rects.append(self.new_top_rect)
            self.rects.append(self.new_bottom_rect)
            
            
        if self.rects[0].x + self.rects[0].width < 0:
            self.rects.pop(0) # Remove pillars that move off-screen
           
    
    def restart(self):
        if self.is_alive == False:
            text = pygame.font.SysFont('Arial', 30).render('Game Over... press r to restart', True, (255, 0, 0))
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]: # Restart the game if "R" is pressed
                self.is_alive = True
                self.stop = False  
                self.keypressed = False
                self.x = random.randint(WIDTH, WIDTH + 10)
                self.top_y = 0
                self.speed = 3
                self.x_speed = 0
                self.rects = [pygame.Rect(self.x, self.top_y, self.width, self.top_height)
                      , pygame.Rect(self.x, self.bottom_y, self.width, self.bottom_height)]
                          
                player_rectangle.alive = True            
                player_rectangle.stop = False
                player_rectangle.keypressed = False         
                player_rectangle.alive = True
                player_rectangle.x = WIDTH//2
                player_rectangle.y = 170
                player_rectangle.rect = pygame.Rect(player_rectangle.x, player_rectangle.y, player_rectangle.width, player_rectangle.height)
                player_rectangle.velocity = 0
                player_rectangle.Gravity = 0.5
                player_rectangle.jump_strength = -5   
                       
player_rectangle = player()
pillar_rectangles = pillars()

while run:       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill('black')  # Fill with black color
 
    pillar_rectangles.draw(screen)
    pillar_rectangles.move_left()
    pillar_rectangles.repeat()
    
    player_rectangle.draw()
    player_rectangle.gravity()
    pillar_rectangles.restart()
    
    for rect in pillar_rectangles.rects: 
        if player_rectangle.rect.colliderect(rect): # Collision detected
            pillar_rectangles.stop = True # Stop the pillars
            pillar_rectangles.keypressed = True # Disable pillar movement
            pillar_rectangles.is_alive = False  # Set pillars' alive state to False
            pillar_rectangles.top_y = 0
            pillar_rectangles.bottom_y = 0
            player_rectangle.alive = False # Set player alive state to False
            player_rectangle.keypressed = False  # Disable space bar input
    
    pygame.display.flip() # Update the display
    clock.tick(FPS)

pygame.quit()