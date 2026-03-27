# ╭─────────────────────────────────────────────────────────────────────────────────╮
# │ Screensaver Star Eagle | Protetor de Tela Estelar - Versão para Linux e Windows │
# ╰─────────────────────────────────────────────────────────────────────────────────╯

version = "1.0"
# The MIT License (MIT)
Author = "Copyright (C) 2026 Jayme Gonçalves"
Repo = "https://github.com/Jayme-G/SCR_StarEagle"

import pygame
import random
import math
import sys
import os
import configparser

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ===================== CONFIGURAÇÕES =====================
DEFAULT_CONFIG = {
    'NUM_STARS': 500,
    'MAX_Z': 100.0,
    'MIN_Z': 1.0,
    'DEFAULT_SPEED': 0.5,
    'SCREEN_WIDTH': 1920,
    'SCREEN_HEIGHT': 1080,
    'MAX_STAR_SIZE': 5.0,
    'STAR_COLORS': [(127, 0, 255), (0, 127, 255), (0, 0, 255)],
    'MUSIC_ENABLED': True,
    'MUSIC_FILE': 'musica.mp3',
    'IMAGE_ENABLED': True,
    'IMAGE_FILE': 'imagem.png',
    'FPS_LIMIT': 60,
    'BACKGROUND_COLOR': (0, 0, 0),
}

def load_config():
    config = DEFAULT_CONFIG.copy()
    config_path = resource_path("config.ini")

    if os.path.exists(config_path):
        try:
            parser = configparser.ConfigParser()
            parser.read(config_path, encoding='utf-8')
            if 'Settings' in parser:
                section = parser['Settings']

                # Inteiros
                for key in ['NUM_STARS', 'SCREEN_WIDTH', 'SCREEN_HEIGHT', 'FPS_LIMIT']:
                    if key in section:
                        try:
                            config[key] = int(section[key])
                        except ValueError:
                            pass

                # Floats
                for key in ['MAX_Z', 'MIN_Z', 'DEFAULT_SPEED', 'MAX_STAR_SIZE']:
                    if key in section:
                        try:
                            config[key] = float(section[key])
                        except ValueError:
                            pass

                # Cores das estrelas
                if 'STAR_COLORS' in section:
                    color_str = section['STAR_COLORS']
                    colors = []
                    for c in color_str.split(';'):
                        c = c.strip()
                        if c:
                            try:
                                rgb = tuple(int(x.strip()) for x in c.split(','))
                                if len(rgb) == 3:
                                    colors.append(rgb)
                            except ValueError:
                                pass
                    if colors:
                        config['STAR_COLORS'] = colors

                # Booleanos
                if 'MUSIC_ENABLED' in section:
                    try:
                        config['MUSIC_ENABLED'] = section.getboolean('MUSIC_ENABLED')
                    except:
                        pass
                if 'IMAGE_ENABLED' in section:
                    try:
                        config['IMAGE_ENABLED'] = section.getboolean('IMAGE_ENABLED')
                    except:
                        pass

                # Cor de fundo
                if 'BACKGROUND_COLOR' in section:
                    bg_str = section['BACKGROUND_COLOR'].strip()
                    try:
                        bg = tuple(int(x.strip()) for x in bg_str.split(','))
                        if len(bg) == 3:
                            config['BACKGROUND_COLOR'] = bg
                    except ValueError:
                        pass

                # Configuração de musica
                if 'MUSIC_FILE' in section:
                    config['MUSIC_FILE'] = section['MUSIC_FILE'].strip()

                # Configuração de imagem
                if 'IMAGE_FILE' in section:
                    config['IMAGE_FILE'] = section['IMAGE_FILE'].strip()

        except Exception as e:
            print(f"Erro ao carregar config.ini: {e}. Usando padrões.")
    else:
        print(f"config.ini não encontrado em {config_path}. Criando arquivo com configurações padrão...")
        create_default_config(config_path)

    return config

