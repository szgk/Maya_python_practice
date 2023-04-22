import os
import pymel.core as pm
import subprocess
import logging


class ListScriptsWindow(object):
    """
    スクリプトディレクトリにあるPythonスクリプトの一覧を表示するウィンドウを作成するクラス
    """
    def __init__(self):
        """
        ウィンドウとレイアウトを作成し、スクリプトディレクトリを設定するコンストラクタ
        """
        self.window = pm.window(title='Script List', widthHeight=(300, 300))
        self.layout = pm.columnLayout(parent=self.window)
        # スクリプトディレクトリを取得
        self.script_directory = pm.internalVar(userScriptDir=True)

    def show(self):
        """
        ウィンドウを表示するメソッド
        """
        self.list_scripts()
        pm.showWindow(self.window)


    def list_scripts(self):
        """
        スクリプトディレクトリ内のPythonスクリプトを一覧表示するメソッド
        """
        # scriptsディレクトリ内の.py, .melファイル名を格納
        scripts = []

        for f in os.listdir(self.script_directory):
          if os.path.isfile(os.path.join(self.script_directory, f)) and f.endswith(('.py', 'mel')):
              scripts.append(f)

        for script in scripts:
            # スクリプト名をボタンとして表示
            label = script.replace('.mel', '') + ' copy to clip board'
            pm.button(label=label, command=lambda _, _script=script: self.run_script(_script))

    def run_script(self, script):
        """
        指定されたPythonスクリプトを実行するメソッド
        """

        # pythonファイルの場合、スクリプトの内容を実行する
        if script.endswith('.py'):
          script_path = os.path.join(self.script_directory, script)
          with open(script_path, encoding="utf-8") as f:
            script_content = f.read()
            exec(script_content)

        # melファイルの場合、ファイル名をクリップボードにコピー
        # TODO: MELウィンドウに貼り付けて実行させるまでやりたい
        if script.endswith('.mel'):
          file_name = script.replace('.mel', '')
          p = subprocess.Popen( ['clip'], stdin=subprocess.PIPE, shell=True )
          p.stdin.write(str.encode(file_name))

def create_plugin():
    """
    プラグインのエントリーポイントとなる関数
    """
    ListScriptsWindow().show()
    ListScriptsWindow().list_scripts()

create_plugin()