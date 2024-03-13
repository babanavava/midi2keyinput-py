# midi2keyinput-py

pythonでMIDI入力を長押しなどにも対応可能なキーボード入力に変換します。

## 使用したライブラリ

- keyboard
- pygame

## 使用方法(windows前提)
まずgitとpythonを入れる

次にPowerShellでこのリポジトリをクローンしたい場所に移動した後で
```PowerShell
> git clone && cd 
> py -m venv .venv
> .venv/Scripts/activate
> py -m pip install -U pip setuptools
> py -m pip install -r requirements.txt
> py midi2keyinput.py
```
