"""Character set preset definitions"""

SINGLE_LINE = {
    "top_left": "┌",
    "top_right": "┐",
    "bottom_left": "└",
    "bottom_right": "┘",
    "horizontal": "─",
    "vertical": "│",
    "tjunction_up": "┴",
    "tjunction_down": "┬",
    "tjunction_left": "┤",
    "tjunction_right": "├",
    "cross": "┼",
}

DOUBLE_LINE = {
    "top_left": "╔",
    "top_right": "╗",
    "bottom_left": "╚",
    "bottom_right": "╝",
    "horizontal": "═",
    "vertical": "║",
    "tjunction_up": "╩",
    "tjunction_down": "╦",
    "tjunction_left": "╣",
    "tjunction_right": "╠",
    "cross": "╬",
}

HEAVY_LINE = {
    "top_left": "┏",
    "top_right": "┓",
    "bottom_left": "┗",
    "bottom_right": "┛",
    "horizontal": "━",
    "vertical": "┃",
    "tjunction_up": "┻",
    "tjunction_down": "┳",
    "tjunction_left": "┫",
    "tjunction_right": "┣",
    "cross": "╋",
}

ROUNDED_LINE = {
    "top_left": "╭",
    "top_right": "╮",
    "bottom_left": "╰",
    "bottom_right": "╯",
    "horizontal": "─",
    "vertical": "│",
    "tjunction_up": "┴",
    "tjunction_down": "┬",
    "tjunction_left": "┤",
    "tjunction_right": "├",
    "cross": "┼",
}

MIXED_DOUBLE_SINGLE = {
    "top_left": "╒",
    "top_right": "╕",
    "bottom_left": "╘",
    "bottom_right": "╛",
    "horizontal": "═",
    "vertical": "│",
    "tjunction_up": "╧",
    "tjunction_down": "╤",
    "tjunction_left": "╡",
    "tjunction_right": "╞",
    "cross": "╪",
}

ASCII_BASIC = {
    "top_left": "+",
    "top_right": "+",
    "bottom_left": "+",
    "bottom_right": "+",
    "horizontal": "-",
    "vertical": "|",
    "tjunction_up": "+",
    "tjunction_down": "+",
    "tjunction_left": "+",
    "tjunction_right": "+",
    "cross": "+",
}

PRESETS = {
    "SINGLE_LINE": SINGLE_LINE,
    "DOUBLE_LINE": DOUBLE_LINE,
    "HEAVY_LINE": HEAVY_LINE,
    "ROUNDED_LINE": ROUNDED_LINE,
    "MIXED_DOUBLE_SINGLE": MIXED_DOUBLE_SINGLE,
    "ASCII_BASIC": ASCII_BASIC,
}

def format_charset_python(charset: dict) -> str:
    """Format charset as Python dict string"""
    lines = ["{"]
    for key, value in charset.items():
        lines.append(f'    "{key}": "{value}",')
    lines.append("}")
    return "\n".join(lines)

def format_charset_javascript(charset: dict) -> str:
    """Format charset as JavaScript object string"""
    lines = ["{"]
    for key, value in charset.items():
        lines.append(f'    "{key}": "{value}",')
    lines.append("}")
    return "\n".join(lines)
