"""Install the verified engine and import a copy of this consumer fixture."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
os.chdir(root)
stage = sys.argv[1]
if stage == "lint":
    text = (root / "project.godot").read_text()
    assert "config_version=5" in text and 'config/name="gdam-test-godot"' in text
    assert 'config/icon="res://icon.svg"' in text
    assert "run/main_scene" not in text, "fixture capabilities must be reviewed when a game scene is added"
    assert ET.parse(root / "icon.svg").getroot().tag == "{http://www.w3.org/2000/svg}svg"
elif stage == "unit":
    target = root / ".artifacts/import-project"
    shutil.rmtree(target, ignore_errors=True)
    target.mkdir(parents=True)
    for name in ("project.godot", "icon.svg", "icon.svg.import"):
        shutil.copy2(root / name, target / name)
    result = subprocess.run([str(root / ".artifacts/godot/bin/godot"), "--headless", "--editor", "--path", str(target), "--import", "--quit"], capture_output=True, text=True, timeout=120)
    output = result.stdout + result.stderr
    (root / ".artifacts/import.log").write_text(output)
    if result.returncode or "ERROR:" in output:
        raise SystemExit(output)
    assert any((target / ".godot/imported").glob("icon.svg-*.ctex")), "fixture icon was not imported"
    print("Verified engine imported the consumer fixture; source resources unchanged")
else:
    raise SystemExit("usage: check_fixture.py lint|unit")
