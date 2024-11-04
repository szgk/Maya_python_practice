import pymel.core as pm
import maya.cmds as cmds

def rename_blendshape_target_ui():
    # UIがすでに存在している場合は削除
    if pm.window("renameBlendshapeTargetWindow", exists=True):
        pm.deleteUI("renameBlendshapeTargetWindow")
    
    # UIの作成
    window = pm.window("renameBlendshapeTargetWindow", title="Blendshape Target Renamer", widthHeight=(300, 150))
    pm.columnLayout(adjustableColumn=True)
    
    # 消したい文字列の入力欄
    pm.text(label="消したい文字列（ターゲット名）:")
    target_text_field = pm.textField()
    
    # 新しい名前の入力欄
    pm.text(label="新しい名前:")
    new_text_field = pm.textField()
    
    # 実行ボタン
    pm.button(label="ターゲット名を変更", command=lambda *args: rename_blendshape_target_from_ui(target_text_field, new_text_field))
    
    pm.showWindow(window)

def rename_blendshape_target_from_ui(target_text_field, new_text_field):
    # 入力フィールドから文字列を取得
    target_text = pm.textField(target_text_field, query=True, text=True)
    new_text = pm.textField(new_text_field, query=True, text=True)

    # 選択されているオブジェクトを取得
    selected_objects = pm.selected()
    
    if not selected_objects:
        pm.warning("オブジェクトを選択してください。")
        return

    for obj in selected_objects:
        # オブジェクトにブレンドシェイプが存在するか確認
        blendshapes = pm.listHistory(obj, type='blendShape')
        if not blendshapes:
            pm.warning(f"{obj}にはブレンドシェイプが設定されていません。")
            continue
        
        # 各ブレンドシェイプのターゲット（キー名）を変更
        for blendshape in blendshapes:
            # ブレンドシェイプのターゲット（ウェイト属性名）を取得
            targets = blendshape.listAttr(multi=True, string="weight")  # "weight"アトリビュートがターゲット名のリスト

            for target in targets:
                target_name = target.getAlias()
                
                if target_text in target_name:
                    # 新しいターゲット名を作成
                    new_target_name = target_name.replace(target_text, new_text)
                    
                    # ターゲット名を新しいエイリアスに設定
                    cmds.aliasAttr(new_target_name, f"{blendshape}.{target_name}")
                    print(f"{target_name} を {new_target_name} に変更しました。")
                else:
                    print(f"{target_name} に '{target_text}' は含まれていません。")

# 使用方法
rename_blendshape_target_ui()
