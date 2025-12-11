#!/usr/bin/env python3
"""
Simple test suite for ASCII Box Character Editor
Run this to verify everything is working correctly
"""

import json

from utils.presets import PRESETS, format_charset_javascript, format_charset_python
from utils.renderer import generate_all_patterns


def test_presets():
    """Test that all presets are valid"""
    print("Testing presets...")

    required_keys = [
        "top_left",
        "top_right",
        "bottom_left",
        "bottom_right",
        "horizontal",
        "vertical",
        "tjunction_up",
        "tjunction_down",
        "tjunction_left",
        "tjunction_right",
        "cross",
    ]

    for name, charset in PRESETS.items():
        for key in required_keys:
            assert key in charset, f"Preset {name} missing key: {key}"
            assert isinstance(charset[key], str), (
                f"Preset {name} key {key} must be string"
            )
            assert len(
                charset[key]) > 0, f"Preset {name} key {key} cannot be empty"

    print(f"  ✓ All {len(PRESETS)} presets are valid")
    return True


def test_renderers():
    """Test that all renderers work"""
    print("Testing renderers...")

    for name, charset in PRESETS.items():
        patterns = generate_all_patterns(charset)

        assert len(patterns) == 5, (
            f"Expected 5 patterns for {name}, got {len(patterns)}"
        )

        for pattern in patterns:
            assert "title" in pattern, "Pattern missing title"
            assert "content" in pattern, "Pattern missing content"
            assert isinstance(pattern["content"],
                              str), "Pattern content must be string"
            assert len(pattern["content"]
                       ) > 0, "Pattern content cannot be empty"

    print(f"  ✓ All patterns render correctly for all presets")
    return True


def test_formatters():
    """Test charset formatters"""
    print("Testing formatters...")

    charset = PRESETS["SINGLE_LINE"]

    python_code = format_charset_python(charset)
    assert "{" in python_code, "Python format missing opening brace"
    assert "}" in python_code, "Python format missing closing brace"
    assert "top_left" in python_code, "Python format missing keys"

    js_code = format_charset_javascript(charset)
    assert "{" in js_code, "JavaScript format missing opening brace"
    assert "}" in js_code, "JavaScript format missing closing brace"
    assert "top_left" in js_code, "JavaScript format missing keys"

    print("  ✓ Formatters work correctly")
    return True


def test_pattern_structure():
    """Test that patterns have correct structure"""
    print("Testing pattern structure...")

    charset = PRESETS["SINGLE_LINE"]
    patterns = generate_all_patterns(charset)

    for pattern in patterns:
        lines = pattern["content"].split("\n")

        assert len(lines) >= 3, "Pattern should have at least 3 lines"

        for char_key in ["top_left", "top_right", "horizontal", "vertical"]:
            char = charset[char_key]
            found = any(char in line for line in lines)
            assert found, f"Character {char_key} ('{char}') not found in pattern"

    print("  ✓ Pattern structures are correct")
    return True


def test_unicode_characters():
    """Test that Unicode characters render correctly"""
    print("Testing Unicode characters...")

    unicode_presets = ["SINGLE_LINE",
                       "DOUBLE_LINE", "HEAVY_LINE", "ROUNDED_LINE"]

    for name in unicode_presets:
        charset = PRESETS[name]
        patterns = generate_all_patterns(charset)

        for pattern in patterns:
            content = pattern["content"]

            try:
                content.encode("utf-8")
            except UnicodeEncodeError:
                assert False, f"Preset {name} contains invalid Unicode"

    print("  ✓ Unicode characters are valid")
    return True


def test_ascii_basic():
    """Test ASCII_BASIC preset for compatibility"""
    print("Testing ASCII_BASIC preset...")

    charset = PRESETS["ASCII_BASIC"]
    patterns = generate_all_patterns(charset)

    for pattern in patterns:
        content = pattern["content"]

        try:
            content.encode("ascii")
        except UnicodeEncodeError:
            assert False, "ASCII_BASIC contains non-ASCII characters"

    print("  ✓ ASCII_BASIC is pure ASCII")
    return True


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("ASCII Box Character Editor - Test Suite")
    print("=" * 80 + "\n")

    tests = [
        test_presets,
        test_renderers,
        test_formatters,
        test_pattern_structure,
        test_unicode_characters,
        test_ascii_basic,
    ]

    passed = 0
    failed = 0

    for test_func in tests:
        try:
            if test_func():
                passed += 1
        except AssertionError as e:
            print(f"  ✗ Test failed: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
            failed += 1

    print("\n" + "=" * 80)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 80 + "\n")

    if failed == 0:
        print("✓ All tests passed! The application is ready to use.")
        print("\nTo start the server, run:")
        print("  python3 app.py")
        print("\nThen open your browser to:")
        print("  http://localhost:5000")
        return True
    else:
        print("✗ Some tests failed. Please check the output above.")
        return False


if __name__ == "__main__":
    import sys

    success = run_all_tests()
    sys.exit(0 if success else 1)
