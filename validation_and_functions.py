from ansi_codes import txt,get_list_of_colours_fg
import random

def validate_int_input_with_bounds(lowbound,upperbound,message=""):#upper bound is exclusive lower bound inclusive
    while True:
        try:
            answer = int(input(message))
            if answer >= lowbound and answer < upperbound:
                return answer
            else:
                print("{}Please choose a valid number.{}".format(txt.warning,txt.sty.reset))
        except:
            print("{}Please choose a valid number.{}".format(txt.col.fg.strg.red,txt.sty.reset))
    

def validate_not_empty_input(message=""):#asks until non empty input entered
    while True:
        answer = input(message)
        if answer != "":
            return answer
        else:
            print("{}Type something!{}".format(txt.warning,txt.sty.reset))


def validate_int_input(message=""):#asks until num input entered
    while True:
        try:
            answer = int(input(message))
            return answer
        except:
            print("{}Please choose a numeral.{}".format(txt.warning,txt.sty.reset))

def validate_input_from_array(array,message=""):#loops through array until input is equal to 1 element in the array
    while True:
        answer = input(message)
        for loop in array:
            if answer.capitalize() == str(loop).capitalize():
                return answer
        print("{}Please choose a valid input.{}".format(txt.col.fg.strg.red,txt.sty.reset))

def RandomColour(): # Choose random colour for monster.
    ColourList = get_list_of_colours_fg()[0]
    Colour = ColourList[random.randint(0,len(ColourList)-1)]
    return Colour

def health_bar(currentHealth: int,maxHealth: int,length: int = 20, barColour: str = txt.sty.reset, edgeColour: str = txt.sty.reset):
    """
    Prints the actor's health in a cool and neat bar format
    
    Args:
        currentHealth (int): The actor's current health, to be displayed as full boxes
        maxHealth (int): The actor's maximum health, to be displayed as empty boxes
        length (int, default of 20): The length of the bar (discluding the edges) in characters
        barColour (str, default of none): The colour code of the bar
        edgeColour (str, default of none): The colour code of the edges
    Returns:
        Nothing
    """
    corners = ["╭","╮","╯","╰"]
    vertical = "│"
    horizontal = "━"
    bar = {1:"█",
            0.875:"▉",
            0.75:"▊",
            0.625:"▋",
            0.5:"▌",
            0.375:"▍",
            0.25:"▎",
            0.125:"▏",
            0:" "}
    
    healthBar = []
    
    # Print the top edge
    message = edgeColour + corners[0]
    for i in range(0,length,1):
        message += horizontal
    message += corners[1] + txt.sty.reset
    healthBar += message + "\n"
    
    # Print the bar
    healthPerCharacter = maxHealth / length
    message = edgeColour + vertical
    for i in range(0,length,1):
        healthLeft = (currentHealth - i*healthPerCharacter) / healthPerCharacter
        if healthLeft > 1:
            healthLeft = 1
        if healthLeft < 0:
            healthLeft = 0
        percent = round(healthLeft*8)/8
        message += barColour + bar[percent]
    message += edgeColour + vertical + txt.sty.reset
    healthBar += message + "\n"

    # Print the bottom edge
    message = edgeColour + corners[3]
    for i in range(0,length,1):
        message += horizontal
    message += corners[2] + txt.sty.reset
    healthBar += message
    
    return healthBar

def stringify_list(data: list):
    """
    Returns a list in a more human-readable format to be printed

    Args:
        data (list): the list to be stringified.
    Returns:
        Nothing
    """
    if type(data) != list:
        return str(data)
    message = ""
    for index in range(len(data)):
        item = data[index]
        message += stringify_list(item)
    return message