"""Build the standalone preview and the Confluence HTML macro from one source."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
fragment = (root / 'src/generator.html').read_text(encoding='utf-8')
out = root / 'dist'
out.mkdir(exist_ok=True)
(out / 'confluence.txt').write_text(fragment, encoding='utf-8')
(out / 'preview.html').write_text(
    '<!doctype html><html lang="ru"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1">'
    '<title>Provider QA</title></head><body style="margin:0;background:#eef2f7">'
    + fragment + '</body></html>', encoding='utf-8')
print('Built dist/preview.html and dist/confluence.txt')