def create_default_config(path):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"""[Settings]
# ╭──────────────────────────────────────────────────────────────────────────────────────────────────╮
# │ Configurações do Screensaver Star Eagle | Protetor de Tela Estelar - Versão para Linux e Windows │
# ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
#
# Versão {version}
# The MIT License (MIT)
# Copyright (C) 2026 {Author}
# Repositório: {Repo}
#
# Edite os valores abaixo e salve o arquivo.
# O jogo carrega os valores automaticamente ao ser executado.
# Para retornar para as configurações padrão, basta excluir este arquivo.

# Quantidade de estrelas (recomendado: 100 a 2000)                    
NUM_STARS = 500

# Mais ou menos profundidade de estrelas (recomendado: 30.0 a 200.0)              
MAX_Z = 100.0
                    
# Estrelas chegam muito perto / bem longe (recomendado: 0.5 a 10)
MIN_Z = 1.0

# Velocidade base das estrelas (quanto maior, mais rápidas)                    
DEFAULT_SPEED = 0.5
                  
# Resolução da tela (ajuste conforme a resolução da sua tela ou para ganho de desempenho)                   
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Tamanho máximo das estrelas                    
MAX_STAR_SIZE = 5.0

# Cores das estrelas (R,G,B) separadas por ; 
# Exemplo com mais cores: 0,255,0;255,255,255;255,0,0;0,0,255;255,255,0;255,165,0                    
STAR_COLORS = 127,0,255;0,127,255;0,0,255

                    
# True = música ligada | False = música desligada                    
MUSIC_ENABLED = True

# Nome do arquivo da música (deve estar na mesma pasta do executável)
# Pode ser "musica.mp3", "som.wav", "toque.mid", "trilha.ogg", etc.
MUSIC_FILE = musica.mp3

# True = imagem central animada | False = sem imagem                    
IMAGE_ENABLED = True

# Nome do arquivo da imagem central (deve estar na mesma pasta do executável)
# Pode ser "imagem.png", "logo.jpg", "foto.bmp", etc.
IMAGE_FILE = imagem.png

# Limite de frames por segundo (60 é ótimo. Valores menores melhoram desempenho)                    
FPS_LIMIT = 60

# Cor de fundo (R,G,B) - 0,0,0 = preto                    
BACKGROUND_COLOR = 0,0,0

""")
        print(f"✅ config.ini criado com sucesso em: {path}")
    except Exception as e:
        print(f"❌ Não foi possível criar config.ini: {e}")

# Carrega as configurações (executado automaticamente)
config = load_config()

# Aplica nas variáveis globais
NUM_STARS = config['NUM_STARS']
MAX_Z = config['MAX_Z']
MIN_Z = config['MIN_Z']
DEFAULT_SPEED = config['DEFAULT_SPEED']
SCREEN_WIDTH = config['SCREEN_WIDTH']
SCREEN_HEIGHT = config['SCREEN_HEIGHT']
MAX_STAR_SIZE = config['MAX_STAR_SIZE']
STAR_COLORS = config['STAR_COLORS']
MUSIC_FILE = config['MUSIC_FILE']
IMAGE_FILE = config['IMAGE_FILE']

