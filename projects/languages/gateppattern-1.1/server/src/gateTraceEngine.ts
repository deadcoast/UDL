import { TextDocument } from "vscode-languageserver-textdocument";
import { splitBlocks, GateBlock } from "./gateParser";

function parseBreakGate(block: GateBlock) {
  const text = block.lines.join("\n");
  const m = text.match(/break_gate\s*\(([^)]*)\)/);
  if (!m) return null;
  const argStr = m[1];
  const args: Record<string, string> = {};
  argStr.split(",").forEach((raw) => {
    const part = raw.trim();
    const kv = part.split(":");
    if (kv.length >= 2) {
      const key = kv[0].trim();
      const val = kv.slice(1).join(":").trim();
      args[key] = val;
    }
  });
  return args;
}

export function compileToTrace(doc: TextDocument): string {
  const text = doc.getText();
  const blocks = splitBlocks(text);
  const lines: string[] = [];

  for (const block of blocks) {
    if (block.type === "FUNCTION_CALL") {
      const args = parseBreakGate(block);
      if (args) {
        lines.push("#==TRACE:FUNCTION");
        lines.push(">trace::FUNCTION:");
        lines.push(`    name:"break_gate"`);
        if (args["agent"]) lines.push(`    agent:${args["agent"]}`);
        if (args["gate"]) lines.push(`    gate:${args["gate"]}`);
        if (args["by_user"]) lines.push(`    by_user:${args["by_user"]}`);
      } else {
        lines.push("#==TRACE:FUNCTION");
        lines.push(">trace::FUNCTION:");
        lines.push(`    raw:"${block.lines.join("\n").replace(/"/g, '\\"')}"`);
      }
    } else if (block.type === "STATE_CHANGE") {
      lines.push("#==TRACE:STATE");
      lines.push(">trace::STATE:");
      block.lines.slice(1).forEach((l) => {
        const trimmed = l.trim();
        if (trimmed.startsWith(">out")) {
          lines.push(`    ${trimmed.substring(4).trim()}`);
        }
      });
    }
  }

  if (lines.length === 0) {
    lines.push("#==TRACE:COMPILED");
    lines.push("# no FUNCTION_CALL or STATE_CHANGE blocks detected");
  }

  return lines.join("\n");
}
