import curses
from curses import wrapper
import time
import random
import requests


def fetch_text_from_api():
#Fetch random text from an API.
    try:
        # random quotes API 
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        data = response.json()
        return data["content"]
    except requests.RequestException:
        # if API fails
        return "The quick brown fox jumps over the lazy dog and he fall on the dog."


def start_screen(stdscr):
#Displays the welcome screen.
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!", curses.color_pair(3))
    stdscr.addstr("\nInstructions:")
    stdscr.addstr("\n- Type the displayed text as fast as you can.")
    stdscr.addstr("\n- Use Backspace to correct mistakes.")
    stdscr.addstr("\n- Press Esc to exit at any time.")
    stdscr.addstr("\n\nPress any key to begin!", curses.color_pair(3))
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
#Displays target text, current text
    stdscr.addstr(0, 0, f"Speed Typing Test - WPM: {wpm}", curses.color_pair(3))
    stdscr.addstr("\n\n", curses.color_pair(3))

    # Disp target text
    for i, char in enumerate(target):
        color = curses.color_pair(3)
        if i < len(current):
            if current[i] == char:
                color = curses.color_pair(1)  
            else:
                color = curses.color_pair(2)  
        stdscr.addstr(char, color)

    # current input below
    stdscr.addstr("\n\nYour input:\n", curses.color_pair(3))
    stdscr.addstr("".join(current), curses.color_pair(1))


def wpm_test(stdscr):
    #Main typing test
    target_text = fetch_text_from_api()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        # Calculate WPM
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        # Clear and update screen
        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        # Check if the test is complete
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # Esc
            return False

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if current_text:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    return True


def main(stdscr):
    """Main function to initialize the curses application."""
    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  

    start_screen(stdscr)
    while True:
        test_result = wpm_test(stdscr)
        if not test_result:
            break

        # Completion message
        stdscr.addstr("\n\nYou completed the text!", curses.color_pair(1))
        stdscr.addstr("\nPress any key to retry or Esc to exit.", curses.color_pair(3))
        key = stdscr.getkey()

        if ord(key) == 27:  # Exit 
            break


wrapper(main)
