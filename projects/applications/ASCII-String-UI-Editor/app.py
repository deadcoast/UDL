"""Flask backend for ASCII Box Character Editor"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import ast
import json

from utils.presets import PRESETS, format_charset_python, format_charset_javascript
from utils.renderer import generate_all_patterns

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    """Render main application page"""
    return render_template('index.html')


@app.route('/api/presets', methods=['GET'])
def get_presets():
    """Get all available presets"""
    return jsonify({
        'presets': list(PRESETS.keys())
    })


@app.route('/api/preset/<preset_name>', methods=['GET'])
def get_preset(preset_name):
    """Get specific preset character set"""
    if preset_name not in PRESETS:
        return jsonify({'error': 'Preset not found'}), 404

    charset = PRESETS[preset_name]
    return jsonify({
        'charset': charset,
        'formatted': {
            'python': format_charset_python(charset),
            'javascript': format_charset_javascript(charset)
        }
    })


@app.route('/api/render', methods=['POST'])
def render_preview():
    """
    Render box patterns from character set
    Expects JSON: { "charset": {...} }
    Returns: { "patterns": [...], "error": null }
    """
    try:
        data = request.get_json()

        if not data or 'charset' not in data:
            return jsonify({'error': 'Missing charset data'}), 400

        charset = data['charset']

        required_keys = [
            'top_left', 'top_right', 'bottom_left', 'bottom_right',
            'horizontal', 'vertical', 'tjunction_up', 'tjunction_down',
            'tjunction_left', 'tjunction_right', 'cross'
        ]

        missing_keys = [key for key in required_keys if key not in charset]
        if missing_keys:
            return jsonify({
                'error': f'Missing required keys: {", ".join(missing_keys)}'
            }), 400

        patterns = generate_all_patterns(charset)

        return jsonify({
            'patterns': patterns,
            'error': None
        })

    except Exception as e:
        return jsonify({
            'error': f'Rendering error: {str(e)}',
            'patterns': []
        }), 500


@app.route('/api/parse', methods=['POST'])
def parse_charset():
    """
    Parse character set from code string
    Expects JSON: { "code": "..." }
    Returns: { "charset": {...}, "error": null }
    """
    try:
        data = request.get_json()

        if not data or 'code' not in data:
            return jsonify({'error': 'Missing code data'}), 400

        code = data['code'].strip()

        charset = None

        try:
            charset = json.loads(code)
        except:
            pass

        if charset is None:
            try:
                charset = ast.literal_eval(code)
            except:
                pass

        if charset is None:
            return jsonify({
                'error': 'Could not parse character set. Must be valid JSON or Python dict.',
                'charset': None
            }), 400

        if not isinstance(charset, dict):
            return jsonify({
                'error': 'Character set must be an object/dictionary',
                'charset': None
            }), 400

        return jsonify({
            'charset': charset,
            'error': None
        })

    except Exception as e:
        return jsonify({
            'error': f'Parse error: {str(e)}',
            'charset': None
        }), 500


@app.route('/api/export/<format_type>', methods=['POST'])
def export_code(format_type):
    """
    Export character set in specified format
    Expects JSON: { "charset": {...} }
    format_type: 'python' or 'javascript'
    """
    try:
        data = request.get_json()

        if not data or 'charset' not in data:
            return jsonify({'error': 'Missing charset data'}), 400

        charset = data['charset']

        if format_type == 'python':
            code = format_charset_python(charset)
        elif format_type == 'javascript':
            code = format_charset_javascript(charset)
        else:
            return jsonify({'error': 'Invalid format type'}), 400

        return jsonify({
            'code': code,
            'error': None
        })

    except Exception as e:
        return jsonify({
            'error': f'Export error: {str(e)}',
            'code': None
        }), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
