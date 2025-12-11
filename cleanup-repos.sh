#!/bin/bash
# UDL Monorepo - Phase 0: Cleanup Script
# Commits and pushes all changes across all repositories

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}UDL Monorepo Preparation - Phase 0${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Repositories with uncommitted changes
REPOS_WITH_CHANGES=(
    "axe_syntax"
    "black-milk"
    "camo-obsidian"
    "canon"
    "CLAY"
    "ctx-card"
    "DrRx"
    "FINK"
    "gate"
    "hoc"
    "mecha_development"
    "milkDocs"
    "motleyBard"
    "PACER"
    "remedysyntax"
    "robo_md"
)

# Counter
COMMITTED=0
PUSHED=0
SKIPPED=0

# Function to add global .DS_Store ignore
add_global_gitignore() {
    local repo=$1
    if [ -f "$repo/.gitignore" ]; then
        if ! grep -q "\.DS_Store" "$repo/.gitignore"; then
            echo ".DS_Store" >> "$repo/.gitignore"
            echo -e "  ${GREEN}✓${NC} Added .DS_Store to .gitignore"
        fi
    else
        echo ".DS_Store" > "$repo/.gitignore"
        echo -e "  ${GREEN}✓${NC} Created .gitignore with .DS_Store"
    fi
}

# Process each repository
for repo in "${REPOS_WITH_CHANGES[@]}"; do
    if [ ! -d "$repo" ]; then
        echo -e "${YELLOW}⚠${NC}  Directory $repo not found, skipping..."
        ((SKIPPED++))
        continue
    fi

    echo -e "\n${BLUE}Processing:${NC} $repo"
    cd "$repo"

    # Check if it's a git repo
    if [ ! -d ".git" ]; then
        echo -e "  ${RED}✗${NC} Not a git repository"
        cd ..
        ((SKIPPED++))
        continue
    fi

    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        echo -e "  ${GREEN}✓${NC} No changes to commit"
        cd ..
        continue
    fi

    # Add .DS_Store to .gitignore if not already there
    add_global_gitignore "."

    # Remove .DS_Store files from tracking
    git rm --cached .DS_Store 2>/dev/null || true
    git rm --cached **/.DS_Store 2>/dev/null || true
    find . -name .DS_Store -delete 2>/dev/null || true

    # Show what's changed
    echo -e "  ${YELLOW}Changes:${NC}"
    git status --short | head -10

    # Stage all changes
    git add -A

    # Commit
    COMMIT_MSG="chore: pre-monorepo cleanup - prepare for migration"
    git commit -m "$COMMIT_MSG" 2>/dev/null || {
        echo -e "  ${YELLOW}⚠${NC}  Nothing to commit (changes were .DS_Store only)"
        cd ..
        continue
    }

    echo -e "  ${GREEN}✓${NC} Committed changes"
    ((COMMITTED++))

    # Push
    if git push 2>/dev/null; then
        echo -e "  ${GREEN}✓${NC} Pushed to remote"
        ((PUSHED++))
    else
        echo -e "  ${RED}✗${NC} Failed to push (may need authentication or remote not set)"
    fi

    cd ..
done

# Summary
echo -e "\n${BLUE}========================================${NC}"
echo -e "${BLUE}Summary:${NC}"
echo -e "${GREEN}✓${NC} Committed: $COMMITTED repositories"
echo -e "${GREEN}✓${NC} Pushed: $PUSHED repositories"
echo -e "${YELLOW}⚠${NC}  Skipped: $SKIPPED repositories"
echo -e "${BLUE}========================================${NC}\n"

echo -e "${GREEN}Phase 0.1 Complete!${NC} All changes committed and pushed.\n"
