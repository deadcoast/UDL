let editor;
let currentCharset = null;
let debounceTimer;
let allCharacters = [];

const CHARACTER_CATEGORIES = {
    corners: {
        name: 'Corners',
        chars: [
            { symbol: '┌', label: 'Light Down Right', code: '\\u250C' },
            { symbol: '┐', label: 'Light Down Left', code: '\\u2510' },
            { symbol: '└', label: 'Light Up Right', code: '\\u2514' },
            { symbol: '┘', label: 'Light Up Left', code: '\\u2518' },
            { symbol: '╔', label: 'Double Down Right', code: '\\u2554' },
            { symbol: '╗', label: 'Double Down Left', code: '\\u2557' },
            { symbol: '╚', label: 'Double Up Right', code: '\\u255A' },
            { symbol: '╝', label: 'Double Up Left', code: '\\u255D' },
            { symbol: '┏', label: 'Heavy Down Right', code: '\\u250F' },
            { symbol: '┓', label: 'Heavy Down Left', code: '\\u2513' },
            { symbol: '┗', label: 'Heavy Up Right', code: '\\u2517' },
            { symbol: '┛', label: 'Heavy Up Left', code: '\\u251B' },
            { symbol: '╭', label: 'Rounded Down Right', code: '\\u256D' },
            { symbol: '╮', label: 'Rounded Down Left', code: '\\u256E' },
            { symbol: '╰', label: 'Rounded Up Right', code: '\\u2570' },
            { symbol: '╯', label: 'Rounded Up Left', code: '\\u256F' }
        ]
    },
    lines: {
        name: 'Lines',
        chars: [
            { symbol: '─', label: 'Light Horizontal', code: '\\u2500' },
            { symbol: '│', label: 'Light Vertical', code: '\\u2502' },
            { symbol: '═', label: 'Double Horizontal', code: '\\u2550' },
            { symbol: '║', label: 'Double Vertical', code: '\\u2551' },
            { symbol: '━', label: 'Heavy Horizontal', code: '\\u2501' },
            { symbol: '┃', label: 'Heavy Vertical', code: '\\u2503' },
            { symbol: '╌', label: 'Light Dashed', code: '\\u254C' },
            { symbol: '╎', label: 'Light Dashed Vert', code: '\\u254E' },
            { symbol: '╍', label: 'Heavy Dashed', code: '\\u254D' },
            { symbol: '╏', label: 'Heavy Dashed Vert', code: '\\u254F' }
        ]
    },
    junctions: {
        name: 'T-Junctions',
        chars: [
            { symbol: '├', label: 'Light Vert Right', code: '\\u251C' },
            { symbol: '┤', label: 'Light Vert Left', code: '\\u2524' },
            { symbol: '┬', label: 'Light Down Horiz', code: '\\u252C' },
            { symbol: '┴', label: 'Light Up Horiz', code: '\\u2534' },
            { symbol: '╠', label: 'Double Vert Right', code: '\\u2560' },
            { symbol: '╣', label: 'Double Vert Left', code: '\\u2563' },
            { symbol: '╦', label: 'Double Down Horiz', code: '\\u2566' },
            { symbol: '╩', label: 'Double Up Horiz', code: '\\u2569' },
            { symbol: '┣', label: 'Heavy Vert Right', code: '\\u2523' },
            { symbol: '┫', label: 'Heavy Vert Left', code: '\\u252B' },
            { symbol: '┳', label: 'Heavy Down Horiz', code: '\\u2533' },
            { symbol: '┻', label: 'Heavy Up Horiz', code: '\\u253B' }
        ]
    },
    crosses: {
        name: 'Crosses',
        chars: [
            { symbol: '┼', label: 'Light Cross', code: '\\u253C' },
            { symbol: '╬', label: 'Double Cross', code: '\\u256C' },
            { symbol: '╋', label: 'Heavy Cross', code: '\\u254B' },
            { symbol: '╪', label: 'Mixed Cross', code: '\\u256A' },
            { symbol: '╫', label: 'Mixed Cross 2', code: '\\u256B' },
            { symbol: '┿', label: 'Light Vert Heavy H', code: '\\u253F' },
            { symbol: '╂', label: 'Heavy Vert Light H', code: '\\u2542' }
        ]
    },
    double: {
        name: 'Double Lines',
        chars: [
            { symbol: '╔', label: 'Down Right', code: '\\u2554' },
            { symbol: '╗', label: 'Down Left', code: '\\u2557' },
            { symbol: '╚', label: 'Up Right', code: '\\u255A' },
            { symbol: '╝', label: 'Up Left', code: '\\u255D' },
            { symbol: '═', label: 'Horizontal', code: '\\u2550' },
            { symbol: '║', label: 'Vertical', code: '\\u2551' },
            { symbol: '╠', label: 'Vert Right', code: '\\u2560' },
            { symbol: '╣', label: 'Vert Left', code: '\\u2563' },
            { symbol: '╦', label: 'Down Horiz', code: '\\u2566' },
            { symbol: '╩', label: 'Up Horiz', code: '\\u2569' },
            { symbol: '╬', label: 'Cross', code: '\\u256C' }
        ]
    },
    heavy: {
        name: 'Heavy Lines',
        chars: [
            { symbol: '┏', label: 'Down Right', code: '\\u250F' },
            { symbol: '┓', label: 'Down Left', code: '\\u2513' },
            { symbol: '┗', label: 'Up Right', code: '\\u2517' },
            { symbol: '┛', label: 'Up Left', code: '\\u251B' },
            { symbol: '━', label: 'Horizontal', code: '\\u2501' },
            { symbol: '┃', label: 'Vertical', code: '\\u2503' },
            { symbol: '┣', label: 'Vert Right', code: '\\u2523' },
            { symbol: '┫', label: 'Vert Left', code: '\\u252B' },
            { symbol: '┳', label: 'Down Horiz', code: '\\u2533' },
            { symbol: '┻', label: 'Up Horiz', code: '\\u253B' },
            { symbol: '╋', label: 'Cross', code: '\\u254B' }
        ]
    },
    rounded: {
        name: 'Rounded Corners',
        chars: [
            { symbol: '╭', label: 'Down Right', code: '\\u256D' },
            { symbol: '╮', label: 'Down Left', code: '\\u256E' },
            { symbol: '╰', label: 'Up Right', code: '\\u2570' },
            { symbol: '╯', label: 'Up Left', code: '\\u256F' }
        ]
    },
    misc: {
        name: 'Miscellaneous',
        chars: [
            { symbol: '+', label: 'Plus', code: '\\u002B' },
            { symbol: '-', label: 'Minus/Dash', code: '\\u002D' },
            { symbol: '|', label: 'Pipe', code: '\\u007C' },
            { symbol: '╌', label: 'Light Dashed', code: '\\u254C' },
            { symbol: '╍', label: 'Heavy Dashed', code: '\\u254D' },
            { symbol: '╎', label: 'Light Dashed V', code: '\\u254E' },
            { symbol: '╏', label: 'Heavy Dashed V', code: '\\u254F' },
            { symbol: '╴', label: 'Light Left', code: '\\u2574' },
            { symbol: '╵', label: 'Light Up', code: '\\u2575' },
            { symbol: '╶', label: 'Light Right', code: '\\u2576' },
            { symbol: '╷', label: 'Light Down', code: '\\u2577' },
            { symbol: '╸', label: 'Heavy Left', code: '\\u2578' },
            { symbol: '╹', label: 'Heavy Up', code: '\\u2579' },
            { symbol: '╺', label: 'Heavy Right', code: '\\u257A' },
            { symbol: '╻', label: 'Heavy Down', code: '\\u257B' }
        ]
    }
};

