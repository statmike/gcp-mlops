#!/usr/bin/env python3
"""Audit or apply standard tracking and IDE headers across statmike/gcp-mlops.

Mirrors the exact header template and exclusion rules of architectures/headers/add_headers.ipynb.

Usage:
  python3 architectures/headers/sync_headers.py --check
  python3 architectures/headers/sync_headers.py --apply
"""

import argparse
import fnmatch
import json
import os
import sys
import urllib.parse

GITHUB_ACCOUNT = 'statmike'
REPO_NAME = 'gcp-mlops'

EXCLUDE = [
    'LICENSE.md',
    'CONTRIBUTING.md',
    'CODE_OF_CONDUCT.md',
    'SECURITY.md',
    'agent-skills',
    '.agents',
    '.claude',
    'Applied ML/AI Agents/image-to-graph/examples',
    'Applied ML/AI Agents/data-mcp-sandbox/results',
    'data+ai/dataflow/gpu/benchmark/data/runs',
    '*/PLANS.md',
    '*/CLAUDE.md',
    '*/CHANGELOG.md',
    '*/blurb.md',
    'MLOps/Feature Store/BigQuery/BigQuery Feature Store - Overview.md',
    'MLOps/Feature Store/Bigtable/Bigtable Feature Store - Overview.md',
    'MLOps/Feature Store/Feature Store Overview.md',
    'MLOps/Feature Store/Spanner/Spanner Feature Store - Overview.md',
    'MLOps/Feature Store/Valkey/Valkey Feature Store - Overview.md',
]

ICONS = dict(
    bigquery='https://www.gstatic.com/images/branding/gcpiconscolors/bigquery/v1/32px.svg',
    github='https://www.svgrepo.com/download/217753/github.svg',
    colab='https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg',
    ecolab='https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN',
    vertex='https://www.gstatic.com/images/branding/gcpiconscolors/vertexai/v1/32px.svg',
    download='https://www.svgrepo.com/download/5445/download-button.svg',
    linkedin='https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg',
    bluesky='https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg',
    twitter='https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg',
    reddit='https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png',
    youtube='https://upload.wikimedia.org/wikipedia/commons/f/fd/YouTube_full-color_icon_%282024%29.svg',
)


def make_urls(root: str, file: str, repo_base: str) -> dict[str, str]:
    prefixes = dict(
        colab='https://colab.research.google.com/github/',
        bqstudio='https://console.cloud.google.com/bigquery/import?url=',
        ecolab='https://console.cloud.google.com/vertex-ai/colab/import/',
        github='https://github.com/',
        github_raw='https://raw.githubusercontent.com/',
        wbi='https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=',
        track='https://us-central1-vertex-ai-mlops-369716.cloudfunctions.net/pixel-tracking?',
        linkedin='https://www.linkedin.com/sharing/share-offsite/?url=',
        bluesky='https://bsky.app/intent/compose?text=',
        twitter='https://twitter.com/intent/tweet?url=',
        reddit='https://reddit.com/submit?url=',
    )

    path = root.replace(repo_base, f'{GITHUB_ACCOUNT}/{REPO_NAME}').split('/')
    path_part = urllib.parse.quote('/'.join(path[2:])) + '/' if len(path) > 2 else ''

    return dict(
        track=prefixes['track'] + f"path={urllib.parse.quote_plus('/'.join(path))}&file={urllib.parse.quote_plus(file)}",
        colab=prefixes['colab'] + '/'.join(path[0:2]) + '/blob/main/' + path_part + urllib.parse.quote(file),
        ecolab=prefixes['ecolab'] + urllib.parse.quote_plus(prefixes['github_raw'] + '/'.join(path[0:2]) + '/main/' + path_part + urllib.parse.quote(file)),
        github=prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + path_part + urllib.parse.quote(file),
        download=prefixes['github_raw'] + '/'.join(path[0:2]) + '/main/' + path_part + urllib.parse.quote(file),
        wbi=prefixes['wbi'] + prefixes['github_raw'] + '/'.join(path[0:2]) + '/main/' + path_part + urllib.parse.quote(file),
        bqstudio=prefixes['bqstudio'] + prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + path_part + urllib.parse.quote(file),
        linkedin=prefixes['linkedin'] + prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + urllib.parse.quote(path_part + urllib.parse.quote(file)),
        bluesky=prefixes['bluesky'] + prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + urllib.parse.quote(path_part + urllib.parse.quote(file)),
        twitter=prefixes['twitter'] + prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + urllib.parse.quote(path_part + urllib.parse.quote(file)),
        reddit=prefixes['reddit'] + prefixes['github'] + '/'.join(path[0:2]) + '/blob/main/' + urllib.parse.quote(path_part + urllib.parse.quote(file)),
        connect_github='https://www.github.com/statmike',
        connect_linkedin='https://www.linkedin.com/in/statmike',
        connect_youtube='https://www.youtube.com/@statmike-channel',
        connect_bluesky='https://bsky.app/profile/statmike.bsky.social',
        connect_twitter='https://x.com/statmike',
    )


