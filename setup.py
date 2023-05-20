import subprocess
import sys
from importlib.util import find_spec as check_exists

global installed
installed = []

def install(package):
    print("Package %s not installed; installing now" % package)
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    installed.append(package)

try:
    assert check_exists("cv2") is not None
except ImportError:
    install("opencv-python")

try:
    assert check_exists("PIL") is not None
except ImportError:
    install("Pillow")

try:
    assert check_exists("numpy") is not None
except ImportError:
    install("numpy")

try:
    assert check_exists("pandas") is not None
except ImportError:
    install("pandas")

if installed is not None:
    [print("Package %s successfully installed", p) for p in installed]
else:
    print("All modules correctly installed")