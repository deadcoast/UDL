# f8 Syntax - Build for the Algorithm Fate Analyzer Application (AFAA)

## Introduction

### F8 Syntax How it Works

- **F8 Syntax** - A customizable, self contained and simple bracket based syntax. - F8 runs primarely on the organizational structure of the **F8ZeroBracket System**. - The **F8ZeroBracket System** is a bracket based syntax that runs on TAB spacing. - **PleaseNote:** `F8BS` is a common acronym used in this documentation for the **F8ZeroBracket System**. - F8 Enforses a Two Tier vertical heirarchy in its 5 tier organization system.
  `        - What this means is, the first two brackets require a reachable vertical connection through the code blocks structure.` - **AlphaBracket** - The First tier functions. - The AlphaBracket is the main control point of each and every code block. - This tier helps structure and modularize the code, ensuring the entire code file is structured and modularized. - _The Vertical heirarchy is enforcedin this tier._ - **Initializers** - The Second tier functions. - The initializers control the validation and requirements of the code block. - They from the main F8 AlphaBracket. - _The Vertical heirarchy is enforcedin this tier._ - **Paramaters** - The third tier functions. - The Paramaters inherit from the Initializers, this tier handles definining the functions the Variables will operate on. - _The Vertical heirarchy is NOT enforcedin this tier._ - **Variables** - The fourth tier functions. - The Variables inherit from the Paramater's, this tier handles the specifics and definitions. - _The Vertical heirarchy is NOT enforced in this tier._ - **Execute** - The fifth tier functions. - The fifth tier is the execution code block. - This tier controls customizations and batch handing of your projects code, it helps customize exactly how and what is executed. - _The Vertical heirarchy is NOT enforced in this tier._

## Future Implementations

- **Future Implementations**
  - Offer a lint or built-in check that warns if indentation rules are violated—this saves frustration.
  - Offer a built-in check that warns if the F8BS is not used correctly—this saves frustration.
  - Providing a linter and parser to enforce F8 Syntax.
  - Allowing advanced users an opt-out or “lax” mode—only to dismiss the Vertical Two Tier Heirarchal Enforcement.
  - `strict mode` and `debug mode` that refuses to continue on syntax error.
    - This way, advanced users can force early failures to track down issues quickly, without having to implement the "req" Paramater.

### Tab Based

- F8 is a TAB strictly organized syntax. It focuses on modular codebases with its F8ZeroBracket System(F8BS), creating modular code blocks for all functions. It further enforces this structure by requiring the first two tiers of the F8BS to be aligned vertically. You will find that the F8BS creates an enhanced, rigid, reinforced and organized structure when building out your code blocks without the hassle of semi-colons and commas beside brackets.

### Error Friendly

- F8 is a continuous code system, it will continue its code fnction even through error. The Multiple levels of the F8BS system provides several layers of security and reinforcement to error interruptions. Additionally, the enhancements and modifications to the Executate statement allow the user to pinpoint what they want to use, where, or just leave it untill the end and put it all together. Another feature of the F8BS is it allows the code to compile much easier. All code blocks are encased for an easy setup and checkout for most compilers.

### Overview

- In short, f8Syntax will try its best to circumvent errors in the code and partially run what it can, when it can without the hassle of type checks and tedious imports. For further customizations, Paramaters functions like 'req' will create a strict and rigid enviornment when runnig the code, forcing F8 to shutdown without the attached req function.

## F8ZeroBracket System

- **F8ZeroBracket System** is a system of brackets that are used to encase the code block.
  - The F8BS is used to create a strict and rigid enviornment when running the code.
  - Below you will find the F8BS and its components, with their rules and examples.

### AlphaBracket

`<`: Opening Alpha Bracket
`>`: Closing Alpha Bracket

- All f8Syntax statements must start, and end with AlphaBrackets
- Opens and Closes entire chain of brackets Beta, Gamma, and Delta
- AlphaBrackets must align vertically, cannot be unreachable

### BetaBracket

`[`: Opening Beta Bracket
`]`: Closing Beta Bracket

- Encases Initiation Commands
- BetaBracket must align vertically, cannot be unreachable, cannot nest unless in closing `!EXEC!` EpsilotBracket.

### GammeBracket

`{`: Opening Gamma Bracket
`}`: Closing Gamma Bracket

- Encases **Paramaters**
- Gamma Bracket may be closed without OR without Vertical Alignment
- When stacking paramater definitions, you must close the previous bracket before opening a new one.

- **Example**

```f8
< F8:
    [INIT =
		{prohibited =
			(placeholderOne,
			placeholderTwo,
            placeholderThree)} # When stacking paramater definitions, you must close the previous bracket before opening a new one.
        {code_creation =
	        S.4: FULL CODE COMPLETION,
	        S.5: BEST IN PRACTISE GENERATION FOCUSED ON COMPLETE PROJECT IMPLEMENTATIONS
        }
    ]
>
```

