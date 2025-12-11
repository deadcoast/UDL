export interface CharacterSet {
  top_left: string;
  top_right: string;
  bottom_left: string;
  bottom_right: string;
  horizontal: string;
  vertical: string;
  tjunction_up: string;
  tjunction_down: string;
  tjunction_left: string;
  tjunction_right: string;
  cross: string;
}

export const SINGLE_LINE: CharacterSet = {
  top_left: '┌',
  top_right: '┐',
  bottom_left: '└',
  bottom_right: '┘',
  horizontal: '─',
  vertical: '│',
  tjunction_up: '┴',
  tjunction_down: '┬',
  tjunction_left: '┤',
  tjunction_right: '├',
  cross: '┼',
};

export const DOUBLE_LINE: CharacterSet = {
  top_left: '╔',
  top_right: '╗',
  bottom_left: '╚',
  bottom_right: '╝',
  horizontal: '═',
  vertical: '║',
  tjunction_up: '╩',
  tjunction_down: '╦',
  tjunction_left: '╣',
  tjunction_right: '╠',
  cross: '╬',
};

export const HEAVY_LINE: CharacterSet = {
  top_left: '┏',
  top_right: '┓',
  bottom_left: '┗',
  bottom_right: '┛',
  horizontal: '━',
  vertical: '┃',
  tjunction_up: '┻',
  tjunction_down: '┳',
  tjunction_left: '┫',
  tjunction_right: '┣',
  cross: '╋',
};

export const ROUNDED_LINE: CharacterSet = {
  top_left: '╭',
  top_right: '╮',
  bottom_left: '╰',
  bottom_right: '╯',
  horizontal: '─',
  vertical: '│',
  tjunction_up: '┴',
  tjunction_down: '┬',
  tjunction_left: '┤',
  tjunction_right: '├',
  cross: '┼',
};

export const MIXED_DOUBLE_SINGLE: CharacterSet = {
  top_left: '╒',
  top_right: '╕',
  bottom_left: '╘',
  bottom_right: '╛',
  horizontal: '═',
  vertical: '│',
  tjunction_up: '╧',
  tjunction_down: '╤',
  tjunction_left: '╡',
  tjunction_right: '╞',
  cross: '╪',
};

export const ASCII_BASIC: CharacterSet = {
  top_left: '+',
  top_right: '+',
  bottom_left: '+',
  bottom_right: '+',
  horizontal: '-',
  vertical: '|',
  tjunction_up: '+',
  tjunction_down: '+',
  tjunction_left: '+',
  tjunction_right: '+',
  cross: '+',
};

export const PRESETS: Record<string, { name: string; charset: CharacterSet }> = {
  SINGLE_LINE: { name: 'Single Line', charset: SINGLE_LINE },
  DOUBLE_LINE: { name: 'Double Line', charset: DOUBLE_LINE },
  HEAVY_LINE: { name: 'Heavy Line', charset: HEAVY_LINE },
  ROUNDED_LINE: { name: 'Rounded Corners', charset: ROUNDED_LINE },
  MIXED_DOUBLE_SINGLE: { name: 'Mixed Double/Single', charset: MIXED_DOUBLE_SINGLE },
  ASCII_BASIC: { name: 'ASCII Basic (+/-/|)', charset: ASCII_BASIC },
};
