from ansi_codes import txt

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

def validate_input_from_array(array,message=""):
    while True:
        answer = input(message)
        for loop in array:
            if answer == loop:
                return answer
        print("{}Please choose a valid input.{}".format(txt.col.fg.strg.red,txt.sty.reset))