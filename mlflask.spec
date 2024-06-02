# -*- mode: python ; coding: utf-8 -*-

datas = [
    ('models/mlbusiness.pkl', 'models'),
    ('models/mleconomy.pkl', 'models'),  # Путь к модели
    ('venv/Lib/site-packages/pandas', 'pandas'),  # Путь к библиотеке pandas
    ('venv/Lib/site-packages/joblib', 'joblib'),
    ('venv/Lib/site-packages/joblib', 'scikit-learn'),
    ('venv/Lib/site-packages/joblib', 'numpy'),
    ('venv/Lib/site-packages/joblib', 'requests'),
    ('venv/Lib/site-packages/joblib', 'flask'),  # Путь к библиотеке joblib
    # Добавьте другие библиотеки, если это необходимо
]

a = Analysis(
    ['mlflask.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mlflask',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)