def make_header(root: str, file: str, repo_base: str) -> str:
    urls = make_urls(root, file, repo_base)
    if file.endswith('.ipynb'):
        return f'''![tracker]({urls['track']})
<!--- header table --->
<table align="left">
<tr>
  <td style="text-align: center">
    <a href="{urls['github']}">
      <img width="32px" src="{ICONS['github']}" alt="GitHub logo">
      <br>View on<br>GitHub
    </a>
  </td>
  <td style="text-align: center">
    <a href="{urls['colab']}">
      <img width="32px" src="{ICONS['colab']}" alt="Google Colaboratory logo">
      <br>Run in<br>Colab
    </a>
  </td>
  <td style="text-align: center">
    <a href="{urls['ecolab']}">
      <img width="32px" src="{ICONS['ecolab']}" alt="Google Cloud Colab Enterprise logo">
      <br>Run in<br>Colab Enterprise
    </a>
  </td>      
  <td style="text-align: center">
    <a href="{urls['bqstudio']}">
      <img width="32px" src="{ICONS['bigquery']}" alt="BigQuery logo">
      <br>Open in<br>BigQuery Studio
    </a>
  </td>
  <td style="text-align: center">
    <a href="{urls['wbi']}">
      <img width="32px" src="{ICONS['vertex']}" alt="Vertex AI logo">
      <br>Open in<br>Vertex AI Workbench
    </a>
  </td>
</tr>
<tr>
  <td colspan="5" style="text-align: right">
    <b>Share This On: </b> 
    <a href="{urls['linkedin']}"><img src="{ICONS['linkedin']}" alt="Linkedin Logo" width="20px"></a> 
    <a href="{urls['reddit']}"><img src="{ICONS['reddit']}" alt="Reddit Logo" width="20px"></a> 
    <a href="{urls['bluesky']}"><img src="{ICONS['bluesky']}" alt="BlueSky Logo" width="20px"></a> 
    <a href="{urls['twitter']}"><img src="{ICONS['twitter']}" alt="X (Twitter) Logo" width="20px"></a> 
  </td>
</tr>
<tr>
  <td colspan="5" style="text-align: right">
    <b>Connect With Author On: </b> 
    <a href="{urls['connect_linkedin']}"><img src="{ICONS['linkedin']}" alt="Linkedin Logo" width="20px"></a>
    <a href="{urls['connect_github']}"><img src="{ICONS['github']}" alt="GitHub Logo" width="20px"></a> 
    <a href="{urls['connect_youtube']}"><img src="{ICONS['youtube']}" alt="YouTube Logo" width="20px"></a>
    <a href="{urls['connect_bluesky']}"><img src="{ICONS['bluesky']}" alt="BlueSky Logo" width="20px"></a> 
    <a href="{urls['connect_twitter']}"><img src="{ICONS['twitter']}" alt="X (Twitter) Logo" width="20px"></a>
  </td>
</tr>
<tr>
  <td colspan="5" style="text-align: right">
    <a href="{urls['download']}"><img src="{ICONS['download']}" alt="Download icon" width="20px"></a> <a href="{urls['download']}">Download Notebook</a> <i>(right-click and "Save As")</i>
  </td>
</tr>
</table>'''

    if file.endswith('.md'):
        return f'''![tracker]({urls['track']})
<!--- header table --->
<table>
<tr>     
  <td style="text-align: center">
    <a href="{urls['github']}">
      <img width="32px" src="{ICONS['github']}" alt="GitHub logo">
      <br>View on<br>GitHub
    </a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Share On: </b> 
    <a href="{urls['linkedin']}"><img src="{ICONS['linkedin']}" alt="Linkedin Logo" width="20px"></a> 
    <a href="{urls['reddit']}"><img src="{ICONS['reddit']}" alt="Reddit Logo" width="20px"></a> 
    <a href="{urls['bluesky']}"><img src="{ICONS['bluesky']}" alt="BlueSky Logo" width="20px"></a> 
    <a href="{urls['twitter']}"><img src="{ICONS['twitter']}" alt="X (Twitter) Logo" width="20px"></a> 
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Connect With Author On: </b> 
    <a href="{urls['connect_linkedin']}"><img src="{ICONS['linkedin']}" alt="Linkedin Logo" width="20px"></a>
    <a href="{urls['connect_github']}"><img src="{ICONS['github']}" alt="GitHub Logo" width="20px"></a> 
    <a href="{urls['connect_youtube']}"><img src="{ICONS['youtube']}" alt="YouTube Logo" width="20px"></a>
    <a href="{urls['connect_bluesky']}"><img src="{ICONS['bluesky']}" alt="BlueSky Logo" width="20px"></a> 
    <a href="{urls['connect_twitter']}"><img src="{ICONS['twitter']}" alt="X (Twitter) Logo" width="20px"></a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <a href="{urls['download']}"><img src="{ICONS['download']}" alt="Download icon" width="20px"></a> <a href="{urls['download']}">Download File</a> <i>(right-click and "Save As")</i>
  </td>
</tr>
</table><br/><br/>

---
'''
    return ''


