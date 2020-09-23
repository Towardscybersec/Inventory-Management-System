application_title = "Inventory"
main_python_file = "index.py"

import sys

from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

includes = []
include_files = ['themes']

setup(
    name = application_title,
    version = "0.1",
    description = "inventory",
    options = {"build_exe" : {"includes" : includes, "include_files" : include_files}},
    executables = [Executable(main_python_file, base = base)])
