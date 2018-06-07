from PIL import Image, ImageDraw, ImageFont
import math
import sys
import pygame
import time
import os

font = ImageFont.truetype("MarkPro-Bold.otf", 120, encoding='unic')

def create_image(char, font):
    w, h = font.getsize(char)
    img = Image.new('RGB', (w + 10, h + 10), 'white')
    draw = ImageDraw.Draw(img)
    draw.text((5,5), char, 'black', font)
    return img

def stretch_glyph(char, font, ratiox=0.5, ratioy=1, gap=100):
    img = create_image(char, font)
    old_size = img.size
    imgdata = img.load()
    x = math.floor(old_size[0]*ratiox)
    y = math.floor(old_size[1]*ratioy)

    img_left = img.copy().crop((0, 0, int(old_size[0]*ratiox), old_size[1]))
    img_right = img.copy().crop((int(old_size[0]*ratiox),0,old_size[0],old_size[1]))

    new_size = (old_size[0] + gap, old_size[1])
    new_img = Image.new(img.mode, new_size, 'white')
    new_img.paste(img_left, (0,0))
    new_img.paste(img_right, (int(math.ceil(old_size[0]*ratiox)+gap), 0))

    pixels = []
    for i in range(old_size[1]):
        pixels.append(img.getpixel((x,i)))

    data = new_img.load()
    minx = int(math.floor(old_size[0]*ratiox))
    maxx = int(math.ceil(old_size[0]*ratiox) + gap)
    for i in range(minx, maxx):
        for j in range(old_size[1]):
           data[i, j] = pixels[j] 
        
    return new_img

def show_glyph(char, font):
    img = create_image(char,font)
    img.show()
    return img

def show_stretch(char, font, ratiox=0.5, gap=100):
    img = stretch_glyph(char, font, ratiox=ratiox, gap=gap)
    img.show()

def clear(screen):
    screen.fill((0,0,0))

def show_char(screen, char):
    img = create_image(char, font)
    raw_str = img.tobytes()
    pygame_surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    screen.blit(pygame_surface, (0,0))
    pygame.display.update()

def show_stretched_char(screen, char, gap=0):
    img = stretch_glyph(char, font, gap=gap)
    raw_str = img.tobytes()
    pygame_surface = pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    screen.blit(pygame_surface, (0,0))
    pygame.display.update()

def main():
    global font
    
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        fontfile = sys.argv[1]
        font = ImageFont.truetype(fontfile, 120, encoding='unic')

    pygame.init()
    print("Press ESC to exit.")

    screen = pygame.display.set_mode((500,200))
    clock = pygame.time.Clock()

    running = True

    alphabet = [ key for key in range(pygame.K_a, pygame.K_z + 1) ]
    num = [ key for key in range(pygame.K_0, pygame.K_9 + 1) ] 

    stretching = False
    gap = 0
    char = None
    prev_char = None
    last_stretch = None
    while running:
        stretchclock = time.clock()
        if stretching and prev_char and stretchclock - last_stretch >= 0.1:
            gap += 10
            clear(screen)
            show_stretched_char(screen, prev_char, gap=gap)
            last_stretch = stretchclock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in alphabet or event.key in num:
                    gap = 0
                    char = pygame.key.name(event.key)
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        char = char.upper()    
                    clear(screen)
                    show_char(screen, char)
                    prev_char = char
                elif event.key == pygame.K_LCTRL and prev_char:
                    gap += 10
                    last_stretch = time.clock()
                    clear(screen)
                    show_stretched_char(screen, prev_char, gap=gap)
                    stretching = True
                elif event.key == pygame.K_LSHIFT and prev_char:
                    gap = 0
                    clear(screen)
                    show_char(screen, prev_char)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL and prev_char:
                    stretching = False
        clock.tick(30)


    pygame.quit()

main()

