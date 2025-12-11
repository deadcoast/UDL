
import { TextDocument } from 'vscode-languageserver-textdocument';

export function evaluateEvolutionReport(doc: TextDocument): string {
  const text = doc.getText();
  const hasTorchbearer = /Torchbearer/.test(text);
  const hasEchoTrace = /#==TRACE:ECHO/.test(text) || /ECHO_MEMORY/.test(text);
  const hasGateFusionHints = /GATE.*FUSION/i.test(text);

  let potential = 0.25;
  if (hasTorchbearer) potential += 0.35;
  if (hasEchoTrace) potential += 0.2;
  if (hasGateFusionHints) potential += 0.15;
  if (potential > 1.0) potential = 1.0;

  return [
    '#==TRACE:EVOLUTION',
    '>trace::EVOLUTION:',
    `    potential:"${potential.toFixed(2)}"`,
    `    arc:"ASCENT"`,
    `    note:"Heuristic evolution estimate based on titles, echoes, and fusion hints"`
  ].join('\n');
}
