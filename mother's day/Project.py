import os
from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np
import random

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 10
DURATION = 10  # seconds
TOTAL_FRAMES = FPS * DURATION

# Colors (customize here)
BG_COLOR = (135, 206, 235)  # Sky blue background
MESSAGE_COLOR = (255, 20, 147)  # Deep pink
SUBMESSAGE_COLOR = (255, 255, 255)  # White
FLOWER_CENTER_COLOR = (255, 215, 0)  # Gold
FLOWER_PETAL_COLOR = (255, 182, 193)  # Light pink
WATERFALL_COLOR = (0, 191, 255)  # Deep sky blue
STARS_COLOR = (255, 255, 0)  # Yellow

# Messages (customize here)
MAIN_MESSAGE = "Happy Mother's Day!"
SUB_MESSAGE = "To the best mom in the world!"

# Fonts (try to load from asset/font, else default)
try:
    FONT_MESSAGE = ImageFont.truetype("asset/font/message.ttf", 50)
except:
    FONT_MESSAGE = ImageFont.load_default()

try:
    FONT_SUBMESSAGE = ImageFont.truetype("asset/font/submessage.ttf", 30)
except:
    FONT_SUBMESSAGE = ImageFont.load_default()

# Images (try to load, else None)
try:
    IMG_BEFORE = Image.open("asset/image/before.png").convert("RGBA")
except:
    IMG_BEFORE = None

try:
    IMG_AFTER = Image.open("asset/image/after.png").convert("RGBA")
except:
    IMG_AFTER = None

try:
    FLOATING_IMG = Image.open("asset/image/floating.png").convert("RGBA")
except:
    FLOATING_IMG = None

def draw_background(draw):
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill=BG_COLOR)

def draw_flower(draw, x, y, size=50):
    # Center
    draw.ellipse([x-size/4, y-size/4, x+size/4, y+size/4], fill=FLOWER_CENTER_COLOR)
    # Petals
    for angle in range(0, 360, 45):
        rad = np.radians(angle)
        px = x + size/2 * np.cos(rad)
        py = y + size/2 * np.sin(rad)
        draw.ellipse([px-size/4, py-size/4, px+size/4, py+size/4], fill=FLOWER_PETAL_COLOR)

def draw_waterfall(draw, frame):
    # Simple waterfall effect
    for i in range(10):
        y = (frame * 10 + i * 60) % (HEIGHT + 60) - 60
        draw.rectangle([WIDTH-100, y, WIDTH-50, y+50], fill=WATERFALL_COLOR)

def draw_stars(draw, frame):
    random.seed(42)  # For consistent stars
    for i in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT//2)
        brightness = (np.sin(frame * 0.1 + i) + 1) / 2  # Twinkle
        color = tuple(int(c * brightness) for c in STARS_COLOR)
        draw.ellipse([x-2, y-2, x+2, y+2], fill=color)

def draw_sliding_message(draw, frame):
    # Slide in from left
    text_width = draw.textlength(MAIN_MESSAGE, font=FONT_MESSAGE)
    x = -text_width + (frame / TOTAL_FRAMES) * (WIDTH + text_width)
    y = HEIGHT // 2 - 50
    draw.text((x, y), MAIN_MESSAGE, fill=MESSAGE_COLOR, font=FONT_MESSAGE)

    # Submessage appears after
    if frame > TOTAL_FRAMES // 2:
        sub_x = WIDTH // 2 - draw.textlength(SUB_MESSAGE, font=FONT_SUBMESSAGE) // 2
        sub_y = HEIGHT // 2 + 20
        draw.text((sub_x, sub_y), SUB_MESSAGE, fill=SUBMESSAGE_COLOR, font=FONT_SUBMESSAGE)

def draw_floating_image(img, frame, base_img):
    if img:
        # Float around
        x = WIDTH // 2 + 100 * np.sin(frame * 0.05)
        y = HEIGHT // 2 + 50 * np.cos(frame * 0.05)
        base_img.paste(img, (int(x), int(y)), img)

# Create frames
frames = []
for frame in range(TOTAL_FRAMES):
    img = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw_background(draw)
    draw_stars(draw, frame)
    draw_waterfall(draw, frame)
    draw_flower(draw, 200, 200)
    draw_flower(draw, 600, 300)  # Extra flower
    draw_sliding_message(draw, frame)
    draw_floating_image(FLOATING_IMG, frame, img)

    # Convert to RGB for imageio
    rgb_img = img.convert("RGB")
    frames.append(np.array(rgb_img))

# Save as GIF
imageio.mimsave("mothers_day_card.gif", frames, fps=FPS)
print("Animated card saved as mothers_day_card.gif")