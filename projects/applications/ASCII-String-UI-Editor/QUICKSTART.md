# ASCII Box Character Editor - Quick Start Guide

## What You've Got

A complete Flask web application for editing and previewing ASCII box drawing characters with:

- 6 built-in character presets
- Live Monaco code editor
- Real-time pattern rendering
- Python & JavaScript export
- Professional dark theme UI

## 30-Second Setup

```bash
# Install dependencies (Flask is probably not installed yet)
pip install Flask==3.0.0 Flask-CORS==4.0.0

# Run the app
python3 app.py
```

Open: **http://localhost:5000**

## What Each File Does

### Core Application

- **app.py** - Flask server with 6 API endpoints
- **requirements.txt** - Python dependencies

### Backend Logic

- **utils/presets.py** - 6 character set definitions
- **utils/renderer.py** - 5 pattern rendering functions

### Frontend

- **templates/index.html** - Main web page
- **static/css/style.css** - Dark theme styling
- **static/js/app.js** - Monaco editor + API integration

### Helper Scripts

- **run.sh** - Convenience launcher
- **test_app.py** - Test suite (verify everything works)
- **demo_presets.py** - CLI demo of all presets

## Try It Out

### Run the Test Suite

```bash
python3 test_app.py
```

### Demo All Presets in Terminal

```bash
python3 demo_presets.py
```

### Demo a Specific Preset

```bash
python3 demo_presets.py DOUBLE_LINE
python3 demo_presets.py ROUNDED_LINE
python3 demo_presets.py ASCII_BASIC
```

## Using the Web Interface

### 1. Select a Preset

- Click the "Select Preset..." dropdown
- Choose any of the 6 presets
- Editor populates with the character set
- Preview updates automatically

### 2. Edit Characters

- Modify any character in the JSON
- Changes appear in preview after 500ms
- Status indicator shows parse state (green = valid)

### 3. Export Code

- **Export Python** - Copy as Python dict
- **Export JavaScript** - Copy as JS object
- **Copy Preview** - Copy all rendered patterns

## Available Presets

| Preset              | Example | Style                          |
| ------------------- | ------- | ------------------------------ |
| SINGLE_LINE         | ┌─┐     | Classic Unicode thin lines     |
| DOUBLE_LINE         | ╔═╗     | Heavy double borders           |
| HEAVY_LINE          | ┏━┓     | Bold thick lines               |
| ROUNDED_LINE        | ╭─╮     | Rounded corners                |
| MIXED_DOUBLE_SINGLE | ╒═╕     | Mixed styles                   |
| ASCII_BASIC         | +-+     | Pure ASCII (max compatibility) |

## 5 Preview Patterns

Each charset renders these patterns:

1. **2×2 Grid** - Full junction demo
2. **3×3 Grid** - Multiple crosses
3. **Simple Frame** - Basic box
4. **Single Cell** - Minimal example
5. **Wide Header Box** - Header with divider

## API Endpoints

All APIs are REST-based JSON:

```bash
# Get all preset names
curl http://localhost:5000/api/presets

# Get specific preset
curl http://localhost:5000/api/preset/DOUBLE_LINE

# Parse custom charset
curl -X POST http://localhost:5000/api/parse \
  -H "Content-Type: application/json" \
  -d '{"code": "{\"top_left\": \"┌\"}"}'

# Render patterns
curl -X POST http://localhost:5000/api/render \
  -H "Content-Type: application/json" \
  -d '{"charset": {...}}'

# Export as Python
curl -X POST http://localhost:5000/api/export/python \
  -H "Content-Type: application/json" \
  -d '{"charset": {...}}'
```

## Character Set Format

All 11 keys are required:

```javascript
{
    "top_left": "┌",       // ┌ corner
    "top_right": "┐",      // ┐ corner
    "bottom_left": "└",    // └ corner
    "bottom_right": "┘",   // ┘ corner
    "horizontal": "─",     // ─ line
    "vertical": "│",       // │ line
    "tjunction_up": "┴",   // ┴ T pointing up
    "tjunction_down": "┬", // ┬ T pointing down
    "tjunction_left": "┤", // ┤ T pointing left
    "tjunction_right": "├",// ├ T pointing right
    "cross": "┼"          // ┼ cross junction
}
```

## Example Output

### SINGLE_LINE Preset

```
┌─────────┬─────────┐
│ Header  │ Header  │
├─────────┼─────────┤
│ Data    │ Data    │
└─────────┴─────────┘
```

### DOUBLE_LINE Preset

```
╔═════════╦═════════╗
║ Header  ║ Header  ║
╠═════════╬═════════╣
║ Data    ║ Data    ║
╚═════════╩═════════╝
```

### ASCII_BASIC Preset

```
+---------+---------+
| Header  | Header  |
+---------+---------+
| Data    | Data    |
+---------+---------+
```

## Troubleshooting

### "Port 5000 already in use"

```bash
# Kill the process
kill -9 $(lsof -ti:5000)

# Or edit app.py to use different port
```

### "No module named 'flask'"

```bash
# Install Flask
pip install Flask==3.0.0 Flask-CORS==4.0.0
```

### Monaco Editor not loading

- Check internet connection (uses CDN)
- Try different browser
- Check browser console for errors

## Next Steps

### Production Deployment

```bash
# Install gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Add Custom Presets

Edit `utils/presets.py` and add to `PRESETS` dict.

### Create New Patterns

Edit `utils/renderer.py` and add to `generate_all_patterns()`.

### Customize Theme

Edit `static/css/style.css` `:root` variables.

## Documentation

- **SETUP.md** - Comprehensive setup guide
- **README_FLASK.md** - Complete project documentation
- This file - Quick start guide

## Support

Run tests to verify everything:

```bash
python3 test_app.py
```

All 6 tests should pass. If any fail, check the error messages.

---

**Ready to go!** Just run `python3 app.py` and open http://localhost:5000
