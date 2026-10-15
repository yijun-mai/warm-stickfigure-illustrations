#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Package only the installable skill, including its notices and references."""
from pathlib import Path
import zipfile,sys
from validate_project import validate

ROOT=Path(__file__).resolve().parents[1]
if not validate():sys.exit(1)
dest=ROOT/'dist';dest.mkdir(exist_ok=True)
out=dest/'warm-stickfigure-illustrations.zip'
skill=ROOT/'warm-stickfigure-illustrations'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(skill.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts:z.write(p,p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    assert 'warm-stickfigure-illustrations/SKILL.md' in z.namelist()
print(out)
