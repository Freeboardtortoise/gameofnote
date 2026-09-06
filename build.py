# build.py
from pathlib import Path

files = [
    "vector.py",
    "stateMachine.py",
    "Constants.py",
    "mobs.py",
    "shader.py",
    "attacking.py",
    "placing.py",
    "generation.py",
    "lives.py",
    "playerMovement.py",
    "inventory.py",
    "startScreen.py",
    "code.py"

]

source_dir = Path("src")
output = "\n\n".join(
    (source_dir / filename).read_text(encoding="utf-8")
    for filename in files
)

Path("game.py").write_text(output, encoding="utf-8")

