#!/bin/bash
# UDL Monorepo - Project Migration Script
# Moves existing projects into the new categorized structure

set -e

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}📦 UDL Project Migration${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Create target directories if they don't exist
echo -e "${BLUE}📁 Creating target directories...${NC}"
for category in languages tools extensions applications libraries experimental; do
    mkdir -p "projects/$category"
    echo -e "  ${GREEN}✓${NC} projects/$category"
done
echo ""

# Counters
MOVED=0
SKIPPED=0
FAILED=0

# Function to move a project
move_project() {
    local source="$1"
    local category="$2"
    local target="projects/$category/$source"

    echo -e "${BLUE}Moving:${NC} $source → $category/"

    if [ ! -d "$source" ]; then
        echo -e "  ${RED}✗${NC} Source directory not found"
        ((FAILED++))
        return 1
    fi

    if [ -d "$target" ]; then
        echo -e "  ${YELLOW}⚠${NC}  Target already exists, skipping"
        ((SKIPPED++))
        return 0
    fi

    # Move the project
    mv "$source" "$target"

    # Check if move was successful
    if [ -d "$target" ]; then
        echo -e "  ${GREEN}✓${NC} Moved successfully"
        ((MOVED++))

        # If it has a .git directory, note it
        if [ -d "$target/.git" ]; then
            echo -e "  ${BLUE}ℹ${NC}  Git history preserved"
        fi
    else
        echo -e "  ${RED}✗${NC} Move failed"
        ((FAILED++))
        return 1
    fi
}

# Language projects
move_project "axe-Syntax" "languages"
move_project "1az" "languages"
move_project "gate" "languages"
move_project "gateppattern-1.1" "languages"
move_project "f8Syntax" "languages"
move_project "DrRx" "languages"
move_project "remedysyntax" "languages"
move_project "hoc" "languages"

# Tool projects
move_project "CTX" "tools"
move_project "ctx-card" "tools"
move_project "sandbag" "tools"
move_project "axe" "tools"
move_project "axe_syntax" "tools"
move_project "JETSON" "tools"
move_project "BARRELMAN" "tools"
move_project "robo_md" "tools"
move_project "FINK" "tools"

# Extension projects
move_project "camo-obsidian" "extensions"

# Application projects
move_project "black-milk" "applications"
move_project "StrawberryMause" "applications"
move_project "ASCII-String-UI-Editor" "applications"

# Library projects
move_project "hunt_ascii" "libraries"
move_project "ASCII-hunt" "libraries"
move_project "milkDocs" "libraries"

# Experimental projects
move_project "mecha_lang" "experimental"
move_project "mecha_development" "experimental"
move_project "motleyBard" "experimental"
move_project "canon" "experimental"
move_project "CLAY" "experimental"
move_project "PACER" "experimental"
move_project "udl-directory-template" "experimental"

# Move .depreciated to .archive if it exists
if [ -d ".depreciated" ]; then
    echo -e "\n${BLUE}Moving:${NC} .depreciated → .archive/"
    mv .depreciated .archive/depreciated 2>/dev/null || echo -e "  ${YELLOW}⚠${NC}  Already moved"
    echo -e "  ${GREEN}✓${NC} Archived deprecated projects"
fi

# Also move 4Di and JEFRY if they exist
if [ -d "4Di" ]; then
    move_project "4Di" "experimental"
fi
if [ -d "JEFRY" ]; then
    move_project "JEFRY" "experimental"
fi

# Summary
echo -e "\n${BLUE}========================================${NC}"
echo -e "${BLUE}Migration Summary:${NC}"
echo -e "${GREEN}✓${NC} Moved: $MOVED projects"
echo -e "${YELLOW}⚠${NC}  Skipped: $SKIPPED projects"
echo -e "${RED}✗${NC} Failed: $FAILED projects"
echo -e "${BLUE}========================================${NC}\n"

# List final structure
echo -e "${BLUE}📊 New Structure:${NC}\n"
for category in languages tools extensions applications libraries experimental; do
    count=$(ls -1 "projects/$category" 2>/dev/null | wc -l | tr -d ' ')
    if [ "$count" -gt 0 ]; then
        echo -e "  ${BLUE}projects/$category/${NC} ($count projects)"
        ls -1 "projects/$category" 2>/dev/null | sed 's/^/    /'
        echo ""
    fi
done

echo -e "${GREEN}✅ Migration Complete!${NC}\n"
echo -e "Next steps:"
echo -e "  ${BLUE}•${NC} Review the new structure"
echo -e "  ${BLUE}•${NC} Create project.json for each project"
echo -e "  ${BLUE}•${NC} Update inter-project dependencies"
echo -e "  ${BLUE}•${NC} Test builds: ${GREEN}pnpm build${NC}\n"
