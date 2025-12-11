
import { Diagnostic, DiagnosticSeverity } from 'vscode-languageserver/node';
import { TextDocument } from 'vscode-languageserver-textdocument';

export function getDiagnostics(doc: TextDocument): Diagnostic[] {
  const text = doc.getText();
  const diagnostics: Diagnostic[] = [];

  const breakIdx = text.indexOf('break_gate');
  if (breakIdx !== -1 && !text.match(/\?\s*confirm:\s*"YES"/)) {
    const pos = doc.positionAt(breakIdx);
    diagnostics.push({
      message: 'break_gate detected without explicit ? confirm:"YES" ceremony confirmation.',
      severity: DiagnosticSeverity.Warning,
      range: {
        start: pos,
        end: { line: pos.line, character: pos.character + 'break_gate'.length }
      },
      source: 'gate-lsp'
    });
  }

  if (text.includes('!!IRREVERSIBLE') && text.includes('STATUS="ACTIVE"')) {
    diagnostics.push({
      message: 'Irreversibility marker (!!IRREVERSIBLE) present while a gate is still STATUS="ACTIVE". Check gate state sequencing.',
      severity: DiagnosticSeverity.Information,
      range: {
        start: { line: 0, character: 0 },
        end: { line: 0, character: 1 }
      },
      source: 'gate-lsp'
    });
  }

  return diagnostics;
}
