"""Validate a built static release before publishing. Python 3 standard library only."""
import hashlib
import json
import sys
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

root = Path(sys.argv[1]).resolve()
catalog = json.loads((root / 'catalog.json').read_text())
base = catalog['url']
base_path = urlparse(base).path


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if 'id' in values:
            self.ids.add(values['id'])
        for key in ('href', 'src'):
            if key in values:
                self.links.append(values[key])


pages = {}
for path in root.rglob('*.html'):
    page = Page()
    page.feed(path.read_text())
    pages[path] = page

errors = []
for path, page in pages.items():
    for link in page.links:
        if link.startswith(base):
            parsed = urlparse(link)
            target = root / unquote(parsed.path[len(base_path):])
            if target.is_dir():
                target /= 'index.html'
            if not target.exists():
                errors.append(f'{path.relative_to(root)}: missing {link}')
            elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)}: missing anchor {link}')
        elif link.startswith('#') and unquote(link[1:]) not in page.ids:
            errors.append(f'{path.relative_to(root)}: missing anchor {link}')

entries = catalog['entries']
assert len({entry['id'] for entry in entries}) == len(entries), 'Duplicate IDs'
for kind, count in catalog['counts'].items():
    assert sum(entry['kind'] == kind for entry in entries) == count, kind
for entry in entries:
    assert len(entry['source_revision']) == 40, entry['id']
    if entry['kind'] == 'resource':
        assert entry['sources'] and entry['limitations'], entry['id']
        assert entry['independently_reproduced'] is False, entry['id']
    if 'sha256' in entry:
        raw = root / entry['markdown'].removeprefix(base)
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == entry['sha256'], entry['id']
    if entry['kind'] == 'skill':
        with zipfile.ZipFile(root / entry['download_url'].removeprefix(base)) as archive:
            assert set(archive.namelist()) == {entry['name'] + '/SKILL.md', entry['name'] + '/LICENSE'}
            assert hashlib.sha256(archive.read(entry['name'] + '/SKILL.md')).hexdigest() == entry['sha256']

for path in root.rglob('*'):
    if not path.is_file():
        continue
    if path.suffix == '.json':
        json.loads(path.read_text())
    if path.suffix in ('.md', '.html', '.json', '.txt', '.css', '.js'):
        text = path.read_text()
        for forbidden in ('/Users/', 'credentials.json', 'SSH_ASKPASS', '-----BEGIN OPENSSH PRIVATE KEY-----'):
            assert forbidden not in text, f'Private deployment information: {path}'
assert not errors, '\n'.join(errors)
print(json.dumps({'status': 'passed', 'html_pages': len(pages), 'entries': len(entries), 'counts': catalog['counts'], 'revision': catalog['content_revision']}))
