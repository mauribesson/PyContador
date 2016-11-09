from distutils.core import setup
import py2exe, sys

class Make_exe():
    def __init__(self, python_script):
        sys.argv.append('py2exe')

        setup(
            console=[{'script': python_script}],
            zipfile = None,
            options={
                'py2exe': 
                {
                    'bundle_files': 3, 
                    'compressed': True,
                    # Add includes if necessary, e.g. 
                    'includes': ['PyQt4', 'sys'],
                }
            }
        )

if __name__ == '__main__':
    Make_exe('code.py')