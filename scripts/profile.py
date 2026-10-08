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
if stage == "install":
    snapshot = subprocess.check_output([sys.executable, "scripts/engineering-bootstrap.py"], text=True).strip()
    subprocess.run([sys.executable, snapshot + "/helpers/godot-setup.py", "--version", "4.7.2", "--origin", "godot-builds", "--binary-checksum", "sha512:9aa00f7a605200940bce3027a567b782f49bd8e940dd06ae9e987bd65aee1b1467edd56ed84fcdcbdd44354bf613bdbb4e5d2913e925850368e150c59ed54c65", "--root", str(root / ".artifacts/godot")], check=True)
elif stage == "lint":
    text = (root / "project.godot").read_text()
    assert "config_version=5" in text and 'config/name="gdam-test-godot"' in text
    assert 'config/icon="res://icon.svg"' in text
    assert "run/main_scene" not in text, "fixture capabilities must be reviewed when a game scene is added"
    assert ET.parse(root / "icon.svg").getroot().tag == "{http://www.w3.org/2000/svg}svg"
elif stage == "check":
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
    raise SystemExit("usage: profile.py install|lint|check")
