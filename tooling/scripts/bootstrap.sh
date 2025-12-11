#!/bin/bash
# UDL Monorepo Bootstrap Script
# Sets up development environment for all languages and tools

set -e

BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🚀 UDL Monorepo Bootstrap${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Check prerequisites
echo -e "${BLUE}📋 Checking prerequisites...${NC}"

# Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    echo -e "  ${GREEN}✓${NC} Node.js ${NODE_VERSION}"
else
    echo -e "  ${RED}✗${NC} Node.js not found. Please install Node.js >= 18.0.0"
    echo -e "    Visit: https://nodejs.org/"
    exit 1
fi

# PNPM
if command -v pnpm &> /dev/null; then
    PNPM_VERSION=$(pnpm --version)
    echo -e "  ${GREEN}✓${NC} PNPM ${PNPM_VERSION}"
else
    echo -e "  ${YELLOW}⚠${NC}  PNPM not found. Installing..."
    npm install -g pnpm
    echo -e "  ${GREEN}✓${NC} PNPM installed"
fi

# Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "  ${GREEN}✓${NC} ${PYTHON_VERSION}"
else
    echo -e "  ${RED}✗${NC} Python 3 not found. Please install Python >= 3.8"
    echo -e "    Visit: https://www.python.org/"
    exit 1
fi

# Rust (optional)
if command -v cargo &> /dev/null; then
    CARGO_VERSION=$(cargo --version)
    echo -e "  ${GREEN}✓${NC} ${CARGO_VERSION}"
else
    echo -e "  ${YELLOW}⚠${NC}  Rust not found (optional for Rust projects)"
    echo -e "    Install: curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
fi

# Git
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    echo -e "  ${GREEN}✓${NC} ${GIT_VERSION}"
else
    echo -e "  ${RED}✗${NC} Git not found. Please install Git"
    exit 1
fi

echo ""

# Install Node.js dependencies
echo -e "${BLUE}📦 Installing Node.js dependencies...${NC}"
pnpm install
echo -e "  ${GREEN}✓${NC} Node.js dependencies installed\n"

# Install Python dependencies (if any projects have them)
echo -e "${BLUE}🐍 Setting up Python environments...${NC}"
if [ -f "requirements.txt" ]; then
    python3 -m pip install -r requirements.txt
    echo -e "  ${GREEN}✓${NC} Python dependencies installed"
else
    echo -e "  ${YELLOW}⚠${NC}  No root requirements.txt found (per-project setup)"
fi
echo ""

# Build Rust projects (if any)
if command -v cargo &> /dev/null && [ -f "Cargo.toml" ]; then
    echo -e "${BLUE}🦀 Building Rust workspace...${NC}"
    cargo build
    echo -e "  ${GREEN}✓${NC} Rust workspace built\n"
fi

# Set up git hooks (if we have them)
if [ -d ".husky" ]; then
    echo -e "${BLUE}🪝 Setting up git hooks...${NC}"
    pnpm exec husky install
    echo -e "  ${GREEN}✓${NC} Git hooks installed\n"
fi

# Create .env template if it doesn't exist
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    cp .env.example .env
    echo -e "${BLUE}📝 Created .env from template${NC}\n"
fi

# Summary
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ Bootstrap Complete!${NC}"
echo -e "${BLUE}========================================${NC}\n"

echo -e "Next steps:"
echo -e "  ${BLUE}•${NC} Build all projects:  ${GREEN}pnpm build${NC}"
echo -e "  ${BLUE}•${NC} Run tests:          ${GREEN}pnpm test${NC}"
echo -e "  ${BLUE}•${NC} Start development:  ${GREEN}pnpm dev${NC}"
echo -e "  ${BLUE}•${NC} View docs:          ${GREEN}open docs/README.md${NC}\n"

echo -e "${BLUE}For project-specific commands, navigate to the project directory.${NC}"
echo -e "${BLUE}Happy coding! 🚀${NC}\n"
