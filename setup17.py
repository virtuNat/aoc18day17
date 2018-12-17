import sys
from cx_Freeze import setup, Executable

# Dependency list.
build_exe_options = {
    'packages': ['pygame'], 
    'excludes': ['tkinter', 'numpy'],
    'include_files': ['Day17Input.txt']
}
# Base for GUI apps on Windows.
base = 'Win32GUI' if sys.platform == 'win32' else None

setup(
    name = 'Advent of Code Day 17 Simulator',
    version = '1.17',
    description = 'Naive Water Flow Simulator',
    url = '',
    author = 'virtuNat',
    author_email = '',
    license = 'GPL',
    options = {'build_exe': build_exe_options},
    executables = [Executable('day17.py', base=base)],
    )
        