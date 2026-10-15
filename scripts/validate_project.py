#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate packaging and local references. Does not judge visual quality."""
from pathlib import Path
import json,re,struct,sys

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'warm-stickfigure-illustrations'
def validate():
    errors=[]
    required=['README.md','LICENSE','NOTICE.md','examples/prompts.md','validation/generation-prompts.json','validation/example-manifest.json','warm-stickfigure-illustrations/SKILL.md','warm-stickfigure-illustrations/agents/openai.yaml']
    for name in required:
        if not (ROOT/name).is_file(): errors.append('missing: '+name)
    entry=(SKILL/'SKILL.md').read_text(encoding='utf-8')
    if not re.search(r'^name: warm-stickfigure-illustrations$',entry,re.M):errors.append('skill name mismatch')
    if not re.search(r'^description: .+',entry,re.M):errors.append('description missing')
    for p in ROOT.rglob('*'):
        if not p.is_file() or any(part in {'.git','dist','__pycache__'} for part in p.relative_to(ROOT).parts):continue
        if p.name.startswith('.env'):errors.append('unexpected environment file: '+p.name)
        if p.suffix not in {'.md','.py','.json','.yaml','.yml'}:continue
        text=p.read_text(encoding='utf-8')
        if re.search(r'(?:ghp_|github_pat_|sk-proj-)[A-Za-z0-9_]{15,}',text):errors.append('possible credential in '+p.name)
        if re.search(r'[DE]:[\\/]Users[\\/]',text):errors.append('personal filesystem path in '+p.name)
        if p.suffix=='.md':
            for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
                target=target.strip('<>').split('#')[0]
                if not target or target.startswith(('https://','http://','mailto:')):continue
                if not (p.parent/target).exists():errors.append('broken link: '+p.name+' -> '+target)
        if p.suffix=='.md' and '[TODO' in text:errors.append('unfinished scaffold in '+p.name)
    manifest=json.loads((ROOT/'validation/example-manifest.json').read_text(encoding='utf-8'))
    if len(manifest)!=8:errors.append('expected 8 showcase images')
    for row in manifest:
        p=ROOT/row['file']
        if not p.is_file():errors.append('missing image '+row['file']);continue
        data=p.read_bytes()
        if data[:8]!=b'\x89PNG\r\n\x1a\n':errors.append('not PNG '+row['file']);continue
        width,height=struct.unpack('>II',data[16:24])
        if (width,height)!=(row['width'],row['height']):errors.append('dimensions mismatch '+row['file'])
        if abs(width/height-16/9)>.015:errors.append('unexpected aspect ratio '+row['file'])
    print(json.dumps({'ok':not errors,'errors':errors,'showcase_images':len(manifest),'scope':'file structure, local links, image headers and packaging hygiene; not automated visual/OCR validation'},ensure_ascii=False))
    return not errors

if __name__=='__main__':sys.exit(0 if validate() else 1)
