#!/usr/bin/env python3
"""
Demo script to showcase all available character set presets
Run this to see what each preset looks like
"""

from utils.presets import PRESETS
from utils.renderer import generate_all_patterns


def demo_all_presets():
    """Display all presets with their rendered patterns"""

    print("=" * 80)
    print("ASCII Box Character Editor - Preset Showcase")
    print("=" * 80)
    print()

    for preset_name, charset in PRESETS.items():
        print(f"\n{'=' * 80}")
        print(f"PRESET: {preset_name}")
        print(f"{'=' * 80}\n")

        print("Character Set:")
        for key, value in charset.items():
            print(f"  {key:20} : '{value}'")

        print("\nRendered Patterns:")
        print("-" * 80)

        patterns = generate_all_patterns(charset)

        for i, pattern in enumerate(patterns, 1):
            print(f"\n{i}. {pattern['title']}")
            print(pattern["content"])

        print()


def demo_single_preset(preset_name):
    """Display a single preset"""

    if preset_name not in PRESETS:
        print(f"Error: Preset '{preset_name}' not found.")
        print(f"Available presets: {', '.join(PRESETS.keys())}")
        return

    charset = PRESETS[preset_name]

    print(f"\n{'=' * 80}")
    print(f"PRESET: {preset_name}")
    print(f"{'=' * 80}\n")

    patterns = generate_all_patterns(charset)

    for pattern in patterns:
        print(f"{pattern['title']}:")
        print(pattern["content"])
        print()


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        preset_name = sys.argv[1].upper()
        demo_single_preset(preset_name)
    else:
        demo_all_presets()
