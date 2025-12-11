# Repository Guidelines

Monorepo for DSLs, tools, extensions, apps.

## Project Structure & Module Organization
- Root configs: `package.json`, `turbo.json`, `pyproject.toml`, `Cargo.toml`.
- `projects/` by domain: `languages/`, `tools/`, `extensions/`, `applications/`, `libraries/`, `experimental/`.
- `shared/` packages/configs; `tooling/` bootstrap/dev scripts + `udl` CLI; `docs/`, `examples/` for reference.
- Add work in the right domain; edit manifests only when needed.

## Build, Test, and Development Commands
- Bootstrap: `./tooling/scripts/bootstrap.sh` (Node 18+/pnpm 8+, Python 3.8+, Rust).
- Build/dev: `pnpm build` or `turbo run build --filter=<project>`; `pnpm dev`/`turbo run dev --filter=<project>`.
- Test: `pnpm test`; scope with `turbo run test --filter=<project>`.
- Hygiene: `pnpm lint format typecheck clean`.
- Scaffolding: `pnpm udl create --name my-tool --type tool --lang typescript` (CLI at `tooling/dev-tools/cli.js`).

## Coding Style & Naming Conventions
- TypeScript/JS: Prettier + ESLint/TypeScript-ESLint; packages `@udl/*`; folders `projects/<domain>/<kebab-name>`.
- Python: Black 88, isort (Black profile), Ruff, pytest in `pyproject.toml`.
- Rust: `cargo fmt` + `cargo clippy`; members under `projects/tools/`, registered in `Cargo.toml`.
- Docs: Markdownlint enabled; concise headings, relative links.

## Testing Guidelines
- Main: `pnpm test`; scope with `turbo run test --filter=<project>`.
- TS: `npm/pnpm test`; Python: `pytest` (`tests/`, `test_*.py`/`*_test.py`, markers `slow|integration|unit`); Rust: `cargo test`.
- Keep tests deterministic; check in fixtures per project.

## Project Quicklinks & Exceptions
- Apps: `projects/applications/black-milk/README.md` (Godot 4), `projects/applications/ASCII-String-UI-Editor/README.md` (Vite/TS+Python), `projects/applications/StrawberryMause/README.md` (TS/Vitest).
- Extensions: `projects/extensions/camo-obsidian/README.md`, `projects/languages/1az/README.md` — `pnpm dev`; package with `vsce package`/`npm publish`.
- DSLs: `projects/languages/gate/README.md`, `projects/languages/gateppattern-1.1/README.md`, `projects/languages/f8Syntax/README.md`, `projects/languages/axe-Syntax/README.md`, `projects/languages/remedysyntax/README.md`, `projects/languages/DrRx/README.md`, `projects/languages/hoc/README.md` — `pnpm dev --filter=<dsl>`.
- Tools (TS/JS): `projects/tools/axe/README.md`, `projects/tools/axe_syntax/README.md`, `projects/tools/BARRELMAN/README.md`, `projects/tools/CTX/README.md`, `projects/tools/ctx-card/README.md`, `projects/tools/FINK/README.md`, `projects/tools/JETSON/README.md`, `projects/tools/robo_md/README.md` — `pnpm dev/test`.
- Rust: `projects/tools/sandbag/README.md` — `cargo fmt && cargo clippy && cargo test`; root Cargo workspace.
- Libraries: `projects/libraries/milkDocs/README.md`, `projects/libraries/ASCII-hunt/README.md`, `projects/libraries/hunt_ascii/README.md` — Python libs; `pytest` + Black/isort/Ruff.
- Experimental (`projects/experimental/README.md`): `4Di` (pnpm install && pnpm build); `canon`, `CLAY`, `JEFRY`, `mecha_lang` (see README, usually pnpm dev/build); `mecha_development` (pnpm install + README steps); `motleyBard` (python -m venv .venv && pip install -r requirements.txt && pytest); `PACER` (pip install -r requirements.txt && pytest); `udl-directory-template` (copy as starter).

## Commit & Pull Request Guidelines
- Use Conventional Commits as in history (`feat:`, `fix:`, `docs:`, `chore:`); add scope when helpful (`feat(gate): add parser hook`).
- Before a PR: run `pnpm lint` and `pnpm test`, plus language-specific checks (`cargo fmt && cargo test` for Rust, `pytest` for Python).
- PRs should include a short summary, linked issue/reference, test results, and screenshots/recordings for UI-visible changes.
- Keep scopes narrow and call out cross-project impacts explicitly.
