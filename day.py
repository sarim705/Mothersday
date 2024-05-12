import pyfiglet
from termcolor import colored
import random

def get_random_font_style():
    font_styles = pyfiglet.FigletFont.getFonts()
    return random.choice(font_styles)

def get_random_color():
    colors = ["white", "red", "green", "blue", "yellow", "cyan", "magenta"]
    return random.choice(colors)

def wish_mothers_day():
    random_font_style = get_random_font_style()
    random_color = get_random_color()
    font = pyfiglet.Figlet(font=random_font_style)
    message = font.renderText("Happy Mother's Day!")
    colored_message = colored(message, color=random_color)
    print(colored_message)

wish_mothers_day()