### DeltaBracket

`(`: Opening Delta Bracket
`)`: Closing Delta Bracket

- Used to encase **Variables**

- **Variable Rules**
  - Variables must be:
    - encased in DeltaBrackets.
    - assigned to:
      - a Paramater.
      - a Command.
      - a Function.
      - a F8B.

- DeltaBracket may close without aligning vertically OR align vertically

### EpsilonBracket

`!`: Opening and Closing bracket for the `EXEC` Execute command (Return Command)
`!!`: Opening and Closing Copmpound EpsilonBracket for Complete Exectuion Statement (CES)

- **EpsilonBracket Rules**
  - EpsilonBracket must be:
  - Assigned to the `EXEC` Sequence.
    - Encased in a:
      - DeltaBracket.
      - AlphaBracket.
  - Must encapsulate all modifiers, variables and paramaters in its line.

## Controllers

`@@`: Chain Command Sequence

- Used to **Chain** Bridge Commands Together

- **Chain Controller Rules**
  - Can only be used after the Bridge Controller `:` gas been called on the same line.
  - Must be encapsulated by one of the F8BS.

`:`: Brige Commands Together

- **Bridge Controller Rules**
  - Always used after F8 is defined at the top of code block, to bridge the rest of the F8BS.
  - Used to **Bridge** Commands, Paramaters, and Variables Together.
  - Cannot be used more than once per line.
    - UNLESS followed by a Chain Sequencer `@@`.

`=`: Assignment Marker

- **Assignment Marker Rules**
  - Cannot be followed by any opening bracket.
  - Almost always followed by a new line.
  - May be followed only by a closing bracket of DeltaBracket.

`,`: Passes multiple variables in a string **or** a list.

- **Comma Rules**
  - Cannot be followed by any opening bracket.
  - Almost always followed by a new line.
  - May be followed only by a closing bracket of DeltaBracket.

### Docstring

`#`: Global Documenting Character

- **Docstring Rules**
  - Documenting Character for single file documentation.
  - The Single Docstring Characters can be placed Anywhere in the code block.

`##--#`: Docstring Opening Sequence

- **Docstring Opening Sequence Rules**
  - Docstring Sequences are used when a more verbose code tagging is needed.
  - Used to open a docstring sequence.
  - Open Docstring sequences can ONLY be placed Directly Above an AlphaBracket.

`#--##`: Docstring Closing Sequence

- **Docstring Closing Sequence Rules**
  - Docstring Closing Sequence.
  - Used to Close the Docstring Sequence.
  - Closing Docstring sequences can ONLY be placed Directly Above an AlphaBracket.

```f8
##--#
# Full Docstring Example
#--##
```

## Commands

`F8`: Main Command Call

- **Main Command Call Rules**
  - Main Command Call.
  - Must be placed after an opening Alpha Bracket.
  - Must be ALL CAPS.
  - Utilizes AlphaBracket.

`INIT`: Initiate Command Call for Paramaters

- **Initiate Command Call for Paramaters Rules**
  - Initiate Command Call for Paramaters.
  - Must be ALL CAPS.
  - Utilizes BetaBracket.

`param`: Initiate Command Call for Variables

- **Initiate Command Call for Variables Rules**
  - Initiate Command Call for Variables.
  - Must be all lowercase.
  - Utilizes GammaBracket.

`true`: Return `EXEC`

- **True Return `EXEC` Rules**
  - Confirms the Return `EXEC`.
  - Utilizes GammaBracket OR EpsilonBracket.
  - Must be lowercase.

`false`: Passes the Return `EXEC`

- **False Return `EXEC` Rules**
  - Passes the Return `EXEC`.
  - Utilizes GammaBracket OR EpsilonBracket.
  - Must be lowercase.

### EXEC Sequence

#### Universal EXEC Rules

- **Universal EXEC Rules**
  - All `EXEC` functions must start a new AlphaBracket directly after and attached to the closing AlphaBracket.
  - The `EXEC` functions must have their own open and closed EpsilonBracket.
  - The `EXEC` function must encase all modifiers and paramaters in its EpsilonBracket and AlphaBracket at the end of the code block.

#### EXEC and the EpsilonBracket

- **EXEC and the EpsilonBracket Rules**
  - Call the EpsilonBracket with `!EXEC!` in any code block to assign it to that specific block.
  - The EpsilonBracket allows you to add Modifiers with `:` OR, for advanced cases, call the Modifier Chain with `@@`.
  - If the modifier chain is envoked, that Command, Variable or function must be encased in its ZeroBracket.
  - If modifiers or paramaters are used, they must be encased in the `EXEC` function EpsilonBracket.

#### Compound EpsilonBracket

- **Compound EpsilonBracket Rules**
  - Compound EpsilonBracket call will execute a CES.
  - This will circumvent Function calling and confusion in type imports.
