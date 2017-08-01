import os
import csv
import shutil
import subprocess

from powerlibs.aws.λ.deployer import settings


def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


class TempDir(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        ensure_dir(self.path)
        return self.path

    def __exit__(self, *args):
        shutil.rmtree(self.path)


def read_env_vars(filepath):
    with open(filepath, 'r') as f:
        return dict(csv.reader(f, delimiter=str('=')))


def zip_package(dir_path):
    zip_path = os.path.join(settings.BASE_TMP_DIR, 'package')
    return shutil.make_archive(zip_path, 'zip', dir_path, '.')


def install_requirements():
    subprocess.Popen(
        ["pip", "--upgrade", "install", "-r", settings.REQUIREMENTS_FILE],
        shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
