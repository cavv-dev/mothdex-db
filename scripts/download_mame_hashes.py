#!/usr/bin/env python
import os
import sys
import subprocess
import shutil
import tempfile
from common import DATA_DIR


def download_mame_hashes():
    """Download the MAME hash files from the official MAME GitHub repository."""
    print("Downloading MAME hash files...")

    if not shutil.which('git'):
        print("Git is not installed or not found in PATH. Please install Git to proceed.")
        sys.exit(1)

    destination = os.path.join(DATA_DIR, 'mame', 'hash')
    os.makedirs(destination, exist_ok=True)

    repo_url = 'https://github.com/mamedev/mame.git'

    dir_path = 'hash'

    with tempfile.TemporaryDirectory() as temp_dir:
        subprocess.run(
            ['git', 'clone', '--depth', '1', '--filter=blob:none',
             '--sparse', repo_url, temp_dir],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        subprocess.run(
            ['git', '-C', temp_dir, 'sparse-checkout', 'set', dir_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        hash_dir = os.path.join(temp_dir, dir_path)
        if os.path.exists(hash_dir):
            for item in os.listdir(hash_dir):
                s = os.path.join(hash_dir, item)
                d = os.path.join(destination, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)

    print(f"Successfully downloaded MAME hash files to {destination}")
