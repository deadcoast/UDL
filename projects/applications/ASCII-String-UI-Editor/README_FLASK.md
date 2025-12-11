# ASCII Box Character Editor

A web-based editor for creating and previewing ASCII box drawing characters with live rendering.

## Features

- **Live Preview**: Real-time rendering of box patterns as you edit
- **6 Built-in Presets**: Single line, double line, heavy, rounded, mixed, and ASCII basic
- **Monaco Editor**: Professional code editor with syntax highlighting
- **Multiple Patterns**: Demonstrates all junction types across 5 different patterns
- **Export Options**: Copy as Python dict or JavaScript object
- **Dark Theme**: VS Code-inspired interface

## Quick Start

### 1. Install Dependencies

```bash
pip install Flask==3.0.0 Flask-CORS==4.0.0
```

### 2. Run the Server

```bash
python3 app.py
```

Or use the convenience script:

```bash
./run.sh
```

### 3. Open in Browser

Navigate to: `http://localhost:5000`

## Project Structure

```
ascii-box-editor/
├── app.py                      # Flask backend with API endpoints
├── requirements.txt            # Python dependencies
├── utils/
│   ├── __init__.py
│   ├── presets.py             # 6 character set presets
│   └── renderer.py            # Box rendering logic (5 patterns)
├── templates/
│   └── index.html             # Main application page
└── static/
    ├── css/
    │   └── style.css          # Dark theme styling
    └── js/
        └── app.js             # Frontend + Monaco integration
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve main HTML page |
| `/api/presets` | GET | Get list of available presets |
| `/api/preset/<name>` | GET | Get specific preset charset |
| `/api/parse` | POST | Parse charset from code string |
| `/api/render` | POST | Render box patterns from charset |
| `/api/export/<format>` | POST | Export as Python/JavaScript |

## Usage

1. **Select a Preset**: Choose from 6 built-in character sets
2. **Edit Character Set**: Modify the JSON/dict in the Monaco editor
3. **Live Preview**: See 5 different box patterns update in real-time
4. **Export**: Copy formatted code for Python or JavaScript
5. **Copy Preview**: Copy rendered ASCII art to clipboard

## Character Set Format

```javascript
{
    "top_left": "┌",
    "top_right": "┐",
    "bottom_left": "└",
    "bottom_right": "┘",
    "horizontal": "─",
    "vertical": "│",
    "tjunction_up": "┴",
    "tjunction_down": "┬",
    "tjunction_left": "┤",
    "tjunction_right": "├",
    "cross": "┼"
}
```

## Pattern Demos

The editor renders 5 patterns demonstrating:
- 2×2 Grid with all junctions
- 3×3 Grid with multiple crosses
- Simple rectangular frame
- Single cell box
- Wide box with header separator

## Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Tech Stack

- **Backend**: Flask 3.0 + Flask-CORS
- **Frontend**: Vanilla JavaScript + Monaco Editor 0.44
- **Styling**: Custom CSS (VS Code dark theme)
- **Character Sets**: Unicode box-drawing characters

## License

MIT
