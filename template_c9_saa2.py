import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["cloud"] = pygame.image.load("cloud.png").convert_alpha()

bird=pygame.Rect(100,250,30,30)
groundx=0

# Create a variable 'cloudx' and initialize it to 300


while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-550:
      groundx=0
  screen.blit(images["ground"],[groundx,550]) 
  screen.blit(images["bird"],bird)
  
  # Decrement 'cloudx' by 3
  
  # Check if 'cloudx' is less than -100
  
      # Reset the value 'cloudx' back to 300
      
  # Display the cloud image at [cloudx,150]
  
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
        
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
