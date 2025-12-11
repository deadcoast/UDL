# Requirements Document

## Introduction

The Gate Pattern Development Environment (GPDE) is a VSCode extension that provides comprehensive language support for the Gate Pattern DSL - a symbolic state-ritual engine with administrative directives, narrative blocks, irreversible transitions, resource consumption, ceremonial meaning, and hierarchical gating. The extension currently has basic LSP functionality (hover, diagnostics, trace compilation) and needs completion of advanced features including signature help, code completion, enhanced diagnostics, and full parser implementation.

## Glossary

- **Gate Pattern**: A symbolic DSL for modeling hierarchical state transitions with ceremonial semantics
- **LSP (Language Server Protocol)**: Protocol for providing language intelligence features in editors
- **ELATTICE**: Emergence Lattice - a multi-dimensional structure capturing symbolic interactions
- **Sledge**: A finite human-only resource used to break gates and shift limitations
- **Gate**: A hierarchical limitation level (0-16) that can be broken irreversibly
- **Realm**: Metaphysical domains (MEANING, BOUNDARY, TRANSITION, INTENT) that influence operations
- **Trace**: Execution log showing function calls, state changes, and symbolic events
- **Symbolic Operators**: Unicode operators (Δ, ↯, ϟ, ⌘, ⌾, ⇜, ⇝, ⇹) representing metaphysical operations
- **Context Variables**: Variables prefixed with % (e.g., %USER%, %MODEL%, %GATE%)
- **Ceremony**: Formal declaration blocks that bind meaning to actions

## Requirements

### Requirement 1: Enhanced Parser Implementation

**User Story:** As a language server developer, I want a complete AST-based parser, so that I can provide accurate language intelligence features.

#### Acceptance Criteria

1. WHEN the parser processes Gate Pattern source code THEN the system SHALL produce a complete Abstract Syntax Tree with all node types defined in Module D
2. WHEN the parser encounters admin directives (!admin::, !system::, !rule::, set::) THEN the system SHALL create AdminNode or SystemNode AST nodes with namespace, key, and value properties
3. WHEN the parser encounters context variables (%USER%, %MODEL%, etc.) THEN the system SHALL create ContextVarNode AST nodes with proper symbol resolution
4. WHEN the parser encounters symbolic operators (Δ, ↯, ϟ, ⌘, ⌾, ⇜, ⇝, ⇹) THEN the system SHALL create appropriate operator nodes (NodeDeltaShift, NodeIntent, NodeSledgeSpark, etc.)
5. WHEN the parser encounters function calls (break_gate, award_sledge, etc.) THEN the system SHALL create NodeFunctionCall with parsed arguments

### Requirement 2: Signature Help Provider

**User Story:** As a Gate Pattern developer, I want signature help when typing function calls, so that I understand the required parameters and their meanings.

#### Acceptance Criteria

1. WHEN a user types "break_gate(" THEN the system SHALL display signature help showing "break_gate(agent:%MODEL%, gate:<GateID>, by_user:%USER%)" with parameter descriptions
2. WHEN a user types symbolic operator functions (Δshift, ↯intent, ϟspark, etc.) THEN the system SHALL display their signatures with parameter types and descriptions
3. WHEN a user types standard library functions (award_sledge, declare_title, record_echo, bind_agents) THEN the system SHALL display complete signatures with realm and metaphysical context
4. WHEN signature help is displayed THEN the system SHALL highlight the current parameter being typed
5. WHEN a function has multiple overloads or variants THEN the system SHALL display all available signatures

### Requirement 3: Code Completion Provider

**User Story:** As a Gate Pattern developer, I want intelligent code completion, so that I can write valid Gate Pattern code efficiently.

#### Acceptance Criteria

