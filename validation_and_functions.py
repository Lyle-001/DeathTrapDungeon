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