import { useState, useEffect } from 'react';
import { PRESETS } from './presets';
import { generateAllPatterns, PreviewPattern } from './renderer';

interface Character {
  symbol: string;
  label: string;
}

interface CategoryData {
  name: string;
  chars: Character[];
}

const CHARACTER_CATEGORIES: Record<string, CategoryData> = {
  corners: {
    name: 'Corners',
    chars: [
      { symbol: '┌', label: 'Light Down Right' },
      { symbol: '┐', label: 'Light Down Left' },
      { symbol: '└', label: 'Light Up Right' },
      { symbol: '┘', label: 'Light Up Left' },
      { symbol: '╔', label: 'Double Down Right' },
      { symbol: '╗', label: 'Double Down Left' },
      { symbol: '╚', label: 'Double Up Right' },
      { symbol: '╝', label: 'Double Up Left' },
      { symbol: '┏', label: 'Heavy Down Right' },
      { symbol: '┓', label: 'Heavy Down Left' },
      { symbol: '┗', label: 'Heavy Up Right' },
      { symbol: '┛', label: 'Heavy Up Left' },
      { symbol: '╭', label: 'Rounded Down Right' },
      { symbol: '╮', label: 'Rounded Down Left' },
      { symbol: '╰', label: 'Rounded Up Right' },
      { symbol: '╯', label: 'Rounded Up Left' }
    ]
  },
  lines: {
    name: 'Lines',
    chars: [
      { symbol: '─', label: 'Horizontal' },
      { symbol: '│', label: 'Vertical' },
      { symbol: '═', label: 'Double Horiz' },
      { symbol: '║', label: 'Double Vert' },
      { symbol: '━', label: 'Heavy Horiz' },
      { symbol: '┃', label: 'Heavy Vert' },
    ]
  },
  junctions: {
    name: 'T-Junctions',
    chars: [
      { symbol: '├', label: 'Vert Right' },
      { symbol: '┤', label: 'Vert Left' },
      { symbol: '┬', label: 'Down Horiz' },
      { symbol: '┴', label: 'Up Horiz' },
      { symbol: '╠', label: 'Double Right' },
      { symbol: '╣', label: 'Double Left' },
      { symbol: '╦', label: 'Double Down' },
      { symbol: '╩', label: 'Double Up' },
    ]
  },
  crosses: {
    name: 'Crosses',
    chars: [
      { symbol: '┼', label: 'Light Cross' },
      { symbol: '╬', label: 'Double Cross' },
      { symbol: '╋', label: 'Heavy Cross' },
      { symbol: '╪', label: 'Mixed Cross' },
    ]
  }
};

