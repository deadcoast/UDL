
export interface GateBlock {
  type: 'FUNCTION_CALL' | 'STATE_CHANGE' | 'DECLARATION' | 'OTHER';
  headerLine: number;
  lines: string[];
}

export function splitBlocks(text: string): GateBlock[] {
  const lines = text.split(/\r?\n/);
  const blocks: GateBlock[] = [];
  let current: GateBlock | null = null;

  function startBlock(type: GateBlock['type'], idx: number, line: string) {
    if (current) blocks.push(current);
    current = { type, headerLine: idx, lines: [line] };
  }

  lines.forEach((line, idx) => {
    if (line.startsWith('> FUNCTION_CALL')) {
      startBlock('FUNCTION_CALL', idx, line);
    } else if (line.startsWith('> STATE_CHANGE')) {
      startBlock('STATE_CHANGE', idx, line);
    } else if (line.startsWith('> DECLARATION::FORMAL')) {
      startBlock('DECLARATION', idx, line);
    } else {
      if (!current) {
        current = { type: 'OTHER', headerLine: idx, lines: [line] };
      } else {
        current.lines.push(line);
      }
    }
  });

  if (current) blocks.push(current);
  return blocks;
}
