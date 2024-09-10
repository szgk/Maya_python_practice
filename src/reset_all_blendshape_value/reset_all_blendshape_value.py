import maya.cmds as cmds
import pymel.core as pm

def reset_all_blendshape_value():
    selected_object = cmds.ls(selection=True)
    if selected_object:
        # ブレンドシェイプノードを取得
        blend_shape_nodes = pm.ls(pm.listHistory(selected_object), type='blendShape')
        for blend_shape_node in blend_shape_nodes:
            # ブレンドシェイプターゲットのリストを取得
            targets = blend_shape_node.listAttr(multi=True, keyable=True)
            # 各ターゲットの値を0に設定
            for i, target in enumerate(targets):
                blend_shape_node.setWeight(i, 0)

        else:
            print('選択されたオブジェクトにはブレンドシェイプがありません。')
    else:
        print('オブジェクトが選択されていません。')

reset_all_blendshape_value()