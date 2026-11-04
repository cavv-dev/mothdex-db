#!/usr/bin/env python
import os
import sys
import subprocess
import shutil
import tempfile
from common import DATA_DIR


def download_libretro_dats():
    """Download Libretro DAT files from the official GitHub repository."""
    print("Downloading Libretro DAT files...")

    if not shutil.which('git'):
        print("Git is not installed or not found in PATH. Please install Git to proceed.")
        sys.exit(1)

    base_destination = os.path.join(DATA_DIR, 'libretro')

    repo_url = 'https://github.com/libretro/libretro-database.git'

    directories_to_clone = ['dat', 'metadat']

    for dir_name in directories_to_clone:
        destination = os.path.join(base_destination, dir_name)
        os.makedirs(destination, exist_ok=True)

    with tempfile.TemporaryDirectory() as temp_dir:
        subprocess.run(
            ['git', 'clone', '--depth', '1', '--filter=blob:none',
             '--sparse', repo_url, temp_dir],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        for dir_name in directories_to_clone:
            subprocess.run(
                ['git', '-C', temp_dir, 'sparse-checkout', 'set', dir_name],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            source_dir = os.path.join(temp_dir, dir_name)
            destination = os.path.join(base_destination, dir_name)

            if os.path.exists(source_dir):
                for item in os.listdir(source_dir):
                    s = os.path.join(source_dir, item)
                    d = os.path.join(destination, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, dirs_exist_ok=True)
                    else:
                        shutil.copy2(s, d)

    print(f"Successfully downloaded Libretro DAT files to {base_destination}")