document.addEventListener('DOMContentLoaded', () => {
    initMonaco();
    loadPresets();
    setupEventListeners();
    setupCharacterPalette();
    setupKeyboardShortcuts();
    buildAllCharactersList();
});

function buildAllCharactersList() {
    allCharacters = [];
    for (const [categoryKey, categoryData] of Object.entries(CHARACTER_CATEGORIES)) {
        categoryData.chars.forEach(char => {
            allCharacters.push({
                ...char,
                category: categoryData.name,
                categoryKey: categoryKey
            });
        });
    }
}

function initMonaco() {
    require.config({
        paths: {
            'vs': 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.44.0/min/vs'
        }
    });

    require(['vs/editor/editor.main'], function() {
        editor = monaco.editor.create(document.getElementById('editor'), {
            value: '// Select a preset or enter your character set here',
            language: 'javascript',
            theme: 'vs-dark',
            automaticLayout: true,
            fontSize: 13,
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            wordWrap: 'on',
            lineNumbers: 'on',
            renderWhitespace: 'selection',
            tabSize: 4,
        });

        editor.onDidChangeModelContent(() => {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => {
                parseAndRender();
            }, 500);
        });
    });
}

async function loadPresets() {
    try {
        const response = await fetch('/api/presets');
        const data = await response.json();

        const select = document.getElementById('presetSelect');

        data.presets.forEach(presetName => {
            const option = document.createElement('option');
            option.value = presetName;
            option.textContent = presetName.replace(/_/g, ' ');
            select.appendChild(option);
        });

    } catch (error) {
        showError('Failed to load presets: ' + error.message);
    }
}

