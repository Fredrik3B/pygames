import cx_Freeze

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("pygame1.py")]

options = {
    'build_exe':
        {"packages": ["pygame"],
         'include_files': [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            "racerbil.png",
        ],
        },
}

cx_Freeze.setup(
    name="A bit Racey",
    options=options,
    executables=executables
)

"""Fatal Python error: initfsencoding: unable to load the file system codec
ImportError: invalid flags 1540036830 in 'encodings'

Current thread 0x0006d18c (most recent call first):
"""
