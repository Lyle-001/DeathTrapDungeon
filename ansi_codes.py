#formatted


import os

def get_list_of_colours_fg():#list of foreground colours for indexing
    list_of_colours_fg = [[txt.col.fg.nml.black,txt.col.fg.nml.red,txt.col.fg.nml.green,txt.col.fg.nml.yellow,txt.col.fg.nml.blue,txt.col.fg.nml.magenta,txt.col.fg.nml.cyan,txt.col.fg.nml.white],[txt.col.fg.strg.grey,txt.col.fg.strg.red,txt.col.fg.strg.green,txt.col.fg.strg.yellow,txt.col.fg.strg.blue,txt.col.fg.strg.magenta,txt.col.fg.strg.cyan,txt.col.fg.strg.white]]
    return list_of_colours_fg

def get_list_of_colours_bg():#list of background colours for indexing
    list_of_colours_bg = [[txt.col.bg.nml.black,txt.col.bg.nml.red,txt.col.bg.nml.green,txt.col.bg.nml.yellow,txt.col.bg.nml.blue,txt.col.bg.nml.magenta,txt.col.bg.nml.cyan,txt.col.bg.nml.white],[txt.col.bg.strg.grey,txt.col.bg.strg.red,txt.col.bg.strg.green,txt.col.bg.strg.yellow,txt.col.bg.strg.blue,txt.col.bg.strg.magenta,txt.col.bg.strg.cyan,txt.col.bg.strg.white]]
    return list_of_colours_bg

def get_list_of_formats():#list of formats for indexing
    list_of_formats = [txt.sty.reset,txt.sty.bold,txt.sty.underline,txt.sty.underlinebold,txt.sty.inverse]
    return list_of_formats

class txt:
    warning = "[1m[31m"
    class sty:
        reset = "[0m"
        bold = "[1m"
        underline = "[4m"
        underlinebold = "[1m[4m"
        inverse = "[7m"
    class col:
        class fg:
            class nml:
                black = "[30m"
                red = "[31m"
                green = "[32m"
                yellow = "[33m"
                blue = "[34m"
                magenta = "[35m"
                cyan = "[36m"
                white = "[37m"
            class strg:
                grey = "[90m"
                red = "[91m"
                green = "[92m"
                yellow = "[93m"
                blue = "[94m"
                magenta = "[95m"
                cyan = "[96m"
                white = "[97m"
        class bg:
            class nml:
                black = "[40m"
                red = "[41m"
                green = "[42m"
                yellow = "[43m"
                blue = "[44m"
                magenta = "[45m"
                cyan = "[46m"
                white = "[47m"
            class strg:
                grey = "[100m"
                red = "[101m"
                green = "[102m"
                yellow = "[103m"
                blue = "[104m"
                magenta = "[105m"
                cyan = "[106m"
                white = "[107m"

class icons:
    heart = "{}♡{}".format(txt.col.fg.nml.red,txt.sty.reset)
    gold = "{}¤{}".format(txt.col.fg.nml.yellow,txt.sty.reset)
    damage = "{}⚔{}".format(txt.col.fg.strg.red,txt.sty.reset)
    hitchance = "{}⚄{}".format(txt.col.fg.strg.magenta,txt.sty.reset)

def clearscreen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")