def is_excluded(rel_root: str, rel_path: str) -> bool:
    exclude_wildcards = [e for e in EXCLUDE if e.startswith('*/')]
    exclude_paths = [e for e in EXCLUDE if not e.startswith('*/')]
    if any(rel_root.startswith(e + '/') or rel_root == e for e in exclude_paths):
        return True
    for p in exclude_paths:
        if rel_path == p or rel_path.startswith(p + '/'):
            return True
    for pattern in exclude_wildcards:
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch('/' + rel_path, pattern):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description='Check or apply repository headers.')
    parser.add_argument('--apply', action='store_true', help='Apply missing or outdated headers.')
    parser.add_argument('--check', action='store_true', help='Check headers without modifying files.')
    args = parser.parse_args()

    repo_base = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    audited = 0
    drifted = []
    legacy = []
    updated = 0

    for root, dirs, files in os.walk(repo_base):
        dirs[:] = [
            d for d in dirs
            if d not in {'.git', '.ipynb_checkpoints', '.venv', '.adk', '.pytest_cache', 'temp'}
        ]
        rel_root = root.replace(repo_base + '/', '', 1) if root != repo_base else ''
        if (
            root.endswith('.ipynb_checkpoints')
            or '/temp' in root
            or '.venv/' in root
            or '.adk' in root
            or '.pytest_cache' in root
        ):
            continue

        for file in sorted(files):
            if not file.endswith(('.md', '.ipynb')):
                continue
            rel_path = os.path.join(rel_root, file) if rel_root else file
            if is_excluded(rel_root, rel_path):
                continue

            full_path = os.path.join(root, file)
            expected_header = make_header(root, file, repo_base)

            if file.endswith('.md'):
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if content.startswith('<!--- header table --->') or content.startswith('![tracker](https://'):
                    end_index = None
                    pos = 0
                    for line in content.split('\n'):
                        if line.startswith('#'):
                            end_index = pos
                            break
                        pos += len(line) + 1
                    if end_index is None:
                        continue
                    prior = content[0:end_index]
                else:
                    end_index = 0
                    prior = ''

                if 'path=statmike%2Fvertex-ai-mlops' in prior:
                    legacy.append(rel_path)
                if prior != expected_header:
                    drifted.append(rel_path)
                    if args.apply:
                        with open(full_path, 'w', encoding='utf-8') as f:
                            f.write(expected_header + content[end_index:])
                        updated += 1
                audited += 1

            elif file.endswith('.ipynb'):
                with open(full_path, 'r', encoding='utf-8') as f:
                    nb_raw = json.load(f)
                cells = nb_raw.get('cells', [])
                prior = ''
                end_index = 0
                if cells and cells[0].get('cell_type') == 'markdown':
                    src = cells[0].get('source', '')
                    content = ''.join(src) if isinstance(src, list) else src
                    if content.startswith('<!--- header table --->') or content.startswith('![tracker](https://'):
                        end_index = len(content)
                        prior = content

                if 'path=statmike%2Fvertex-ai-mlops' in prior:
                    legacy.append(rel_path)
                if prior != expected_header:
                    drifted.append(rel_path)
                    if args.apply:
                        import nbformat as nbf
                        nb = nbf.read(full_path, nbf.NO_CONVERT)
                        header_cell = nbf.v4.new_markdown_cell(source=expected_header)
                        if end_index == 0:
                            nb['cells'].insert(0, header_cell)
                        else:
                            nb['cells'][0] = header_cell
                        nbf.write(nb, full_path, version=nbf.NO_CONVERT)
                        updated += 1
                audited += 1

    print(f'Audited files: {audited}')
    print(f'Header drift / missing: {len(drifted)}')
    print(f'Legacy headers: {len(legacy)}')
    if args.apply:
        print(f'Updated files: {updated}')

    if (drifted or legacy) and not args.apply:
        for p in drifted[:10]:
            print(f'  DRIFT: {p}')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
