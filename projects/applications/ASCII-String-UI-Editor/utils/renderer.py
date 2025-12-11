"""Box rendering logic"""

def render_2x2_grid(charset: dict) -> str:
    """
    Render 2x2 grid with headers and data
    Demonstrates: all corners, cross, all t-junctions
    """
    w = 9

    c = charset
    lines = []

    lines.append(
        c['top_left'] +
        c['horizontal'] * w +
        c['tjunction_down'] +
        c['horizontal'] * w +
        c['top_right']
    )

    lines.append(
        c['vertical'] + ' Header  ' +
        c['vertical'] + ' Header  ' +
        c['vertical']
    )

    lines.append(
        c['tjunction_right'] +
        c['horizontal'] * w +
        c['cross'] +
        c['horizontal'] * w +
        c['tjunction_left']
    )

    lines.append(
        c['vertical'] + ' Data    ' +
        c['vertical'] + ' Data    ' +
        c['vertical']
    )

    lines.append(
        c['bottom_left'] +
        c['horizontal'] * w +
        c['tjunction_up'] +
        c['horizontal'] * w +
        c['bottom_right']
    )

    return '\n'.join(lines)


def render_simple_frame(charset: dict) -> str:
    """
    Render simple rectangular frame
    Demonstrates: corners, horizontal, vertical
    """
    w = 17
    c = charset

    lines = [
        c['top_left'] + c['horizontal'] * w + c['top_right'],
        c['vertical'] + ' Simple Frame    ' + c['vertical'],
        c['bottom_left'] + c['horizontal'] * w + c['bottom_right']
    ]

    return '\n'.join(lines)


def render_3x3_grid(charset: dict) -> str:
    """
    Render 3x3 grid
    Demonstrates: multiple cross junctions, all t-junctions
    """
    w = 6
    c = charset
    lines = []

    lines.append(
        c['top_left'] +
        (c['horizontal'] * w + c['tjunction_down']) * 2 +
        c['horizontal'] * w +
        c['top_right']
    )

    for row in range(3):
        lines.append(
            c['vertical'] + ' Cell ' +
            c['vertical'] + ' Cell ' +
            c['vertical'] + ' Cell ' +
            c['vertical']
        )

        if row < 2:
            lines.append(
                c['tjunction_right'] +
                (c['horizontal'] * w + c['cross']) * 2 +
                c['horizontal'] * w +
                c['tjunction_left']
            )

    lines.append(
        c['bottom_left'] +
        (c['horizontal'] * w + c['tjunction_up']) * 2 +
        c['horizontal'] * w +
        c['bottom_right']
    )

    return '\n'.join(lines)


def render_single_cell(charset: dict) -> str:
    """
    Render single cell box
    Demonstrates: basic frame construction
    """
    w = 12
    c = charset

    lines = [
        c['top_left'] + c['horizontal'] * w + c['top_right'],
        c['vertical'] + ' Single Cell' + c['vertical'],
        c['bottom_left'] + c['horizontal'] * w + c['bottom_right']
    ]

    return '\n'.join(lines)


def render_wide_header(charset: dict) -> str:
    """
    Render wide box with header separator
    Demonstrates: horizontal divisions
    """
    w = 25
    c = charset

    lines = [
        c['top_left'] + c['horizontal'] * w + c['top_right'],
        c['vertical'] + ' Wide Header Box       ' + c['vertical'],
        c['tjunction_right'] + c['horizontal'] * w + c['tjunction_left'],
        c['vertical'] + ' Content Area          ' + c['vertical'],
        c['vertical'] + ' Multiple Lines        ' + c['vertical'],
        c['bottom_left'] + c['horizontal'] * w + c['bottom_right']
    ]

    return '\n'.join(lines)


def generate_all_patterns(charset: dict) -> list[dict]:
    """
    Generate all preview patterns
    Returns list of dicts with title and content
    """
    return [
        {
            "title": "2×2 Grid (Full Junction Demo)",
            "content": render_2x2_grid(charset)
        },
        {
            "title": "3×3 Grid (Multiple Junctions)",
            "content": render_3x3_grid(charset)
        },
        {
            "title": "Simple Frame",
            "content": render_simple_frame(charset)
        },
        {
            "title": "Single Cell",
            "content": render_single_cell(charset)
        },
        {
            "title": "Wide Header Box",
            "content": render_wide_header(charset)
        }
    ]
