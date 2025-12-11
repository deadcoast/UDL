# Tooling Scripts

**Purpose:** Shell scripts for monorepo operations and automation
**Status:** Active Infrastructure
**Category:** Build & Automation

## Overview

This directory contains shell scripts that automate common monorepo operations, setup, migration, and maintenance tasks.

## Available Scripts

### bootstrap.sh

**Purpose:** Complete development environment setup

```bash
./tooling/scripts/bootstrap.sh
```

**What it does:**
1. Checks system requirements
2. Installs PNPM (if not present)
3. Installs all Node.js dependencies
4. Sets up Python projects
5. Installs Rust toolchain (if Rust projects exist)
6. Configures git hooks
7. Validates the setup

**Requirements:**
- macOS or Linux
- Node.js >= 18.0.0
- Python >= 3.8 (for Python projects)
- Rust >= 1.70 (for Rust projects)

**Options:**
```bash
# Skip specific steps
./bootstrap.sh --skip-python
./bootstrap.sh --skip-rust

# Dry run
./bootstrap.sh --dry-run

# Verbose output
./bootstrap.sh --verbose
```

**Troubleshooting:**
```bash
# If bootstrap fails, check:
node --version  # Should be >= 18
python3 --version  # Should be >= 3.8

# Clean and retry
rm -rf node_modules pnpm-lock.yaml
./bootstrap.sh
```

---

### migrate-projects.sh

**Purpose:** Migrate projects to categorized monorepo structure

```bash
./tooling/scripts/migrate-projects.sh
```

**What it does:**
1. Creates category directories (if needed)
2. Moves projects to appropriate categories:
   - `languages/` - DSL implementations
   - `tools/` - CLI tools and utilities
   - `extensions/` - Editor extensions
   - `applications/` - Full applications
   - `libraries/` - Reusable libraries
   - `experimental/` - WIP projects
3. Preserves git history (via git mv)
4. Updates workspace configurations
5. Validates migration

**Safety Features:**
- Dry run mode (--dry-run)
- Confirmation prompts
- Backup recommendations
- Rollback instructions

**Options:**
```bash
# Dry run (show what would happen)
./migrate-projects.sh --dry-run

# Force migration (skip confirmations)
./migrate-projects.sh --force

# Migrate specific category only
./migrate-projects.sh --category=languages
```

**Post-Migration:**
```bash
# Verify migration
git status
pnpm install
pnpm build

# If issues, restore from backup
tar -xzf UDL-backup-*.tar.gz
```

## Script Standards

### Structure

All scripts should follow this structure:

```bash
#!/bin/bash
set -euo pipefail

# Script Name - Brief Description
# Usage: ./script-name.sh [options] [args]
#
# Options:
#   --dry-run    Show what would happen
#   --verbose    Verbose output
#   --help       Show this help

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Functions
show_help() {
    # Show usage information
}

main() {
    # Main script logic
}

# Entry point
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi
```

### Best Practices

1. **Error Handling**
   ```bash
   set -euo pipefail  # Exit on error, undefined vars, pipe failures
   trap cleanup EXIT  # Cleanup on exit
   ```

2. **Logging**
   ```bash
   log_info() { echo "[INFO] $*"; }
   log_error() { echo "[ERROR] $*" >&2; }
   log_success() { echo "[SUCCESS] $*"; }
   ```

3. **Safety**
   ```bash
   # Confirm destructive operations
   read -p "Continue? (y/n) " -n 1 -r
   echo
   if [[ ! $REPLY =~ ^[Yy]$ ]]; then
       exit 1
   fi
   ```

4. **Path Handling**
   ```bash
   # Use absolute paths
   SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

   # Quote variables
   cd "$PROJECT_DIR"
   ```

5. **Options Parsing**
   ```bash
   while [[ $# -gt 0 ]]; do
       case $1 in
           --dry-run) DRY_RUN=true; shift ;;
           --help) show_help; exit 0 ;;
           *) echo "Unknown option: $1"; exit 1 ;;
       esac
   done
   ```

## Creating New Scripts

### Template

