# Applications

Full-featured applications built with UDL technologies.

## Projects

### **[black-milk](black-milk/)** ⭐
Bitburner-inspired hacking game built with Godot

**Features:**
- Custom DSL/VM for in-game scripting
- Pure domain logic architecture (SRP)
- Network simulation with security mechanics
- ASCII/retro terminal UI
- Extensible plugin system

**Tech Stack:** GDScript, Custom DSL

---

### **[StrawberryMause](StrawberryMause/)** ⭐
Mouse event recording and playback system with grid-based timeline

**Features:**
- OS-level event capture (macOS CGEventTap)
- Mathematical grid coordinate system
- Timeline visualization with 60Hz updates
- Event data analysis and metrics
- High-precision playback

**Tech Stack:** TypeScript, Electron

---

### **[ASCII-String-UI-Editor](ASCII-String-UI-Editor/)**
Terminal UI editor and ASCII string renderer

**Features:**
- ASCII art editing
- String manipulation
- Export to various formats
- Terminal rendering

**Tech Stack:** TypeScript, HTML5

## Development

Each application has its own development setup. See project-specific READMEs.

### black-milk (Godot)
```bash
# Requires Godot 4.0+
cd projects/applications/black-milk
# Open in Godot Editor
```

### StrawberryMause (Electron)
```bash
cd projects/applications/StrawberryMause
pnpm install
pnpm dev
```

### ASCII-String-UI-Editor (Web)
```bash
cd projects/applications/ASCII-String-UI-Editor
pnpm install
pnpm dev
```

## Architecture Patterns

Applications in this category follow:
- **Clean Architecture** - Separation of concerns
- **Event-Driven** - Decoupled components
- **Domain-First** - Business logic separate from UI
- **Testable** - Pure functions and mocked dependencies
