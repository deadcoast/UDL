
import { Hover, MarkupKind, Position } from 'vscode-languageserver/node';
import { TextDocument } from 'vscode-languageserver-textdocument';

export function getHover(doc: TextDocument, position: Position): Hover | null {
  const text = doc.getText();
  const offset = doc.offsetAt(position);

  let start = offset;
  while (start > 0 && !/\s/.test(text[start - 1])) start--;
  let end = offset;
  while (end < text.length && !/\s/.test(text[end])) end++;

  const word = text.slice(start, end);

  if (/^%[A-Z]+%$/.test(word)) {
    return {
      contents: {
        kind: MarkupKind.Markdown,
        value: `**Context Variable**\\nSymbol: \`${word}\``
      }
    };
  }

  const symbolicMap: Record<string,string> = {
    'Δ': '**Δ Delta Shift**\\nRepresents recorded state transition.',
    '↯': '**↯ Intent Discharge**\\nHuman-bound intent force.',
    'ϟ': '**ϟ Sledge Spark**\\nSledge discharge at a Gate boundary.',
    '⌘': '**⌘ Authority Root**\\nBinds an identity anchor in the ROOT layer.',
    '⌾': '**⌾ Realm Align**\\nAligns a symbol with a metaphysical Realm.',
    '⇜': '**⇜ Meaning Pull**\\nPulls a symbol toward another in semantic orbit.',
    '⇝': '**⇝ Meaning Push**\\nPropagates symbol influence into a field.',
    '⇹': '**⇹ Entanglement Link**\\nRepresents symbolic entanglement between agents or symbols.'
  };

  if (symbolicMap[word]) {
    return {
      contents: {
        kind: MarkupKind.Markdown,
        value: symbolicMap[word]
      }
    };
  }

  if (word === 'break_gate') {
    return {
      contents: {
        kind: MarkupKind.Markdown,
        value: '**break_gate(agent, gate, by_user)**\\nConsumes a Sledge and breaks a Gate, shifting CURRENT_GATE down by 1.'
      }
    };
  }

  return null;
}