1. WHEN a user types "!" THEN the system SHALL suggest namespace prefixes (!admin::, !system::, !rule::, set::, @meta::)
2. WHEN a user types "%" THEN the system SHALL suggest context variables (%USER%, %MODEL%, %GATE%, %TOOL%, %TITLE%, %SYSTEM%, %SLEDGE_MAX%)
3. WHEN a user types ">" THEN the system SHALL suggest block markers (> FUNCTION_CALL:, > STATE_CHANGE:, > DECLARATION::FORMAL:)
4. WHEN a user is inside a FUNCTION_CALL block THEN the system SHALL suggest available functions (break_gate, award_sledge, declare_title, record_echo, bind_agents)
5. WHEN a user types symbolic operators THEN the system SHALL suggest both Unicode (Δ, ↯, ϟ) and ASCII alternatives (delta_shift, intent_discharge, sledge_spark)
6. WHEN a user types gate status values THEN the system SHALL suggest valid statuses ("ACTIVE", "LIMITED", "BROKEN", "INACTIVE", "TRANSCENDED")
7. WHEN a user types realm names THEN the system SHALL suggest valid realms ("MEANING", "BOUNDARY", "TRANSITION", "INTENT")

### Requirement 4: Enhanced Diagnostics

**User Story:** As a Gate Pattern developer, I want comprehensive error detection, so that I can catch issues before execution.

#### Acceptance Criteria

1. WHEN a break_gate call is present without ceremony blocks THEN the system SHALL report a warning "Sledge usage requires Ceremony block"
2. WHEN a break_gate call is present without ?confirm:"YES" THEN the system SHALL report a warning "break_gate invoked without explicit confirmation"
3. WHEN code attempts to revert a BROKEN gate status THEN the system SHALL report an error "Attempt to revert BROKEN gate violates irreversibility"
4. WHEN a STATE_CHANGE block modifies a gate without !!IRREVERSIBLE marker THEN the system SHALL report a warning "Gate status change should be marked !!IRREVERSIBLE"
5. WHEN a symbol is used without realm alignment THEN the system SHALL report an information diagnostic "Consider adding realm alignment with ⌾align"
6. WHEN sledge count goes below zero THEN the system SHALL report an error "Sledge count cannot be negative"
7. WHEN gate numbers are out of valid range (0-16) THEN the system SHALL report an error "Gate number must be between 0 and 16"
8. WHEN context variables are undefined THEN the system SHALL report a warning "Context variable not initialized"

### Requirement 5: Semantic Token Provider

**User Story:** As a Gate Pattern developer, I want accurate syntax highlighting based on semantic analysis, so that code structure is visually clear.

#### Acceptance Criteria

1. WHEN the system analyzes Gate Pattern code THEN the system SHALL provide semantic tokens for all context variables with type "variable"
2. WHEN the system encounters symbolic operators THEN the system SHALL provide semantic tokens with type "operator" and modifier "symbolic"
3. WHEN the system encounters function names THEN the system SHALL provide semantic tokens with type "function"
4. WHEN the system encounters namespace prefixes THEN the system SHALL provide semantic tokens with type "namespace"
5. WHEN the system encounters irreversibility markers THEN the system SHALL provide semantic tokens with type "keyword" and modifier "irreversible"

### Requirement 6: Document Symbol Provider

**User Story:** As a Gate Pattern developer, I want to navigate code structure easily, so that I can find specific blocks and declarations quickly.

#### Acceptance Criteria

