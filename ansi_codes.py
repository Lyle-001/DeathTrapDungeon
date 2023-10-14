

class txt:
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

def get_list_of_colours_fg_nml():
    list_of_colours_fg_nml = [txt.col.fg.nml.black,txt.col.fg.nml.red,txt.col.fg.nml.green,txt.col.fg.nml.yellow,txt.col.fg.nml.blue,txt.col.fg.nml.magenta,txt.col.fg.nml.cyan,txt.col.fg.nml.white]
    return list_of_colours_fg_nml

def get_list_of_colours_fg_strg():
    list_of_colours_fg_strg = [txt.col.fg.strg.black,txt.col.fg.strg.red,txt.col.fg.strg.green,txt.col.fg.strg.yellow,txt.col.fg.strg.blue,txt.col.fg.strg.magenta,txt.col.fg.strg.cyan,txt.col.fg.strg.white]
    return list_of_colours_fg_strg

def get_list_of_colours_bg_nml():
    list_of_colours_bg_nml = [txt.col.bg.nml.black,txt.col.bg.nml.red,txt.col.bg.nml.green,txt.col.bg.nml.yellow,txt.col.bg.nml.blue,txt.col.bg.nml.magenta,txt.col.bg.nml.cyan,txt.col.bg.nml.white]
    return list_of_colours_bg_nml

def get_list_of_colours_bg_strg():
    list_of_colours_bg_strg = [txt.col.bg.strg.black,txt.col.bg.strg.red,txt.col.bg.strg.green,txt.col.bg.strg.yellow,txt.col.bg.strg.blue,txt.col.bg.strg.magenta,txt.col.bg.strg.cyan,txt.col.bg.strg.white]
    return list_of_colours_bg_strg

def get_list_of_formats():
    list_of_formats = [txt.sty.reset,txt.sty.bold,txt.sty.underline,txt.sty.underlinebold,txt.sty.inverse]
    return list_of_formats