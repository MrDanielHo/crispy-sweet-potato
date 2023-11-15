"""Bouncing DVD Logo, by Al Swigard al@inventwithpython.com
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press CTRL + C to stop.

Note: do not resize the terminal window while this program is running.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, artistic, bext"""

import sys, random, time

try:
    import bext
except ImportError:
    print('''This program requires the bext module, which you
    can install by following the instructions at
    https://pypi.org/project/Bext''')
    sys.exit()

# Set up the constants:
WIDTH, HEIGHT = bext.size()
# We cannot print to the last column on Windows without it adding a 
# newline automatically so reduce the width by one:
WIDTH -= 1

NUMBER_OF_LOGOS = 5     # (!) Try changing this to 1 or 100
PAUSE_AMOUNT    = 0.2   # (!) Try changing this to 1.0 or 0.0 
# (!) Try changing this list to fewer colours:
COLOURS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT    = 'ur'
UP_LEFT     = 'ul'
DOWN_RIGHT  = 'dr'
DOWN_LEFT   = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries:
COLOUR  = 'colour'
X       = 'x'
Y       = 'y'
DIR     = 'direction'


def main():
    bext.clear()

    # Generate some logos.
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOUR: random.choice(COLOURS),
                       X: random.randint(1, WIDTH - 4),
                       Y: random.randint(1, HEIGHT - 4),
                       DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner.
            logos[-1][X] -= 1

    cornerBounces = 0   # Count how many times a logo hits a corner.
    while True:     # Main program loop
        for logo in logos:  # Handle each logo in the logos list.
            # Erase the logo's current location:
            bext.goto(logo[X], logo[Y])
            print('   ', end='')    # (!) Try commending this line out.

            originalDirection = logo[DIR]
            
            # See if the logo bounces off the corners:
            if logo[X] == 0 and logo [Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo [Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            # See if the logo bounches off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo [DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            # (WIDTH - 3 becasue 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo [Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == 0 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_RIGHT

            if logo[DIR] != originalDirection:
                # Change colour when the logo bounces:
                logo[COLOUR] = random.choice(COLOURS)
            
            # Move the logo. (X Moves by 2 because of the terminal 
            # characters are twice as tall as they are wide.)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            if logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            if logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            if logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corner bounces:
        bext.goto(5,0)
        bext.fg('white')
        print(f'Corner bounces: {cornerBounces}', end='')

        for logo in logos:
            # Draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOUR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(PAUSE_AMOUNT)


# If this program was run (instead of impoerted), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD logo')
        sys.exit()  # When CTRL + C is pressed, end the program.