class Star:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.speed = 0.0
        self.color = (255, 255, 255)
        self.reset()

    def reset(self):
        self.x = random.uniform(-MAX_Z, MAX_Z)
        self.y = random.uniform(-MAX_Z, MAX_Z)
        self.z = random.uniform(MIN_Z, MAX_Z)
        self.speed = DEFAULT_SPEED + random.uniform(0.0, 1.0)
        self.color = random.choice(STAR_COLORS)

    def update(self):
        self.z -= self.speed
        if self.z < MIN_Z:
            self.reset()

    def draw(self, screen):
        scale = 1000.0 / self.z
        x_pos = int(self.x * scale + SCREEN_WIDTH / 2)
        y_pos = int(self.y * scale + SCREEN_HEIGHT / 2)
        
        depth_factor = 1.0 - self.z / MAX_Z
        brightness = int(150 + 105 * depth_factor)
        size = MAX_STAR_SIZE * depth_factor + 1.0

        if (0 <= x_pos < SCREEN_WIDTH and 0 <= y_pos < SCREEN_HEIGHT):
            r = int(self.color[0] * (brightness / 255.0))
            g = int(self.color[1] * (brightness / 255.0))
            b = int(self.color[2] * (brightness / 255.0))

            pygame.draw.circle(screen, (r, g, b), (x_pos, y_pos), int(size))

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Star Eagle | Protetor de Tela Estelar - Tela Cheia")
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    music_file = resource_path(MUSIC_FILE)
    if config['MUSIC_ENABLED']:
        if os.path.exists(music_file):
            try:
                pygame.mixer.music.load(music_file)
                pygame.mixer.music.play(loops=-1)
                print(f"Música carregada com sucesso! ({MUSIC_FILE})")
            except Exception as e:
                print(f"Erro ao carregar música: {e}")
        else:
            print(f"Arquivo '{MUSIC_FILE}' não encontrado em: {music_file}")
    else:
        print("Música desativada nas configurações (MUSIC_ENABLED = False)")

    # Carrega Imagem
    image_file = resource_path(IMAGE_FILE)
    image = None
    if config['IMAGE_ENABLED']:
        if os.path.exists(image_file):
            try:
                image = pygame.image.load(image_file)
                orig_w, orig_h = image.get_size()
                target_scale = min(SCREEN_WIDTH / orig_w, SCREEN_HEIGHT / orig_h)
                print(f"Imagem carregada com sucesso! ({IMAGE_FILE})")
            except Exception as e:
                print(f"Erro ao carregar imagem: {e}")
        else:
            print(f"Arquivo '{IMAGE_FILE}' não encontrado em: {image_file}")
    else:
        print("Imagem desativada nas configurações (IMAGE_ENABLED = False)")

    # Inicializa estrelas
    stars = [Star() for _ in range(NUM_STARS)]

    # Variáveis de animação
    phase = "growing"
    scale_factor = 0.0
    alpha = 255
    grow_speed = 0.005
    fade_speed = 0.005
    pulse_speed = 0.05
    pulse_timer = 0.0
    pulse_count = 0
    max_pulses = 5

    running = True
    fullscreen_mode = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_F11:
                    fullscreen_mode = not fullscreen_mode
                    if not fullscreen_mode:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
                        pygame.display.set_caption("Star Eagle | Protetor de Tela Estelar - Janela")
                    else:
                        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
                        pygame.display.set_caption("SStar Eagle | Protetor de Tela Estelar - Tela Cheia")
                    pygame.display.flip()

        screen.fill(config['BACKGROUND_COLOR'])

        # Atualiza e desenha estrelas
        for star in stars:
            star.update()
            star.draw(screen)

        # Lógica de Animação da Imagem
        if phase == "growing":
            scale_factor += grow_speed
            if scale_factor >= 1.0:
                scale_factor = 1.0
                phase = "pulsing"
                pulse_timer = 0.0
                pulse_count = 0
        elif phase == "pulsing":
            pulse_timer += pulse_speed
            sin_val = math.sin(pulse_timer)
            scale_factor = 1.0 + 0.05 * sin_val
            if sin_val > 0 and math.sin(pulse_timer - pulse_speed) <= 0:
                pulse_count += 1
            if pulse_count >= max_pulses:
                phase = "fading"
        elif phase == "fading":
            alpha -= 255 * fade_speed
            if alpha <= 0:
                alpha = 0
                phase = "growing"
                scale_factor = 0.0
                alpha = 255

        # Desenha imagem se existir
        if image:
            current_scale = scale_factor * target_scale
            if current_scale > 0:
                scaled_image = pygame.transform.scale(image, (int(orig_w * current_scale), int(orig_h * current_scale)))
                rect = scaled_image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                scaled_image.set_alpha(alpha)
                screen.blit(scaled_image, rect)

        pygame.display.flip()
        clock.tick(config['FPS_LIMIT'])

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
