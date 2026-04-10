import shutil
from pathlib import Path

notebooks_root = Path(__file__).parent.parent / "notebooks"

for batch in ["batch_1", "batch_2"]:
    batch_dir = notebooks_root / batch
    for src in batch_dir.rglob("*.ipynb"):
        # Skip checkpoints and already-copied -tv notebooks
        if ".ipynb_checkpoints" in src.parts or src.stem.endswith("-tv"):
            continue
        dst = src.with_name(src.stem + "-tv.ipynb")
        shutil.copy2(src, dst)
        print(f"Copied: {dst.relative_to(notebooks_root)}")
