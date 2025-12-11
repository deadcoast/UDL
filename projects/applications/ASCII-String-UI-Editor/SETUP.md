# ASCII Box Character Editor - Setup Guide

## Overview

A professional web-based editor for creating and previewing ASCII box drawing characters with real-time rendering powered by Flask and Monaco Editor.

## Installation

### Method 1: Quick Start (Recommended)

```bash
# 1. Install Python dependencies
pip install Flask==3.0.0 Flask-CORS==4.0.0

# 2. Run the application
python3 app.py

# 3. Open your browser
# Navigate to: http://localhost:5000
```

### Method 2: Using the Run Script

```bash
# Make script executable (first time only)
chmod +x run.sh

# Run the application
./run.sh
```

## System Requirements

- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No additional system dependencies required

## Project Structure

```
ascii-box-editor/
├── app.py                  # Flask backend with 6 API endpoints
├── requirements.txt        # Python dependencies (Flask, Flask-CORS)
├── run.sh                 # Convenience startup script
│
├── utils/                 # Python modules
│   ├── __init__.py
│   ├── presets.py        # 6 character set presets
│   └── renderer.py       # 5 box pattern renderers
│
├── templates/
│   └── index.html        # Main application page
│
└── static/
    ├── css/
    │   └── style.css     # VS Code-inspired dark theme
    └── js/
        └── app.js        # Monaco editor integration
```

## Features Walkthrough

### 1. Built-in Presets (6 Available)

- **SINGLE_LINE**: Classic Unicode box drawing (┌─┐)
- **DOUBLE_LINE**: Heavy double borders (╔═╗)
- **HEAVY_LINE**: Bold thick lines (┏━┓)
- **ROUNDED_LINE**: Rounded corners (╭─╮)
- **MIXED_DOUBLE_SINGLE**: Mixed styles (╒═╕)
- **ASCII_BASIC**: Basic ASCII characters (+--+)

### 2. Live Editor

- Monaco Editor with syntax highlighting
- Accepts both JSON and Python dict format
- Auto-parse on 500ms debounce
- Real-time validation feedback

### 3. Preview Patterns (5 Demos)

Each character set renders 5 patterns:
1. **2×2 Grid** - Demonstrates all junction types
2. **3×3 Grid** - Shows multiple crosses
3. **Simple Frame** - Basic rectangular box
4. **Single Cell** - Minimal example
5. **Wide Header Box** - Header with separator

### 4. Export Options

- **Export Python**: Format as Python dictionary
- **Export JavaScript**: Format as JS object
- **Copy Preview**: Copy all rendered patterns

## API Documentation

### GET `/api/presets`

Get list of available presets.

**Response:**
```json
{
  "presets": ["SINGLE_LINE", "DOUBLE_LINE", ...]
}
```

### GET `/api/preset/<name>`

Get specific preset with formatted code.

**Response:**
```json
{
  "charset": { "top_left": "┌", ... },
  "formatted": {
    "python": "{\n    \"top_left\": \"┌\",\n    ...\n}",
    "javascript": "{\n    \"top_left\": \"┌\",\n    ...\n}"
  }
}
```

### POST `/api/parse`

Parse character set from code string.

**Request:**
```json
{
  "code": "{ \"top_left\": \"┌\", ... }"
}
```

**Response:**
```json
{
  "charset": { "top_left": "┌", ... },
  "error": null
}
```

### POST `/api/render`

Render box patterns from character set.

**Request:**
```json
{
  "charset": { "top_left": "┌", ... }
}
```

**Response:**
```json
{
  "patterns": [
    {
      "title": "2×2 Grid",
      "content": "┌───┬───┐\n│...│...│\n└───┴───┘"
    }
  ],
  "error": null
}
```

### POST `/api/export/<format>`

Export character set as Python or JavaScript.

**Formats:** `python` or `javascript`

**Request:**
```json
{
  "charset": { "top_left": "┌", ... }
}
```

**Response:**
```json
{
  "code": "{\n    \"top_left\": \"┌\",\n    ...\n}",
  "error": null
}
```

## Usage Examples

### Example 1: Load a Preset

1. Open http://localhost:5000
2. Click the "Select Preset..." dropdown
3. Choose "DOUBLE_LINE"
4. See live preview with all patterns

### Example 2: Create Custom Character Set

```javascript
{
    "top_left": "╔",
    "top_right": "╗",
    "bottom_left": "╚",
    "bottom_right": "╝",
    "horizontal": "═",
    "vertical": "║",
    "tjunction_up": "╩",
    "tjunction_down": "╦",
    "tjunction_left": "╣",
    "tjunction_right": "╠",
    "cross": "╬"
}
```

### Example 3: Export to Python

1. Select or create a character set
2. Click "Export Python"
3. Code is automatically copied to clipboard
4. Paste into your Python code

## Production Deployment

### Option 1: Gunicorn (Recommended)

```bash
# Install gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Option 2: Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t ascii-box-editor .
docker run -p 5000:5000 ascii-box-editor
```

### Option 3: systemd Service

Create `/etc/systemd/system/ascii-box-editor.service`:
```ini
[Unit]
Description=ASCII Box Character Editor
After=network.target

[Service]
User=www-data
WorkingDirectory=/path/to/ascii-box-editor
ExecStart=/usr/bin/gunicorn -w 4 -b 127.0.0.1:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable ascii-box-editor
sudo systemctl start ascii-box-editor
```

## Troubleshooting

### Port Already in Use

```bash
# Find process using port 5000
lsof -ti:5000

# Kill the process
kill -9 $(lsof -ti:5000)

# Or use a different port
python3 app.py  # Edit app.py to change port
```

### Monaco Editor Not Loading

- Check internet connection (CDN requirement)
- Open browser console for errors
- Try clearing browser cache

### Import Errors

```bash
# Ensure you're in the project directory
cd /path/to/ascii-box-editor

# Reinstall dependencies
pip install -r requirements.txt
```

### Python Version Issues

```bash
# Check Python version (needs 3.8+)
python3 --version

# Use specific Python version
python3.11 app.py
```

## Development Tips

### Adding New Presets

Edit `utils/presets.py`:
```python
MY_CUSTOM = {
    "top_left": "╭",
    "top_right": "╮",
    # ... add all 11 required keys
}

PRESETS = {
    "MY_CUSTOM": MY_CUSTOM,
    # ... existing presets
}
```

### Creating New Patterns

Edit `utils/renderer.py`:
```python
def render_my_pattern(charset: dict) -> str:
    c = charset
    lines = [
        c['top_left'] + c['horizontal'] * 10 + c['top_right'],
        c['vertical'] + ' My Pattern ' + c['vertical'],
        c['bottom_left'] + c['horizontal'] * 10 + c['bottom_right']
    ]
    return '\n'.join(lines)

# Add to generate_all_patterns()
```

### Customizing Styling

Edit `static/css/style.css` to change:
- Color scheme (`:root` variables)
- Layout (grid sizing)
- Typography (fonts, sizes)

## Browser Compatibility

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | 90+ | ✓ Full |
| Firefox | 88+ | ✓ Full |
| Safari | 14+ | ✓ Full |
| Edge | 90+ | ✓ Full |

## Performance Notes

- Monaco Editor loads from CDN (~2MB)
- Debounced parsing (500ms delay)
- No persistent storage (session-based)
- Handles large character sets efficiently

## License

MIT License - Free to use, modify, and distribute.

## Support

For issues or questions:
1. Check this documentation
2. Review browser console for errors
3. Verify all dependencies are installed
4. Ensure Python 3.8+ is being used