function setupEventListeners() {
    document.getElementById('presetSelect').addEventListener('change', async (e) => {
        const presetName = e.target.value;
        if (!presetName) return;

        try {
            const response = await fetch(`/api/preset/${presetName}`);
            const data = await response.json();

            editor.setValue(data.formatted.javascript);
            currentCharset = data.charset;

        } catch (error) {
            showError('Failed to load preset: ' + error.message);
        }
    });

    document.getElementById('exportPython').addEventListener('click', () => exportCode('python'));
    document.getElementById('exportJS').addEventListener('click', () => exportCode('javascript'));
    document.getElementById('copyBtn').addEventListener('click', copyPreview);
    document.getElementById('refreshBtn').addEventListener('click', () => parseAndRender());
    document.getElementById('copyAllPatternsBtn').addEventListener('click', copyAllPatterns);

    document.getElementById('clearBtn').addEventListener('click', clearEditor);
    document.getElementById('undoBtn').addEventListener('click', () => editor?.trigger('keyboard', 'undo', null));
    document.getElementById('redoBtn').addEventListener('click', () => editor?.trigger('keyboard', 'redo', null));

    document.getElementById('searchToggleBtn').addEventListener('click', toggleSearch);
    document.getElementById('clearSearchBtn').addEventListener('click', clearSearch);
    document.getElementById('charSearch').addEventListener('input', handleSearch);
    document.getElementById('showAllCategoriesBtn').addEventListener('click', showAllCategories);
}

function setupCharacterPalette() {
    const categorySelect = document.getElementById('categorySelect');

    categorySelect.addEventListener('change', (e) => {
        const category = e.target.value;
        if (!category) {
            showPalettePlaceholder();
            return;
        }

        displayCharacters(category);
    });
}

function setupKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        if (e.key === '?' && !e.ctrlKey && !e.metaKey && !e.altKey) {
            const activeElement = document.activeElement;
            if (activeElement.tagName !== 'INPUT' && activeElement.tagName !== 'TEXTAREA') {
                e.preventDefault();
                toggleShortcutsPanel();
            }
        }

        if ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'K') {
            e.preventDefault();
            clearEditor();
        }

        if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
            e.preventDefault();
            toggleSearch();
            document.getElementById('charSearch').focus();
        }
    });

    document.getElementById('closeShortcuts').addEventListener('click', () => {
        document.getElementById('keyboardShortcuts').classList.remove('show');
    });
}

function toggleShortcutsPanel() {
    const panel = document.getElementById('keyboardShortcuts');
    panel.classList.toggle('show');
}

function clearEditor() {
    if (confirm('Clear the editor? This cannot be undone.')) {
        editor?.setValue('');
        showCopyFeedback('Editor cleared');
    }
}

function toggleSearch() {
    const searchBox = document.getElementById('searchBox');
    const isVisible = searchBox.style.display !== 'none';
    searchBox.style.display = isVisible ? 'none' : 'flex';

    if (!isVisible) {
        document.getElementById('charSearch').focus();
    }
}

function clearSearch() {
    document.getElementById('charSearch').value = '';
    handleSearch({ target: { value: '' } });
}

function handleSearch(e) {
    const query = e.target.value.toLowerCase().trim();

    if (!query) {
        showPalettePlaceholder();
        return;
    }

    const results = allCharacters.filter(char =>
        char.label.toLowerCase().includes(query) ||
        char.symbol === query
    );

    if (results.length === 0) {
        displayNoResults();
        return;
    }

    displaySearchResults(results);
}

function displaySearchResults(results) {
    const grid = document.getElementById('characterGrid');
    grid.innerHTML = '';

    results.forEach(char => {
        const card = createCharCard(char);
        card.classList.add('highlight');
        grid.appendChild(card);
    });
}

function displayNoResults() {
    const grid = document.getElementById('characterGrid');
    grid.innerHTML = '<div class="no-results">No characters found matching your search</div>';
}

function showAllCategories() {
    const grid = document.getElementById('characterGrid');
    grid.innerHTML = '';

    for (const [categoryKey, categoryData] of Object.entries(CHARACTER_CATEGORIES)) {
        const section = document.createElement('div');
        section.className = 'category-section';

        const title = document.createElement('div');
        title.className = 'category-section-title';
        title.textContent = categoryData.name;
        grid.appendChild(title);

        categoryData.chars.forEach(char => {
            const card = createCharCard(char);
            grid.appendChild(card);
        });
    }
}

function createCharCard(char) {
    const card = document.createElement('div');
    card.className = 'char-card';
    card.title = `${char.label}\nClick to copy: ${char.symbol}`;

    const symbol = document.createElement('div');
    symbol.className = 'char-symbol';
    symbol.textContent = char.symbol;

    const label = document.createElement('div');
    label.className = 'char-label';
    label.textContent = char.label;

    card.appendChild(symbol);
    card.appendChild(label);

    card.addEventListener('click', () => copyCharacter(char.symbol, card));

    return card;
}

