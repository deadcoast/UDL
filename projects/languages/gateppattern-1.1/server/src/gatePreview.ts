import { Position } from "vscode-languageserver";
import { TextDocument } from "vscode-languageserver-textdocument";

export function getGateBreakPreview(
  doc: TextDocument,
  _position: Position,
): string {
  const text = doc.getText();
  const m = text.match(/gate\s*:\s*(\d+)/);
  const gate = m ? parseInt(m[1], 10) : 13;
  const newGate = gate - 1;
  return [
    "GATE BREAK PREVIEW",
    "────────────────────",
    `Gate: ${gate} → ${newGate}`,
    "Irreversibility: TRUE",
    "Sledge Cost: 1",
  ].join("\n");
}
