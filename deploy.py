"""Deploy the application to a local directory without requiring a server."""

import argparse
from pathlib import Path
import shutil


def deploy(destination):
    source = Path(__file__).resolve().parent / "app.py"
    target = Path(destination).resolve()
    target.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target / "app.py")
    return target / "app.py"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    print(f"Deployed application to {deploy(args.target)}")


if __name__ == "__main__":
    main()