function showPalettePlaceholder() {
    const grid = document.getElementById('characterGrid');
    grid.innerHTML = '<div class="palette-placeholder">Select a category to browse characters</div>';
}

function displayCharacters(category) {
    const categoryData = CHARACTER_CATEGORIES[category];
    if (!categoryData) return;

    const grid = document.getElementById('characterGrid');
    grid.innerHTML = '';

    categoryData.chars.forEach(char => {
        const card = createCharCard(char);
        grid.appendChild(card);
    });
}

async function copyCharacter(char, cardElement) {
    try {
        await navigator.clipboard.writeText(char);

        cardElement.classList.add('copied');

        showCopyFeedback(`Copied: ${char}`);

        setTimeout(() => {
            cardElement.classList.remove('copied');
        }, 400);

    } catch (error) {
        showError('Failed to copy character');
    }
}

function showCopyFeedback(message) {
    const feedback = document.getElementById('copyFeedback');
    feedback.textContent = message;
    feedback.classList.add('show');

    setTimeout(() => {
        feedback.classList.remove('show');
    }, 2000);
}

async function parseAndRender() {
    const code = editor.getValue();

    showError('');
    updateStatus('pending');

    try {
        const parseResponse = await fetch('/api/parse', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code })
        });

        const parseData = await parseResponse.json();

        if (!parseResponse.ok || parseData.error) {
            showError(parseData.error || 'Parse error');
            updateStatus('error');
            return;
        }

        currentCharset = parseData.charset;

        const renderResponse = await fetch('/api/render', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ charset: currentCharset })
        });

        const renderData = await renderResponse.json();

        if (!renderResponse.ok || renderData.error) {
            showError(renderData.error || 'Render error');
            updateStatus('error');
            return;
        }

        displayPatterns(renderData.patterns);
        updateStatus('success');

    } catch (error) {
        showError('Network error: ' + error.message);
        updateStatus('error');
    }
}

function displayPatterns(patterns) {
    const previewContainer = document.getElementById('preview');
    previewContainer.innerHTML = '';

    patterns.forEach(pattern => {
        const block = document.createElement('div');
        block.className = 'pattern-block';

        const title = document.createElement('div');
        title.className = 'pattern-title';
        title.textContent = pattern.title;

        const content = document.createElement('pre');
        content.className = 'pattern-content';
        content.textContent = pattern.content;

        block.appendChild(title);
        block.appendChild(content);
        previewContainer.appendChild(block);
    });
}

async function copyAllPatterns() {
    const previewContainer = document.getElementById('preview');
    const patterns = previewContainer.querySelectorAll('.pattern-content');

    if (patterns.length === 0) {
        showError('No patterns to copy');
        return;
    }

    const text = Array.from(patterns)
        .map(p => p.textContent)
        .join('\n\n');

    try {
        await navigator.clipboard.writeText(text);
        showCopyFeedback('All patterns copied!');
    } catch (error) {
        showError('Copy failed: ' + error.message);
    }
}

async function exportCode(format) {
    if (!currentCharset) {
        showError('No character set to export');
        return;
    }

    try {
        const response = await fetch(`/api/export/${format}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ charset: currentCharset })
        });

        const data = await response.json();

        if (!response.ok || data.error) {
            showError(data.error || 'Export error');
            return;
        }

        await navigator.clipboard.writeText(data.code);

        const btn = format === 'python' ?
            document.getElementById('exportPython') :
            document.getElementById('exportJS');

        const originalHTML = btn.innerHTML;
        btn.innerHTML = btn.innerHTML.replace(/Python|JavaScript/, '✓ Copied!');
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);

    } catch (error) {
        showError('Export failed: ' + error.message);
    }
}

async function copyPreview() {
    const previewContainer = document.getElementById('preview');
    const patterns = previewContainer.querySelectorAll('.pattern-content');

    if (patterns.length === 0) {
        showError('No preview to copy');
        return;
    }

    const text = Array.from(patterns)
        .map(p => p.textContent)
        .join('\n\n');

    try {
        await navigator.clipboard.writeText(text);

        const btn = document.getElementById('copyBtn');
        const originalHTML = btn.innerHTML;
        btn.innerHTML = btn.innerHTML.replace('Copy', '✓ Copied!');
        setTimeout(() => {
            btn.innerHTML = originalHTML;
        }, 2000);

    } catch (error) {
        showError('Copy failed: ' + error.message);
    }
}

function updateStatus(status) {
    const indicator = document.getElementById('editorStatus');
    indicator.className = 'status-indicator ' + status;
}

function showError(message) {
    const errorElement = document.getElementById('errorMessage');
    errorElement.textContent = message;
}
