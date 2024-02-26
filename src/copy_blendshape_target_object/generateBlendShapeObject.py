import pymel.core as pm

def get_blendshapes():
    # 選択されたオブジェクトを取得
    selected_objects = pm.ls(selection=True, dag=True, type='transform')

    if len(selected_objects) == 0 | len(selected_objects) >= 2:
        print('オブジェクトを一つだけ選択してください')
        return
    
    obj = selected_objects[0]
    # コピーを作成した後動かす横幅・高さを取得
    bounding_box = obj.getBoundingBox()
    width = bounding_box.width() + 2
    print(width)
    height = bounding_box.height() + 2
    print(height)

    # 選択されたオブジェクトごとにブレンドシェイプを取得
    history = pm.listHistory(obj)
    blendshapes = pm.ls( history, type = 'blendShape')

    # オブジェクトのブレンドシェイプを取得
    _blendshape = blendshapes[0]

    print(selected_objects)
    print(blendshapes[0])

    targets = blendshapes[0].getTarget()
    
    target_index = 0 # blendシェイプのターゲットのインデックス
    row_index = 0 # 並べる行のインデックス
    column_index = 0 # 並べる列のインデックス

    for target in targets:
        # 並べる列を加算
        column_index+=1

        print(target)
        print(target_index)

        # blendシェイプを設定
        _blendshape.setWeight(target_index, 1)

        # オブジェクトをコピー
        copy_object = pm.duplicate(obj)[0]

        # コピーオブジェクトの名前をblendシェイプのターゲット名に変更
        copy_object.rename(target)

        translation = copy_object.getTranslation()
        print(copy_object)
        print(translation)

        print((target_index + 1) % 20)

        if (target_index + 1) % 20 == 0:
            print('row_index加算')
            # 20個横に並べたら高さを一段ずらす
            row_index += 1
            # 列をリセット
            column_index = 1
        print('rowindex' + str(row_index))

        # index分横幅を動かす
        copy_width = translation[0] + width * column_index
        copy_height = translation[1] + height * -row_index

        print(copy_width, copy_height)

        copy_object.setTranslation([
            copy_width,
            copy_height,
            translation[2]
        ])

        # blendシェイプをリセット、indexを加算、選択を元オブジェクトへ戻す
        _blendshape.setWeight(target_index, 0)
        target_index+=1
        pm.select(selected_objects)
    
        

# プラグインのメイン関数
def main():
    get_blendshapes()

# メイン関数を実行
main()