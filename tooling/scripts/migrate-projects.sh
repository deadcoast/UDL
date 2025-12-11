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

# Define project categorization
# Format: "source_dir:target_category"

declare -A PROJECT_MAP=(
    # Languages
    ["axe-Syntax"]="languages"
    ["1az"]="languages"
    ["gate"]="languages"
    ["gateppattern-1.1"]="languages"
    ["f8Syntax"]="languages"
    ["DrRx"]="languages"
    ["remedysyntax"]="languages"
    ["hoc"]="languages"

    # Tools
    ["CTX"]="tools"
    ["ctx-card"]="tools"
    ["sandbag"]="tools"
    ["axe"]="tools"
    ["axe_syntax"]="tools"
    ["JETSON"]="tools"
    ["BARRELMAN"]="tools"
    ["robo_md"]="tools"
    ["FINK"]="tools"

    # Extensions
    ["camo-obsidian"]="extensions"

    # Applications
    ["black-milk"]="applications"
    ["StrawberryMause"]="applications"
    ["ASCII-String-UI-Editor"]="applications"

    # Libraries
    ["hunt_ascii"]="libraries"
    ["ASCII-hunt"]="libraries"
    ["milkDocs"]="libraries"

    # Experimental
    ["mecha_lang"]="experimental"
    ["mecha_development"]="experimental"
    ["motleyBard"]="experimental"
    ["canon"]="experimental"
    ["CLAY"]="experimental"
    ["PACER"]="experimental"
    ["udl-directory-template"]="experimental"
)

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
    local source=$1
    local category=$2
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

# Migrate all projects
for project in "${!PROJECT_MAP[@]}"; do
    category="${PROJECT_MAP[$project]}"
    move_project "$project" "$category"
    echo ""
done

# Move .depreciated to .archive if it exists
if [ -d ".depreciated" ]; then
    echo -e "${BLUE}Moving:${NC} .depreciated → .archive/"
    mv .depreciated .archive/depreciated
    echo -e "  ${GREEN}✓${NC} Archived deprecated projects\n"
fi

# Summary
echo -e "${BLUE}========================================${NC}"
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
