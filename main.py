import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 20
LINE_HEIGHT = FONT_SIZE + 5  # Définir LINE_HEIGHT ici

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Coran Matrix')

# Set up the font
font = pygame.font.SysFont('monospace', FONT_SIZE)

# Get the absolute path to the Quran text file
current_dir = os.path.dirname(__file__)
quran_file = os.path.join(current_dir, 'quran-simple.txt')

# Check if the Quran text file exists
if not os.path.exists(quran_file):
    print(f"Error: {quran_file} not found.")
    pygame.quit()
    sys.exit()

# Load the text of the Quran
with open(quran_file, 'r', encoding='utf-8') as f:
    quran_text = f.read()

# Function to create matrix columns
def create_matrix_columns(screen, text, font, line_height):
    columns = []
    for x in range(0, SCREEN_WIDTH, FONT_SIZE):
        column_text = random.sample(text, len(text))
        column = {'x': x, 'y': random.randint(-SCREEN_HEIGHT, 0), 'text': column_text, 'speed': random.randint(2, 5)}
        columns.append(column)
    return columns

# Create the initial columns
columns = create_matrix_columns(screen, quran_text, font, LINE_HEIGHT)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for column in columns:
        column['y'] += column['speed']
        if column['y'] > SCREEN_HEIGHT:
            column['y'] = random.randint(-SCREEN_HEIGHT, 0)
            column['speed'] = random.randint(2, 5)
        
        for i, char in enumerate(column['text']):
            if column['y'] + i * LINE_HEIGHT < SCREEN_HEIGHT:  # Utiliser LINE_HEIGHT ici
                color = (0, 255, 0)
                char_surface = font.render(char, True, color)
                screen.blit(char_surface, (column['x'], column['y'] + i * LINE_HEIGHT))
            else:
                break

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()
