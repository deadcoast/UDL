# axe:Syntax Documentation

**`axe:Syntax`** is a custom notation for building CLI Menus in **`axe:Builder`**, a Python-based menu builder. It uses a combination of **operators** and bracketed constructs to define Main Menus, Nested Menus, SubCommands, and their numeric variables.

**Step 1:** Create your Main Menus
**Step 2:** Title your Main Menus
**Step 3:** Create Nested Menus for each Main Menu
**Step 4:** Create the Contents (titles) of your Nested Menus
**Step 5:** Export your custom Menus to Python for your own Python CLI Template!

---

## Operators

### `:`
- **Purpose**: Chains or composes two commands (e.g., chaining a Main Menu `[M]` to a Nested Menu `[N]`).
- **Constraints**:  
  - Can only be used **once** per command line.  
  - Must **not** be enclosed in brackets, parentheses, or braces.

### `=`
- **Purpose**: Equates or assigns numeric values or outcomes to menu commands.
- **Usage**:  
  - Used within MenuCommands `[]` or SubCommands `()` to assign a `NumericVariable {}`.  
  - Example: `[M={2}]` means “the Main Menu `[M]` **2** is indicated for manipulation or additions.

### `+`
- **Purpose**: Adds or extends commands with additional options or variables.
- **Usage**:
- Used for additions to MenuCommands or SubCommands
  - Example: `[M+{2}]` means “The CLI will have two Main Menus`[M]`.
  - Example: `[M={2}]:[N+{2}]` means “The CLI will have two Nested Menus`[N]`.
  - Inside a MenuCommand to append extra SubCommands or NumericVariables.  
  - Example: `[N+(.)={6}]` means “the Nested Menu `[N]` is combined with a Custom SubCommand `(.)` and assigned **6**.”

### `""`
- **Purpose**: Encloses string-based content, such as titles or labels.
- **Usage**:  
  - Paired with `(T)` (the Title SubCommand) to define main menu and nested menu titles.  
  - Example: `(T="This is the Title")`.

---

## Hierarchy

1. **MenuCommands**: `[]`  
   - Represent main or top-level menus (e.g., `[M]` or `[N]`).  
   - Can contain **SubCommands** and/or **NumericVariables**.  
   - Example: `[M+{2}]` creates **2** Main Menus.

2. **SubCommands**: `()`  
   - Represent secondary or custom commands nested under a MenuCommand.  
   - **`(.)`** (Custom Command): Independent and must always be closed. Cannot enclose other commands.  
   - **`(T)`** (Title Command): Must enclose the `=` operator and the title string in quotes, e.g. `(T="My Title")`.

3. **NumericVariables**: `{}`  
   - Used to specify numeric parameters (e.g., specific menu identification, how many menus or sub-items to create).  
   - Always preceded by the `=` operator.  
   - Example: `{3}` indicates **3** items for that command.

---

## Quick Reference Examples

### 1. Creating Multiple Main Menus

```python
# [M+{3}] means:
# "[M]" - Main Menu Command
# "+"  - Add operation
# "{3}" - NumericVariable specifying 3 menus
[M+{3}]  # Creates 3 Main Menus
```

### 2. Creating Nested Menus

```python
# [M={2}] indicates Main Menu #2.
# ':' chains [M={2}] to [N+{3}], which indicates adding 3 Nested Menus.
# '+' indicates Nested Menu Additions.
[M={2}]:[N+{3}]
```

### 3. Adding a Title SubCommand

```python
# (T="Menu One Title") is a Title SubCommand.
# ':' chains the Main Menu [M+{1}] to the Title SubCommand (T=...).
[M={1}]:(T="This is the Title for Menu One")
```

### 4. Using a Custom SubCommand with Numeric Variables

```python
# [N+(.)={6}] 
#   "[N]" - Nested Menu
#   "+"   - Add
#   "(.)" - Custom SubCommand
#   "{6}" - NumericVariable specifying 6 items
[M={1}]:[N+(.)={6}]
```

---

## Complete Examples

### Example A: Three Nested Menus in Main Menu #2

1. `[M={2}]`  
   - Specify the **2nd Main Menu**.  
2. `:`  
   - Chain to the next command.  
4. `+`
   - Addition of Nested Menus.
5. `[N+{3}]`
   - Create **3** Nested Menus for that Main Menu.

**Full Syntax**:  
```python
[M={2}]:[N+{3}]
```

### Example B: Six Nested Menus in Main Menu #1 with a Custom SubCommand

1. `[M={1}]`  
   - Specify the **1st Main Menu**.  
2. `:`  
   - Chain to the next command.  
3. `[N+(.)={6}]`  
   - Append a Custom SubCommand `(.)` with a NumericVariable **6**.

**Full Syntax**:  
```python
[M={1}]:[N+(.)={6}]
```

---

## Summary

- **`[]`**: MenuCommands  
- **`()`**: SubCommands  
- **`{}`**: NumericVariables  
- **`:`**: Chaining/Composition Operator  
- **`=`**: Assignment/Equating Operator  
- **`+`**: Addition or Extension Operator  
- **`""`**: String Enclosure for titles or labels  

Use these operators and bracketed constructs to build hierarchical menus, define numeric parameters, and add titles or custom commands in a structured, readable way.