```bash
#!/bin/bash
set -euo pipefail

# my-script.sh - Description of what this script does
# Usage: ./my-script.sh [options]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Configuration
DRY_RUN=false
VERBOSE=false

# Colors (optional)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Logging
log_info() {
    echo -e "${GREEN}[INFO]${NC} $*"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $*"
}

# Functions
show_help() {
    cat <<EOF
Usage: $0 [OPTIONS]

Description of script purpose.

OPTIONS:
    --dry-run       Show what would happen without making changes
    --verbose       Enable verbose output
    --help          Show this help message

EXAMPLES:
    $0 --dry-run
    $0 --verbose
EOF
}

main() {
    log_info "Starting my-script..."

    # Script logic here

    log_info "Done!"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --verbose)
            VERBOSE=true
            shift
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            show_help
            exit 1
            ;;
    esac
done

# Entry point
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main
fi
```

### Steps to Add

1. Create script file
   ```bash
   cd tooling/scripts
   touch my-script.sh
   chmod +x my-script.sh
   ```

2. Write script following template

3. Test thoroughly
   ```bash
   # Syntax check
   bash -n my-script.sh

   # Dry run
   ./my-script.sh --dry-run

   # Real run (in test environment)
   ./my-script.sh
   ```

4. Document
   - Add to this README
   - Include usage examples
   - Document any caveats

5. Integrate (if needed)
   - Add to bootstrap.sh
   - Add to CI/CD workflows
   - Update root package.json scripts

## Testing Scripts

### Manual Testing

```bash
# Syntax check
bash -n script.sh

# Dry run
./script.sh --dry-run

# Test in clean environment
docker run --rm -it -v $(pwd):/work ubuntu:latest bash
cd /work
./tooling/scripts/bootstrap.sh
```

### Automated Testing

```bash
# Using BATS (Bash Automated Testing System)
npm install -g bats

# Create test file
cat > tests/bootstrap.bats <<'EOF'
#!/usr/bin/env bats

@test "bootstrap script exists" {
    [ -f "tooling/scripts/bootstrap.sh" ]
}

@test "bootstrap has execute permission" {
    [ -x "tooling/scripts/bootstrap.sh" ]
}

@test "bootstrap shows help" {
    run ./tooling/scripts/bootstrap.sh --help
    [ "$status" -eq 0 ]
}
EOF

# Run tests
bats tests/bootstrap.bats
```

## Maintenance

### When to Update Scripts

- Node.js/Python/Rust version changes
- New project categories added
- Workspace configuration changes
- CI/CD pipeline updates
- Security improvements needed

### Version History

Track major changes:
```bash
# Add to script comments
# Version: 1.1.0
# Last Updated: 2025-12-11
# Changes:
#   - Added --dry-run option
#   - Improved error handling
#   - Updated Node.js version check
```

## Troubleshooting

### Common Issues

**Issue:** Script fails with "command not found"
```bash
# Solution: Check PATH and install missing tools
which pnpm || npm install -g pnpm
```

**Issue:** Permission denied
```bash
# Solution: Make script executable
chmod +x tooling/scripts/my-script.sh
```

**Issue:** Script works locally but fails in CI
```bash
# Solution: Check environment differences
# - Different shell (bash vs sh)
# - Missing tools
# - Different paths
# Test in Docker container matching CI environment
```

## Future Scripts

Planned additions:

- [ ] `update-deps.sh` - Update dependencies across projects
- [ ] `cleanup.sh` - Clean build artifacts and caches
- [ ] `release.sh` - Prepare and tag releases
- [ ] `check-health.sh` - Verify monorepo health
- [ ] `generate-docs.sh` - Generate documentation
- [ ] `sync-configs.sh` - Sync shared configurations

## Contributing

When adding scripts:

1. Follow the template structure
2. Add comprehensive help text
3. Include --dry-run option for destructive operations
4. Test on both macOS and Linux
5. Document in this README
6. Consider CI/CD integration

## Related Documentation

- [Tooling README](../README.md)
- [MONOREPO_ARCHITECTURE.md](../../docs/MONOREPO_ARCHITECTURE.md)
- [GitHub Actions Workflows](../../.github/workflows/)

---

**Total Scripts:** 2
**Languages:** Bash
**Tested On:** macOS, Ubuntu Linux
**Maintained By:** UDL Team
