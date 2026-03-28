# Screensaver Star Eagle - Protetor de Tela Estelar

**Um protetor de tela bonito, leve e totalmente configurável com efeito starfield 3D, música de fundo e imagem central animada.**

<p align="center">
  <img src="https://github.com/Jayme-G/SCR_StarEagle/blob/main/imagem.png?raw=true"
       width="300"/>
</p>

---

## Versão para Linux e Windows

## 1. Sobre o protetor de tela

- O **SCR_StarEagle** é um protetor de tela desenvolvido em Python + Pygame que simula um campo de estrelas em movimento 3D (efeito “tunnel stars” ou starfield clássico). As estrelas voam em direção à câmera com perspectiva realista, mudam de cor e brilho conforme a profundidade. Além disso, é possível colocar uma imagem central que anima suavemente (cresce, pulsa e fade) e uma música de fundo em loop.

- **Repositório:** https://github.com/Jayme-G/SCR_StarEagle.

### Principais características:

- **Efeito visual hipnotizante** - Até 2000 estrelas coloridas com profundidade 3D, brilho dinâmico e tamanho variável;
- **Totalmente personalizável** - via arquivo `config.ini` (resolução, velocidade, quantidade de estrelas, cores, fundo, etc.);
- **Música de fundo** em loop - (suporta MP3, OGG, WAV, MID, etc.);
- **Imagem central animada** - com ciclo de crescimento → pulso → fade;
- **Modo tela cheia** - por padrão (F11 alterna para janela);
- **Saída fácil** - tecla `ESC`;
- **Compatibilidade** - Windows e Linux (funciona tanto como `.exe`/binário quanto script Python);
- **Leve e otimizado** - limite de FPS configurável e uso de `resource_path` para funcionar perfeitamente após compilação com PyInstaller; e
- **Licença MIT** - código aberto, gratuito e modificável.

---

## 2. Aviso Legal / Disclaimer

Este protetor de tela é um projeto pessoal/hobby desenvolvido para diversão, ou seja: 
- Não há garantia de funcionamento em todas as máquinas ou configurações; 
- A imagem e a música são de uso livre para este projeto;
- O autor não se responsabiliza por qualquer dano causado pelo uso do software; e
- Use por sua conta e risco e divirta-se com responsabilidade!

---

## 3. Baixar os binários conforme o seu sistema operacional (Linux ou Windows)

**Versões compiladas (recomendado):**

- **Windows**: `SCR_StarEagle.zip`; ou
- **Linux**: `SCR_StarEagle.tar.xz`

**Onde baixar:**
Disponível na página de Releases do repositório. Basta baixar o arquivo correspondente ao seu SO, descompactar e executar.

---

## 4. Se for executar a partir do Python, utilizar o Python 3.13 (não testei outras versões)

### Requisitos:
- Python 3.13 (recomendado); e
- Biblioteca `pygame` (instale com `pip install pygame`).

### Como rodar:
```bash
pip install pygame (ajustar o comando do pip conforme a sua necessidade, por exemplo: se usa venv, se não é o python global etc.)
python SCR_StarEagle.py
```

---

## 5. Como configurar

O protetor de tela é **altamente configurável** através do arquivo `config.ini`, que é criado automaticamente na primeira execução na pasta '_internal' ou na mesma pasta de 'SCR_StarEagle.py'.

### Como usar:
1. Execute o protetor de tela uma vez → o arquivo `config.ini` será criado automaticamente.
2. Abra `config.ini` com qualquer editor de texto (Bloco de Notas, VS Code, etc.).
3. Altere os valores conforme desejar (as explicações estão em português dentro do arquivo).
4. Salve e execute novamente. As mudanças são aplicadas imediatamente.

### Principais opções de configuração:

```ini
NUM_STARS = 500                             # Quantidade de estrelas (100~2000)
MAX_Z = 100.0                               # Profundidade máxima
MIN_Z = 1.0                                 # Estrelas chegam muito perto
DEFAULT_SPEED = 0.5                         # Velocidade base
SCREEN_WIDTH = 1920                         # Resolução da tela (largura)
SCREEN_HEIGHT = 1080                        # Resolução da tela (altura)
MAX_STAR_SIZE = 5.0                         # Tamanho máximo das estrelas
STAR_COLORS = 127,0,255;0,127,255;0,0,255   # Cores (R,G,B) separadas por ;
MUSIC_ENABLED = True                        # True habilita, False desabilita a música
MUSIC_FILE = musica.mp3                     # Arquivo de música (na mesma pasta)
IMAGE_ENABLED = True                        # True habilita, False desabilita a imagem
IMAGE_FILE = imagem.png                     # Imagem central (na mesma pasta)
FPS_LIMIT = 60                              # Limite de frames por segundo
BACKGROUND_COLOR = 0,0,0                    # Cor de fundo (R,G,B)
```

**Dica:** Para voltar às configurações originais, basta excluir o `config.ini` e executar o programa novamente.

---

Agradecimentos especiais à comunidade Pygame e a todos que ajudam a testar as builds!

Encontrou algum bug? Tem sugestão ou melhoria? 
→ Por favor abra uma issue ou mande sua ideia!

**Divirta-se com o SCR_StarEagle!** 
