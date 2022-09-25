
# Bibliotheek importeren
import pygame

# Zorgen dat de code bij de items in de Pygame bibliotheek kan
pygame.init()

# Scherminstellingen
scherm_breedte = 800
scherm_hoogte = 600

# Kleuren voor de schermachtergrond (wit) en de teksten (zwart)
zwart = (0, 0, 0)
wit = (255, 255, 255)

# Kleuren van de startknop wanneer je wel/niet met de muis erover gaat
donker_groen = (0, 200, 0)
licht_groen = (0, 255, 0)

# Balk boven het scherm - toegevoegde naam en logo
startscherm = pygame.display.set_mode((scherm_breedte, scherm_hoogte))
pygame.display.set_caption('Team: nohtyp')
clock = pygame.time.Clock()

logo = pygame.image.load("RuimteschipLogo.png")
pygame.display.set_icon(logo)