function App() {
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [selectedPreset, setSelectedPreset] = useState<string>('SINGLE_LINE');
  const [searchQuery, setSearchQuery] = useState('');
  const [showSearch, setShowSearch] = useState(false);
  const [feedback, setFeedback] = useState('');
  const [previews, setPreviews] = useState<PreviewPattern[]>([]);
  const [customCharset, setCustomCharset] = useState(PRESETS.SINGLE_LINE.charset);
  const [editorContent, setEditorContent] = useState('');

  useEffect(() => {
    const charset = PRESETS[selectedPreset].charset;
    setCustomCharset(charset);

    const formatted = `{
  "top_left": "${charset.top_left}",
  "top_right": "${charset.top_right}",
  "bottom_left": "${charset.bottom_left}",
  "bottom_right": "${charset.bottom_right}",
  "horizontal": "${charset.horizontal}",
  "vertical": "${charset.vertical}",
  "tjunction_up": "${charset.tjunction_up}",
  "tjunction_down": "${charset.tjunction_down}",
  "tjunction_left": "${charset.tjunction_left}",
  "tjunction_right": "${charset.tjunction_right}",
  "cross": "${charset.cross}"
}`;
    setEditorContent(formatted);
  }, [selectedPreset]);

  useEffect(() => {
    const patterns = generateAllPatterns(customCharset);
    setPreviews(patterns);
  }, [customCharset]);

  const handleEditorChange = (value: string) => {
    setEditorContent(value);

    try {
      const parsed = JSON.parse(value);
      if (parsed.top_left && parsed.horizontal && parsed.vertical) {
        setCustomCharset({
          top_left: parsed.top_left,
          top_right: parsed.top_right,
          bottom_left: parsed.bottom_left,
          bottom_right: parsed.bottom_right,
          horizontal: parsed.horizontal,
          vertical: parsed.vertical,
          tjunction_up: parsed.tjunction_up,
          tjunction_down: parsed.tjunction_down,
          tjunction_left: parsed.tjunction_left,
          tjunction_right: parsed.tjunction_right,
          cross: parsed.cross,
        });
      }
    } catch (e) {
      // Invalid JSON, don't update
    }
  };

  const copyCharacter = async (char: string) => {
    try {
      await navigator.clipboard.writeText(char);
      setFeedback(`Copied: ${char}`);
      setTimeout(() => setFeedback(''), 2000);
    } catch (error) {
      setFeedback('Failed to copy');
    }
  };

  const copyPreview = async (content: string) => {
    try {
      await navigator.clipboard.writeText(content);
      setFeedback('Preview copied!');
      setTimeout(() => setFeedback(''), 2000);
    } catch (error) {
      setFeedback('Failed to copy');
    }
  };

  const getFilteredCharacters = () => {
    if (!searchQuery) return [];

    const results: Character[] = [];
    Object.values(CHARACTER_CATEGORIES).forEach(category => {
      category.chars.forEach(char => {
        if (
          char.label.toLowerCase().includes(searchQuery.toLowerCase()) ||
          char.symbol === searchQuery
        ) {
          results.push(char);
        }
      });
    });
    return results;
  };

  const getDisplayCharacters = () => {
    if (searchQuery && showSearch) {
      return getFilteredCharacters();
    }
    if (selectedCategory) {
      return CHARACTER_CATEGORIES[selectedCategory]?.chars || [];
    }
    return [];
  };

  const displayChars = getDisplayCharacters();

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === '?' && !e.ctrlKey && !e.metaKey) {
        const target = e.target as HTMLElement;
        if (target.tagName !== 'INPUT' && target.tagName !== 'TEXTAREA') {
          e.preventDefault();
          alert('Keyboard Shortcuts:\n? - Show shortcuts\nCtrl+F - Search\nClick characters to copy');
        }
      }
      if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
        e.preventDefault();
        setShowSearch(true);
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="min-h-screen bg-[#0f0f0f] text-[#e8e8e8]">
      <header className="bg-gradient-to-b from-[#1a1a1a] to-[#0f0f0f] border-b border-[#333333] shadow-lg">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center gap-4">
            <svg className="text-[#3b82f6]" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <rect x="3" y="3" width="18" height="18" rx="2"/>
              <line x1="3" y1="9" x2="21" y2="9"/>
              <line x1="9" y1="3" x2="9" y2="21"/>
            </svg>
            <div>
              <h1 className="text-xl font-semibold">ASCII Box Character Editor</h1>
              <p className="text-sm text-[#a0a0a0]">Design and export box-drawing characters</p>
            </div>
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-6 py-6">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
          <div className="bg-[#1a1a1a] border border-[#333333] rounded-lg overflow-hidden">
            <div className="px-6 py-4 border-b border-[#333333] bg-[#242424]">
              <h2 className="text-lg font-semibold mb-1">Character Set Editor</h2>
              <p className="text-sm text-[#a0a0a0]">Edit characters to update all previews in real-time</p>
            </div>

            <div className="px-6 py-3 border-b border-[#333333] bg-[#0f0f0f]">
              <label className="block text-xs text-[#a0a0a0] mb-2 uppercase tracking-wider">Load Preset</label>
              <select
                value={selectedPreset}
                onChange={(e) => setSelectedPreset(e.target.value)}
                className="px-4 py-2 bg-[#242424] text-[#e8e8e8] border border-[#333333] rounded-md text-sm focus:outline-none focus:border-[#3b82f6] w-full"
              >
                {Object.entries(PRESETS).map(([key, data]) => (
                  <option key={key} value={key}>{data.name}</option>
                ))}
              </select>
            </div>

            <textarea
              value={editorContent}
              onChange={(e) => handleEditorChange(e.target.value)}
              className="w-full h-[500px] bg-[#0f0f0f] text-[#e8e8e8] p-4 font-mono text-sm resize-none focus:outline-none border-t border-[#333333]"
              spellCheck={false}
            />
          </div>

          <div className="bg-[#1a1a1a] border border-[#333333] rounded-lg overflow-hidden">
            <div className="px-6 py-4 border-b border-[#333333] bg-[#242424]">
              <h2 className="text-lg font-semibold mb-1">Live Preview Examples</h2>
              <p className="text-sm text-[#a0a0a0]">Click any preview to copy - Updates as you edit</p>
            </div>

            <div className="h-[500px] overflow-y-auto p-6 space-y-4">
              {previews.map((preview, idx) => (
                <div
                  key={idx}
                  className="bg-[#242424] border border-[#333333] rounded-lg overflow-hidden hover:border-[#3b82f6] transition-colors cursor-pointer group"
                  onClick={() => copyPreview(preview.content)}
                  title="Click to copy"
                >
                  <div className="px-3 py-2 bg-[#1a1a1a] border-b border-[#333333]">
                    <h3 className="text-xs font-semibold text-[#a0a0a0] uppercase tracking-wider group-hover:text-[#3b82f6] transition-colors">
                      {preview.title}
                    </h3>
                  </div>
                  <div className="p-4">
                    <pre className="font-mono text-sm text-[#e8e8e8] whitespace-pre">{preview.content}</pre>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="bg-[#1a1a1a] border border-[#333333] rounded-lg overflow-hidden">
          <div className="px-6 py-4 border-b border-[#333333] bg-[#242424]">
            <h2 className="text-lg font-semibold mb-1">Character Palette</h2>
            <p className="text-sm text-[#a0a0a0]">Click any character to copy</p>
          </div>

          <div className="px-6 py-3 border-b border-[#333333] flex gap-3">
            <select
              value={selectedCategory}
              onChange={(e) => {
                setSelectedCategory(e.target.value);
                setShowSearch(false);
                setSearchQuery('');
              }}
              className="px-3 py-2 bg-[#242424] text-[#e8e8e8] border border-[#333333] rounded-md text-sm focus:outline-none focus:border-[#3b82f6]"
            >
              <option value="">Select Category...</option>
              {Object.entries(CHARACTER_CATEGORIES).map(([key, data]) => (
                <option key={key} value={key}>{data.name}</option>
              ))}
            </select>

            <button
              onClick={() => setShowSearch(!showSearch)}
              className="px-4 py-2 bg-[#242424] text-[#e8e8e8] border border-[#333333] rounded-md text-sm hover:bg-[#2a2a2a] transition-colors"
            >
              🔍 Search
            </button>
          </div>

          {showSearch && (
            <div className="px-6 py-3 border-b border-[#333333] bg-[#242424]">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search characters by name..."
                className="w-full px-3 py-2 bg-[#0f0f0f] text-[#e8e8e8] border border-[#333333] rounded-md text-sm focus:outline-none focus:border-[#3b82f6]"
                autoFocus
              />
            </div>
          )}

          <div className="p-6">
            {displayChars.length === 0 ? (
              <div className="text-center py-12 text-[#707070] italic">
                {searchQuery ? 'No characters found' : 'Select a category to browse characters'}
              </div>
            ) : (
              <div className="grid grid-cols-6 sm:grid-cols-8 md:grid-cols-10 lg:grid-cols-12 gap-3">
                {displayChars.map((char, idx) => (
                  <button
                    key={idx}
                    onClick={() => copyCharacter(char.symbol)}
                    className="aspect-square bg-[#242424] border border-[#333333] rounded-lg flex flex-col items-center justify-center p-2 hover:border-[#3b82f6] hover:-translate-y-0.5 hover:shadow-lg hover:shadow-[#3b82f6]/20 transition-all group"
                    title={`${char.label}\nClick to copy: ${char.symbol}`}
                  >
                    <span className="text-2xl font-mono mb-1">{char.symbol}</span>
                    <span className="text-[8px] text-[#707070] text-center uppercase tracking-wide group-hover:text-[#a0a0a0]">
                      {char.label}
                    </span>
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {feedback && (
        <div className="fixed bottom-6 right-6 bg-[#2a2a2a] border border-[#333333] rounded-lg px-4 py-3 shadow-xl animate-in fade-in slide-in-from-bottom-2">
          <p className="text-[#22c55e] font-medium text-sm">{feedback}</p>
        </div>
      )}

      <footer className="mt-12 border-t border-[#333333] bg-[#1a1a1a] py-4">
        <div className="max-w-7xl mx-auto px-6 text-center text-sm text-[#707070]">
          Press <kbd className="px-2 py-1 bg-[#242424] border border-[#333333] rounded text-xs">?</kbd> for keyboard shortcuts
        </div>
      </footer>
    </div>
  );
}

export default App;
