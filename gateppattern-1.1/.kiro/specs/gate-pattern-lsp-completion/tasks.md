# Implementation Plan

- [ ] 1. Set up enhanced parser foundation
  - Create complete tokenizer with all Gate Pattern tokens (!, %, >, #==, symbolic operators, etc.)
  - Define all AST node type interfaces from Module D
  - Implement basic parser structure with error recovery
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [ ] 1.1 Write property test for AST completeness
  - **Property 1: AST Completeness**
  - **Validates: Requirements 1.1**

- [ ] 1.2 Write property test for admin directive parsing
  - **Property 2: Admin Directive Parsing**
  - **Validates: Requirements 1.2**

- [ ] 1.3 Write property test for context variable recognition
  - **Property 3: Context Variable Recognition**
  - **Validates: Requirements 1.3**

- [ ] 1.4 Write property test for symbolic operator parsing
  - **Property 4: Symbolic Operator Parsing**
  - **Validates: Requirements 1.4**

- [ ] 1.5 Write property test for function call parsing
  - **Property 5: Function Call Parsing**
  - **Validates: Requirements 1.5**

- [ ] 2. Implement semantic analyzer core
  - Create symbol table data structures (ContextVarSymbol, GateSymbol, FunctionSymbol, TitleSymbol)
  - Implement scope resolver for context variables and gates
  - Build semantic validator for metaphysical rules (irreversibility, ceremony, realm alignment)
  - Create symbol lookup and reference tracking
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8_

- [ ] 2.1 Write property test for ceremony requirement detection
  - **Property 14: Ceremony Requirement Detection**
  - **Validates: Requirements 4.1**

- [ ] 2.2 Write property test for confirmation requirement detection
  - **Property 15: Confirmation Requirement Detection**
  - **Validates: Requirements 4.2**

- [ ] 2.3 Write property test for irreversibility violation detection
  - **Property 16: Irreversibility Violation Detection**
  - **Validates: Requirements 4.3**

- [ ] 2.4 Write property test for sledge count validation
  - **Property 19: Sledge Count Validation**
  - **Validates: Requirements 4.6**

- [ ] 2.5 Write property test for gate number range validation
  - **Property 20: Gate Number Range Validation**
  - **Validates: Requirements 4.7**

- [ ] 3. Enhance hover provider
  - Extend existing gateHover.ts with semantic information from symbol table
  - Add hover for all symbolic operators with Module C definitions
  - Add hover for context variables showing type and value
  - Add hover for gates showing status, realm, and resistance
  - Add hover for functions showing full signatures from standard library
  - _Requirements: 2.1, 7.3, 7.5_

- [ ] 4. Implement signature help provider
  - Create signature definitions for all standard library functions (break_gate, award_sledge, etc.)
  - Create signature definitions for symbolic operator functions (Δshift, ↯intent, etc.)
  - Implement parameter position detection and highlighting
  - Handle function overloads and variants
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

- [ ] 4.1 Write property test for symbolic operator signatures
  - **Property 6: Symbolic Operator Signatures**
  - **Validates: Requirements 2.2**

- [ ] 4.2 Write property test for standard library signatures
  - **Property 7: Standard Library Signatures**
  - **Validates: Requirements 2.3**

- [ ] 4.3 Write property test for parameter highlighting
  - **Property 8: Parameter Highlighting**
  - **Validates: Requirements 2.4**


- [ ] 5. Implement code completion provider
  - Create completion items for namespace prefixes (!, %, >, #==)
  - Create completion items for context variables
  - Create completion items for block markers
  - Implement context-aware completion (inside FUNCTION_CALL, STATE_CHANGE, etc.)
  - Create completion items for symbolic operators (both Unicode and ASCII)
  - Create completion items for gate statuses and realm names
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7_

- [ ] 5.1 Write property test for context-aware function completion
  - **Property 10: Context-Aware Function Completion**
  - **Validates: Requirements 3.4**

- [ ] 5.2 Write property test for operator dual-form completion
  - **Property 11: Operator Dual-Form Completion**
  - **Validates: Requirements 3.5**

- [ ] 5.3 Write property test for gate status completion
  - **Property 12: Gate Status Completion**
  - **Validates: Requirements 3.6**

- [ ] 5.4 Write property test for realm completion
  - **Property 13: Realm Completion**
  - **Validates: Requirements 3.7**

- [ ] 6. Enhance diagnostic provider
  - Extend existing gateDiagnostics.ts with semantic analysis results
  - Implement all diagnostic codes (ceremony, confirmation, irreversibility, etc.)
  - Add diagnostic for missing realm alignment
  - Add diagnostic for undefined context variables
  - Add diagnostic for invalid gate numbers and negative sledge counts
  - Add diagnostic for missing !!IRREVERSIBLE markers
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8_

- [ ] 6.1 Write property test for irreversible marker detection
  - **Property 17: Irreversible Marker Detection**
  - **Validates: Requirements 4.4**

- [ ] 6.2 Write property test for realm alignment detection
  - **Property 18: Realm Alignment Detection**
  - **Validates: Requirements 4.5**

- [ ] 6.3 Write property test for undefined variable detection
  - **Property 21: Undefined Variable Detection**
  - **Validates: Requirements 4.8**

- [ ] 7. Implement semantic token provider
  - Create semantic token legend with all token types and modifiers
  - Implement token generation for context variables
  - Implement token generation for symbolic operators
  - Implement token generation for function names
  - Implement token generation for namespace prefixes
  - Implement token generation for irreversibility markers
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [ ] 7.1 Write property test for context variable token generation
  - **Property 22: Context Variable Token Generation**
  - **Validates: Requirements 5.1**

- [ ] 7.2 Write property test for symbolic operator token generation
  - **Property 23: Symbolic Operator Token Generation**
  - **Validates: Requirements 5.2**

- [ ] 7.3 Write property test for function name token generation
  - **Property 24: Function Name Token Generation**
  - **Validates: Requirements 5.3**

- [ ] 7.4 Write property test for namespace token generation
  - **Property 25: Namespace Token Generation**
  - **Validates: Requirements 5.4**

- [ ] 7.5 Write property test for irreversibility marker token generation
  - **Property 26: Irreversibility Marker Token Generation**
  - **Validates: Requirements 5.5**

- [ ] 8. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.


- [ ] 9. Implement document symbol provider
  - Extract FUNCTION_CALL blocks as Function symbols
  - Extract STATE_CHANGE blocks as Event symbols
  - Extract DECLARATION blocks as String symbols
  - Extract gate assignments as Variable symbols
  - Extract section headers as Namespace symbols
  - Build hierarchical symbol tree
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [ ] 9.1 Write property test for function call symbol extraction
  - **Property 27: Function Call Symbol Extraction**
  - **Validates: Requirements 6.1**

- [ ] 9.2 Write property test for state change symbol extraction
  - **Property 28: State Change Symbol Extraction**
  - **Validates: Requirements 6.2**

- [ ] 9.3 Write property test for declaration symbol extraction
  - **Property 29: Declaration Symbol Extraction**
  - **Validates: Requirements 6.3**

- [ ] 9.4 Write property test for gate assignment symbol extraction
  - **Property 30: Gate Assignment Symbol Extraction**
  - **Validates: Requirements 6.4**

- [ ] 9.5 Write property test for section header symbol extraction
  - **Property 31: Section Header Symbol Extraction**
  - **Validates: Requirements 6.5**

- [ ] 10. Implement definition provider
  - Implement "Go to Definition" for context variables (navigate to initialization)
  - Implement "Go to Definition" for functions (show Module C documentation)
  - Implement "Go to Definition" for symbolic operators (show Module C definition)
  - Implement "Go to Definition" for gates (navigate to admin declaration)
  - _Requirements: 7.1, 7.3, 7.5_

- [ ] 10.1 Write property test for context variable definition navigation
  - **Property 32: Context Variable Definition Navigation**
  - **Validates: Requirements 7.1**

- [ ] 10.2 Write property test for function definition lookup
  - **Property 34: Function Definition Lookup**
  - **Validates: Requirements 7.3**

- [ ] 10.3 Write property test for operator definition lookup
  - **Property 36: Operator Definition Lookup**
  - **Validates: Requirements 7.5**

- [ ] 11. Implement reference provider
  - Implement "Find All References" for context variables
  - Implement "Find All References" for gates (admin blocks, function calls, state changes)
  - Implement "Find All References" for titles (ceremony blocks, declarations)
  - Build reference index for fast lookup
  - _Requirements: 7.2, 7.4_

- [ ] 11.1 Write property test for gate reference finding
  - **Property 33: Gate Reference Finding**
  - **Validates: Requirements 7.2**

- [ ] 11.2 Write property test for title reference finding
  - **Property 35: Title Reference Finding**
  - **Validates: Requirements 7.4**

- [ ] 12. Implement rename provider
  - Implement rename for context variables (update all references)
  - Implement rename for gate identifiers (update admin blocks, calls, state changes)
  - Implement rename for titles (update ceremony blocks, declarations)
  - Implement reserved keyword protection
  - Implement rename preview generation
  - _Requirements: 12.1, 12.2, 12.3, 12.4, 12.5_

- [ ] 12.1 Write property test for context variable rename completeness
  - **Property 57: Context Variable Rename Completeness**
  - **Validates: Requirements 12.1**

- [ ] 12.2 Write property test for gate identifier rename completeness
  - **Property 58: Gate Identifier Rename Completeness**
  - **Validates: Requirements 12.2**

- [ ] 12.3 Write property test for title rename completeness
  - **Property 59: Title Rename Completeness**
  - **Validates: Requirements 12.3**

- [ ] 12.4 Write property test for reserved keyword protection
  - **Property 60: Reserved Keyword Protection**
  - **Validates: Requirements 12.4**


- [ ] 13. Implement code action provider
  - Create "Add ceremony block template" action for break_gate without ceremony
  - Create "Add ?confirm:\"YES\"" action for break_gate without confirmation
  - Create "Convert to ASCII equivalent" action for Unicode operators
  - Create "Convert to Unicode symbolic operator" action for ASCII operators
  - Create "Add !!IRREVERSIBLE marker" action for STATE_CHANGE without marker
  - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [ ] 13.1 Write property test for ceremony addition action
  - **Property 37: Ceremony Addition Action**
  - **Validates: Requirements 8.1**

- [ ] 13.2 Write property test for confirmation addition action
  - **Property 38: Confirmation Addition Action**
  - **Validates: Requirements 8.2**

- [ ] 13.3 Write property test for Unicode to ASCII conversion action
  - **Property 39: Unicode to ASCII Conversion Action**
  - **Validates: Requirements 8.3**

- [ ] 13.4 Write property test for ASCII to Unicode conversion action
  - **Property 40: ASCII to Unicode Conversion Action**
  - **Validates: Requirements 8.4**

- [ ] 13.5 Write property test for irreversible marker addition action
  - **Property 41: Irreversible Marker Addition Action**
  - **Validates: Requirements 8.5**

- [ ] 14. Implement workspace symbol provider
  - Build workspace-wide symbol index
  - Implement symbol search across all .gate files
  - Implement fuzzy matching for symbol names
  - Return gates, functions, titles, and ceremonies from all files
  - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5_

- [ ] 14.1 Write property test for workspace gate discovery
  - **Property 42: Workspace Gate Discovery**
  - **Validates: Requirements 9.1**

- [ ] 14.2 Write property test for workspace function discovery
  - **Property 43: Workspace Function Discovery**
  - **Validates: Requirements 9.2**

- [ ] 14.3 Write property test for workspace title discovery
  - **Property 44: Workspace Title Discovery**
  - **Validates: Requirements 9.3**

- [ ] 14.4 Write property test for workspace ceremony discovery
  - **Property 45: Workspace Ceremony Discovery**
  - **Validates: Requirements 9.4**

- [ ] 14.5 Write property test for fuzzy symbol matching
  - **Property 46: Fuzzy Symbol Matching**
  - **Validates: Requirements 9.5**

- [ ] 15. Implement folding range provider
  - Detect FUNCTION_CALL blocks for folding
  - Detect STATE_CHANGE blocks for folding
  - Detect DECLARATION blocks for folding
  - Detect triple-quoted string blocks for folding
  - Detect section blocks (#==SECTION:) for folding
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_

- [ ] 15.1 Write property test for function call folding
  - **Property 47: Function Call Folding**
  - **Validates: Requirements 10.1**

- [ ] 15.2 Write property test for state change folding
  - **Property 48: State Change Folding**
  - **Validates: Requirements 10.2**

- [ ] 15.3 Write property test for declaration folding
  - **Property 49: Declaration Folding**
  - **Validates: Requirements 10.3**

- [ ] 15.4 Write property test for triple-quoted string folding
  - **Property 50: Triple-Quoted String Folding**
  - **Validates: Requirements 10.4**

- [ ] 15.5 Write property test for section folding
  - **Property 51: Section Folding**
  - **Validates: Requirements 10.5**

- [ ] 16. Checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.


- [ ] 17. Implement formatting provider
  - Implement indentation normalization (4 spaces for nested blocks)
  - Implement STATE_CHANGE alignment (consistent >out prefixes)
  - Implement triple-quoted string preservation (invariant)
  - Implement section spacing (blank lines between sections)
  - Implement multi-line function call argument alignment
  - _Requirements: 11.1, 11.2, 11.3, 11.4, 11.5_

- [ ] 17.1 Write property test for indentation consistency
  - **Property 52: Indentation Consistency**
  - **Validates: Requirements 11.1**

- [ ] 17.2 Write property test for state change alignment
  - **Property 53: State Change Alignment**
  - **Validates: Requirements 11.2**

- [ ] 17.3 Write property test for string content preservation
  - **Property 54: String Content Preservation**
  - **Validates: Requirements 11.3**

- [ ] 17.4 Write property test for section spacing
  - **Property 55: Section Spacing**
  - **Validates: Requirements 11.4**

- [ ] 17.5 Write property test for argument alignment
  - **Property 56: Argument Alignment**
  - **Validates: Requirements 11.5**

- [ ] 18. Enhance trace compiler
  - Extend existing gateTraceEngine.ts with all trace types
  - Implement FUNCTION_TRACE emission with complete argument details
  - Implement STATE_TRACE emission with before/after values
  - Implement GATE_BREAK_TRACE emission with irreversibility markers
  - Implement SLEDGE_EVENT_TRACE emission with energy profile
  - Implement ECHO_TRACE emission for echo memory
  - Implement REALM_TRACE emission for realm operations
  - Implement EXPRESSIVE mode with LATTICE_TRACE and NARRATIVE_TRACE
  - _Requirements: 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7_

- [ ] 18.1 Write property test for function trace completeness
  - **Property 62: Function Trace Completeness**
  - **Validates: Requirements 13.1**

- [ ] 18.2 Write property test for state trace generation
  - **Property 63: State Trace Generation**
  - **Validates: Requirements 13.2**

- [ ] 18.3 Write property test for gate break trace generation
  - **Property 64: Gate Break Trace Generation**
  - **Validates: Requirements 13.3**

- [ ] 18.4 Write property test for sledge event trace generation
  - **Property 65: Sledge Event Trace Generation**
  - **Validates: Requirements 13.4**

- [ ] 18.5 Write property test for echo trace generation
  - **Property 66: Echo Trace Generation**
  - **Validates: Requirements 13.5**

- [ ] 18.6 Write property test for realm trace generation
  - **Property 67: Realm Trace Generation**
  - **Validates: Requirements 13.6**

- [ ] 18.7 Write property test for expressive mode trace enhancement
  - **Property 68: Expressive Mode Trace Enhancement**
  - **Validates: Requirements 13.7**

- [ ] 19. Implement ELATTICE builder
  - Create ELATTICE data structure (nodes, edges, forces, weights, harmonics)
  - Extract symbols as lattice nodes with types and realms
  - Detect relationships as lattice edges (CAUSAL, ASSOCIATIVE, HIERARCHICAL, RESONANT)
  - Calculate force vectors (INTENT, DELTA, CEREMONY, ECHO)
  - Calculate weights and harmonics
  - Implement realm-based color coding
  - _Requirements: 14.1, 14.2, 14.3, 14.4_

- [ ] 19.1 Write property test for node completeness
  - **Property 69: Node Completeness**
  - **Validates: Requirements 14.1**

- [ ] 19.2 Write property test for edge completeness
  - **Property 70: Edge Completeness**
  - **Validates: Requirements 14.2**

- [ ] 19.3 Write property test for realm color coding
  - **Property 71: Realm Color Coding**
  - **Validates: Requirements 14.3**

- [ ] 19.4 Write property test for force vector display
  - **Property 72: Force Vector Display**
  - **Validates: Requirements 14.4**


- [ ] 20. Enhance evolution predictor
  - Extend existing gateEvolution.ts with advanced metrics
  - Implement title evolution likelihood calculation (echo currents, narrative density, gate breaks)
  - Implement title mutation prediction with generation numbers
  - Implement gate fusion detection (breach memory overlap, harmonic synchrony)
  - Implement resonance calculation across all realms
  - Implement temporal arc classification (ASCENT, DESCENT, CYCLIC, CASCADE)
  - _Requirements: 15.1, 15.2, 15.3, 15.4, 15.5_

- [ ] 20.1 Write property test for title evolution likelihood calculation
  - **Property 73: Title Evolution Likelihood Calculation**
  - **Validates: Requirements 15.1**

- [ ] 20.2 Write property test for title mutation prediction
  - **Property 74: Title Mutation Prediction**
  - **Validates: Requirements 15.2**

- [ ] 20.3 Write property test for gate fusion detection
  - **Property 75: Gate Fusion Detection**
  - **Validates: Requirements 15.3**

- [ ] 20.4 Write property test for resonance calculation
  - **Property 76: Resonance Calculation**
  - **Validates: Requirements 15.4**

- [ ] 20.5 Write property test for temporal arc classification
  - **Property 77: Temporal Arc Classification**
  - **Validates: Requirements 15.5**

- [ ] 21. Update client extension commands
  - Update compileToTrace command to use enhanced trace compiler
  - Update renderELattice command to use ELATTICE builder with interactive visualization
  - Update evaluateEvolution command to use enhanced evolution predictor
  - Add new commands for navigation features (go to definition, find references)
  - Wire up all new LSP providers in client/src/extension.ts
  - _Requirements: All_

- [ ] 22. Create test infrastructure
  - Set up Jest test framework
  - Set up fast-check for property-based testing
  - Create test fixtures (valid programs, invalid programs, edge cases)
  - Create property test generators for Gate Pattern constructs
  - Create test utilities for AST comparison, symbol table validation
  - _Requirements: 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7_

- [ ] 22.1 Write unit tests for parser
  - Test tokenizer with all token types
  - Test AST builder with all node types
  - Test error recovery mechanisms
  - _Requirements: 16.1_

- [ ] 22.2 Write unit tests for semantic analyzer
  - Test symbol table construction
  - Test scope resolution
  - Test semantic validation
  - _Requirements: 16.2_

- [ ] 22.3 Write unit tests for LSP providers
  - Test hover provider responses
  - Test completion provider suggestions
  - Test signature help provider
  - Test diagnostic provider
  - _Requirements: 16.3, 16.4, 16.5_

- [ ] 22.4 Write integration tests
  - Test LSP protocol request/response cycles
  - Test multi-document scenarios
  - Test trace compilation → ELATTICE pipeline
  - _Requirements: 16.6, 16.7_

- [ ] 23. Performance optimization
  - Implement incremental parsing
  - Implement AST caching
  - Implement symbol table caching
  - Add performance metrics collection
  - Optimize hot paths identified by profiling
  - _Design: Performance Considerations_

- [ ] 24. Documentation and polish
  - Update README.md with new features
  - Create CHANGELOG.md entry for v1.1.0
  - Add JSDoc comments to all public APIs
  - Create user guide for new features
  - Add examples of all LSP features
  - _Design: Deployment Strategy_

- [ ] 25. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.
