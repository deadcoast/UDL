import { CharacterSet } from "./presets";

export interface PreviewPattern {
  title: string;
  content: string;
}

export function render2x2Grid(charset: CharacterSet): string {
  const w = 9;
  const c = charset;
  const lines = [];

  lines.push(
    c.top_left +
      c.horizontal.repeat(w) +
      c.tjunction_down +
      c.horizontal.repeat(w) +
      c.top_right,
  );

  lines.push(c.vertical + " Header  " + c.vertical + " Header  " + c.vertical);

  lines.push(
    c.tjunction_right +
      c.horizontal.repeat(w) +
      c.cross +
      c.horizontal.repeat(w) +
      c.tjunction_left,
  );

  lines.push(c.vertical + " Data    " + c.vertical + " Data    " + c.vertical);

  lines.push(
    c.bottom_left +
      c.horizontal.repeat(w) +
      c.tjunction_up +
      c.horizontal.repeat(w) +
      c.bottom_right,
  );

  return lines.join("\n");
}

export function renderSimpleFrame(charset: CharacterSet): string {
  const w = 17;
  const c = charset;

  const lines = [
    c.top_left + c.horizontal.repeat(w) + c.top_right,
    c.vertical + " Simple Frame    " + c.vertical,
    c.bottom_left + c.horizontal.repeat(w) + c.bottom_right,
  ];

  return lines.join("\n");
}

export function render3x3Grid(charset: CharacterSet): string {
  const w = 6;
  const c = charset;
  const lines = [];

  lines.push(
    c.top_left +
      (c.horizontal.repeat(w) + c.tjunction_down).repeat(2) +
      c.horizontal.repeat(w) +
      c.top_right,
  );

  for (let row = 0; row < 3; row++) {
    lines.push(
      c.vertical +
        " Cell " +
        c.vertical +
        " Cell " +
        c.vertical +
        " Cell " +
        c.vertical,
    );

    if (row < 2) {
      lines.push(
        c.tjunction_right +
          (c.horizontal.repeat(w) + c.cross).repeat(2) +
          c.horizontal.repeat(w) +
          c.tjunction_left,
      );
    }
  }

  lines.push(
    c.bottom_left +
      (c.horizontal.repeat(w) + c.tjunction_up).repeat(2) +
      c.horizontal.repeat(w) +
      c.bottom_right,
  );

  return lines.join("\n");
}

export function renderSingleCell(charset: CharacterSet): string {
  const w = 12;
  const c = charset;

  const lines = [
    c.top_left + c.horizontal.repeat(w) + c.top_right,
    c.vertical + " Single Cell" + c.vertical,
    c.bottom_left + c.horizontal.repeat(w) + c.bottom_right,
  ];

  return lines.join("\n");
}

export function renderWideHeader(charset: CharacterSet): string {
  const w = 25;
  const c = charset;

  const lines = [
    c.top_left + c.horizontal.repeat(w) + c.top_right,
    c.vertical + " Wide Header Box       " + c.vertical,
    c.tjunction_right + c.horizontal.repeat(w) + c.tjunction_left,
    c.vertical + " Content Area          " + c.vertical,
    c.vertical + " Multiple Lines        " + c.vertical,
    c.bottom_left + c.horizontal.repeat(w) + c.bottom_right,
  ];

  return lines.join("\n");
}

export function generateAllPatterns(charset: CharacterSet): PreviewPattern[] {
  return [
    {
      title: "2×2 Grid (Full Junction Demo)",
      content: render2x2Grid(charset),
    },
    {
      title: "3×3 Grid (Multiple Junctions)",
      content: render3x3Grid(charset),
    },
    {
      title: "Simple Frame",
      content: renderSimpleFrame(charset),
    },
    {
      title: "Single Cell",
      content: renderSingleCell(charset),
    },
    {
      title: "Wide Header Box",
      content: renderWideHeader(charset),
    },
  ];
}