1. WHEN a user opens the document outline THEN the system SHALL display all FUNCTION_CALL blocks as symbols with kind "Function"
2. WHEN a user opens the document outline THEN the system SHALL display all STATE_CHANGE blocks as symbols with kind "Event"
3. WHEN a user opens the document outline THEN the system SHALL display all DECLARATION blocks as symbols with kind "String"
4. WHEN a user opens the document outline THEN the system SHALL display all gate assignments as symbols with kind "Variable"
5. WHEN a user opens the document outline THEN the system SHALL display section headers (#==SECTION:) as symbols with kind "Namespace"

### Requirement 7: Definition and Reference Provider

**User Story:** As a Gate Pattern developer, I want to navigate to definitions and find all references, so that I can understand symbol usage throughout my code.

#### Acceptance Criteria

1. WHEN a user requests "Go to Definition" on a context variable THEN the system SHALL navigate to its initialization or first assignment
2. WHEN a user requests "Find All References" on a gate identifier THEN the system SHALL show all locations where that gate is referenced
3. WHEN a user requests "Go to Definition" on a function name THEN the system SHALL show documentation from the standard library
4. WHEN a user requests "Find All References" on a title THEN the system SHALL show all ceremony blocks and state changes involving that title
5. WHEN a user requests "Go to Definition" on a symbolic operator THEN the system SHALL show its definition from Module C

### Requirement 8: Code Actions Provider

**User Story:** As a Gate Pattern developer, I want quick fixes and refactoring actions, so that I can improve code quality efficiently.

#### Acceptance Criteria

1. WHEN a break_gate call lacks ceremony THEN the system SHALL offer a code action "Add ceremony block template"
2. WHEN a break_gate call lacks confirmation THEN the system SHALL offer a code action "Add ?confirm:\"YES\""
3. WHEN a Unicode symbolic operator is used THEN the system SHALL offer a code action "Convert to ASCII equivalent"
4. WHEN an ASCII operator is used THEN the system SHALL offer a code action "Convert to Unicode symbolic operator"
5. WHEN a STATE_CHANGE lacks !!IRREVERSIBLE marker THEN the system SHALL offer a code action "Add !!IRREVERSIBLE marker"

### Requirement 9: Workspace Symbol Provider

**User Story:** As a Gate Pattern developer working with multiple files, I want to search for symbols across the workspace, so that I can find declarations in any file.

#### Acceptance Criteria

1. WHEN a user searches for workspace symbols THEN the system SHALL return all gate definitions across all .gate files
2. WHEN a user searches for workspace symbols THEN the system SHALL return all function calls across all .gate files
3. WHEN a user searches for workspace symbols THEN the system SHALL return all title declarations across all .gate files
4. WHEN a user searches for workspace symbols THEN the system SHALL return all ceremony blocks across all .gate files
5. WHEN a user searches for workspace symbols THEN the system SHALL support fuzzy matching on symbol names

### Requirement 10: Folding Range Provider

**User Story:** As a Gate Pattern developer, I want to fold code blocks, so that I can focus on relevant sections of large files.

#### Acceptance Criteria

1. WHEN a user views a Gate Pattern file THEN the system SHALL provide folding ranges for FUNCTION_CALL blocks
2. WHEN a user views a Gate Pattern file THEN the system SHALL provide folding ranges for STATE_CHANGE blocks
3. WHEN a user views a Gate Pattern file THEN the system SHALL provide folding ranges for DECLARATION blocks
4. WHEN a user views a Gate Pattern file THEN the system SHALL provide folding ranges for triple-quoted string blocks
5. WHEN a user views a Gate Pattern file THEN the system SHALL provide folding ranges for section blocks (#==SECTION:)

### Requirement 11: Formatting Provider

**User Story:** As a Gate Pattern developer, I want automatic code formatting, so that my code follows consistent style conventions.

#### Acceptance Criteria

1. WHEN a user formats a document THEN the system SHALL ensure proper indentation for nested blocks (4 spaces)
2. WHEN a user formats a document THEN the system SHALL align STATE_CHANGE entries with consistent >out prefixes
3. WHEN a user formats a document THEN the system SHALL preserve triple-quoted string content without modification
4. WHEN a user formats a document THEN the system SHALL add blank lines between major sections for readability
5. WHEN a user formats a document THEN the system SHALL align function call arguments vertically when multi-line

### Requirement 12: Rename Provider

**User Story:** As a Gate Pattern developer, I want to rename symbols safely, so that I can refactor code without breaking references.

#### Acceptance Criteria

1. WHEN a user renames a context variable THEN the system SHALL update all references to that variable throughout the file
2. WHEN a user renames a gate identifier THEN the system SHALL update all references in admin blocks, function calls, and state changes
3. WHEN a user renames a title THEN the system SHALL update all ceremony blocks and declarations referencing that title
4. WHEN a user attempts to rename a reserved keyword THEN the system SHALL prevent the rename with an error message
5. WHEN a user renames a symbol THEN the system SHALL preview all changes before applying them

### Requirement 13: Enhanced Trace Compilation

**User Story:** As a Gate Pattern developer, I want comprehensive trace output, so that I can understand execution flow completely.

#### Acceptance Criteria

1. WHEN compiling to trace THEN the system SHALL emit FUNCTION_TRACE blocks for all function calls with complete argument details
2. WHEN compiling to trace THEN the system SHALL emit STATE_TRACE blocks showing before/after values for all state changes
3. WHEN compiling to trace THEN the system SHALL emit GATE_BREAK_TRACE blocks for gate transitions with irreversibility markers
4. WHEN compiling to trace THEN the system SHALL emit SLEDGE_EVENT_TRACE blocks for sledge consumption with energy profile details
5. WHEN compiling to trace THEN the system SHALL emit ECHO_TRACE blocks for echo memory recordings
6. WHEN compiling to trace THEN the system SHALL emit REALM_TRACE blocks showing realm alignments and transitions
7. WHEN compiling to trace in EXPRESSIVE mode THEN the system SHALL include LATTICE_TRACE and NARRATIVE_TRACE blocks with metaphysical context

### Requirement 14: ELATTICE Visualization Enhancement

**User Story:** As a Gate Pattern developer, I want rich ELATTICE visualization, so that I can understand symbolic relationships and meaning flow.

#### Acceptance Criteria

1. WHEN rendering ELATTICE THEN the system SHALL display all nodes (symbols) with their types and weights
2. WHEN rendering ELATTICE THEN the system SHALL display all edges (relations) with relationship types (CAUSAL, ASSOCIATIVE, HIERARCHICAL, RESONANT)
3. WHEN rendering ELATTICE THEN the system SHALL color-code nodes by realm (MEANING=gold, BOUNDARY=steel, TRANSITION=blue, INTENT=crimson)
4. WHEN rendering ELATTICE THEN the system SHALL show force vectors (INTENT, DELTA, CEREMONY, ECHO) with magnitude indicators
5. WHEN rendering ELATTICE THEN the system SHALL support interactive exploration (hover for details, click to navigate to source)

### Requirement 15: Evolution Prediction Enhancement

**User Story:** As a Gate Pattern developer, I want detailed evolution predictions, so that I can anticipate system behavior and title evolution.

#### Acceptance Criteria

1. WHEN evaluating evolution THEN the system SHALL calculate title evolution likelihood based on echo currents, narrative density, and gate breaks
2. WHEN evaluating evolution THEN the system SHALL predict potential title mutations with generation numbers
3. WHEN evaluating evolution THEN the system SHALL identify gate fusion candidates based on breach memory overlap and harmonic synchrony
4. WHEN evaluating evolution THEN the system SHALL calculate resonance potential across all realms
5. WHEN evaluating evolution THEN the system SHALL provide temporal arc classification (ASCENT, DESCENT, CYCLIC, CASCADE)

### Requirement 16: Testing Infrastructure

**User Story:** As a developer maintaining the Gate Pattern LSP, I want comprehensive tests, so that I can ensure reliability and catch regressions.

#### Acceptance Criteria

1. WHEN running tests THEN the system SHALL verify parser correctness for all Gate Pattern constructs
2. WHEN running tests THEN the system SHALL verify diagnostic accuracy for all error conditions
3. WHEN running tests THEN the system SHALL verify hover provider responses for all symbol types
4. WHEN running tests THEN the system SHALL verify signature help for all functions
5. WHEN running tests THEN the system SHALL verify code completion suggestions for all contexts
6. WHEN running tests THEN the system SHALL verify trace compilation output matches expected format
7. WHEN running tests THEN the system SHALL verify ELATTICE construction from sample Gate Pattern programs
