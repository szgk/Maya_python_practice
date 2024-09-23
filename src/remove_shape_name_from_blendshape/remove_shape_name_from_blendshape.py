import maya.cmds as cmds
import pymel.core as pm
import re
from binascii import a2b_hex as a2b

def translate_blendshape_garbled():
    selected_object = cmds.ls(selection=True)
    if selected_object:
        # 最初の選択オブジェクトに関連付けられているブレンドシェイプを探す
        blend_shape_nodes = cmds.ls(cmds.listHistory(selected_object[0]), type='blendShape')

        if blend_shape_nodes:
            for blend_shape in blend_shape_nodes:
                blendshape_node = pm.PyNode(blend_shape)
                print(blendshape_node)
                listAlias = cmds.aliasAttr(blend_shape, q=True)
                print(listAlias )
                for i, target in enumerate(listAlias):
                    print(target)
                    print(re.search('Shape', target))
                    if type(target) is str and re.search('Shape', target):
                        print(target.replace('Shape', ''))
                        print(blendshape_node.w[i])
                        cmds.aliasAttr(target.replace('Shape', ''), blendshape_node.w[i])
                        # target.setAlias(target.replace('Shape', ''))

        else:
            print('選択されたオブジェクトにはブレンドシェイプがありません。')
    else:
        print('オブジェクトが選択されていません。')

translate_blendshape_garbled()