"""pyinstaller hook file.

You need to use this hook-file if you are packaging a project using tkinterdnd2.
Just put hook-tkinterdnd2.py in the same directory where you call pyinstaller and type:

    pyinstaller --onefile tracker.py --additional-hooks-dir=C:\Users\ddeit\Desktop\pythonProject\PurpleTracker\hook-tkinterdnd2.py.
"""

from PyInstaller.utils.hooks import collect_data_files, eval_statement


datas = collect_data_files('tkinterdnd2')