- Complete Exectuion Statement.
  - Omit EXEC calls in code blocks untill the end of your code file, calling it with Compound EpsilonBracket call function with `!!EXEC!!`.

#### EXEC Formats

`EXEC`

- **EXEC Rules**
  - Execute Code Sequence
  - Utilizes `!EpsilonBracket!`, `{`GammaBracket`}` Bridge Controller`:`, Chain Controller`@@`.

#### Usage Examples

- **Used to assing and execute a code block.**

`!EXEC!` - Used as a Partial Return Statement for Code Blocks.

`!EXEC:{param}!` - With Modifiers

`!EXEC:req = config!` - With modifiers and Chain Controller

`!EXEC:req = config @@ {floop:1}!` - Used as a Complete Execution Statement with Compound EpsilonBrackets.

`!!EXEC!!` - Complete Execution Statement for the entire code structure, can only be placed at the bottom of the code file.

- **Complete Example with AlphaBracket**.
  - Below we cover stacking Paramater Definitions and the default !EXEC! command.

```f8
< F8:
    [INIT =
		{prohibited =
			(placeholderOne,
			placeholderTwo,
            placeholderThree)} # When stacking Paramater Definitions, you must close the previous bracket before opening a new one.
        {code_creation =
	        (exampleOne,
	        exampleTwo)
        }
	]
>< !EXEC! > # Complete set of EpsilonBrackets and AlphaBracket.
```

### EXEC Modifiers and Variable Rules

#### Universal EXEC Modifier Rules

`floop`

- F8BS: `{`GammaBracket`}`
- Paramater modifier for looping code blocks with EXEC, Commands, Paramaters and Variables with F8ZeroBrackets.
- Requiresa numberic value, if specifying target functions, use `floop = (variable):(numeric_value)`.
- Loop command, takes numerical variations.
  - Used to run multiple iterations or loop the code block.
- If used after `@@` Chain, requires `{`GammaBracket`}`.

`req`

- F8BS: `{`GammaBracket`}`
- Used to Specify the lines, F8B, or functions when entire code block Execution is not desired.
  - To specify variable requirements, use `req:(variable)`.
  - If used after `@@` Chain, requires `{`GammaBracket`}`.

`prohib`

- F8BS: `{`GammaBracket`}`
- Requirement, unskippable. Forces the code to run this variable, if not found, code exits.
- Used to reinforce restrictive commands, variables, initiations or paramaters.
- Can be used as a cancel command or with variables in a f`loop`.
  - If used after `@@` Chain, requires `{`GammaBracket`}`.

## Code Examples

### Document Example Code Block

- Below we cover stacking paramater definitions and the default !EXEC! command.

```f8
< F8:
    [INIT =
		{prohibited =
			placeHolderOne,
			placeHolderTwo,
			placeHolderThree} # When stacking paramater definitions, you must close the previous bracket before opening a new one.
        {code_creation =
			exampleOne,
			exampleTwo
        }
	]
>< !EXEC! > # This will execute all identifiers in the code block.
```

### Complete Code Block Examples

```f8
##--#
# First Code Block
# Classic Vertical Alignment
#--##
< F8:
	[INIT =
		{param: =
			(Placeholder1,
			 Placeholder2,
			 Placeholder3)}
        {example_param =
			(Example_placeholder4
            Example_laceholder5)
		}
	]
>< !EXEC! > # This will execute all identifiers in the code block.

##--#
# Second Code Block
# Example of the correct Syntax for Nested Gamma and Delta Brackets that are not Vertically Aligned
#--##
< F8:
	[INIT =
		{list =
			(Placeholder1, Placeholder2, Placeholder3):(Example_placxeholder1, Examle_placeholder_2)
        }
	]
>< !EXEC:prohib = {list}! > # This will execute the code block with the prohibited paramaters, excluding the listed variables.
< F8:
	[INIT =
	    {prohib =
	        (Placeholder1,
		 Placeholder2,
		 Placeholder3,
		 Placeholder4,
	         Placeholder5,
	         Placeholder6,)
	    {param =
		 (ExampleParam1,
		 (ExampleParam2,
		(ExampleParam3,
		(ExampleParam4)

        }
	]
>< !!EXEC!! > # Compound EpsilonBracket with the Complete Execution Statement "!!EXEC!!"
```

### Config Code Block

- Below we cover a full docstring statement, and specifying !EXEC! modifiers.

```f8
##--#
# Fourth Code Block
# Example of Initiating the config with a forced req statement
# !EXEC! Statement with Bridge ':', 'req', and floop
# This force loads the config
#--##
< F8:
    [INIT =
        {req =
            (config = "Please provide the advanced YAML config for the script")} # Here we force the config to load, and nest the Gammabracket.
	]
>< !EXEC:{req} @@ {floop:(1) = (config)}! > # Alternatively, you can nest the req GammaBracket with the floop modifier. {req = @@ {floop:(1) = (config)}}
```
