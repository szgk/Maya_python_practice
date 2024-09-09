import maya.cmds as cmds
from binascii import a2b_hex as a2b

def fbxasc_to_chr( target_str ):
    return_list = []

    stock = ''
    for var in target_str.split( 'FBXASC' ):
        # 空だったら無視する
        if not var:
            continue
        # 1文字目がアルファベットだったら対象外　return_listに足して次へ。
        if var[0].isalpha():
            return_list.append(var)
            continue

        # 字数が3より多ければ、3文字目までをint変換
        ex_digit = ''
        if len(var)>3:
            ex_digit = var[3:]
            code_int = int(var[:3])
        else:
            code_int = int(var)

        stock +=hex( code_int )
        try:
            return_list.append( a2b(stock.replace('0x','')).decode('utf8') )
        except UnicodeDecodeError:
            continue

        # decode、appendができたらリセット
        stock = ''

        if ex_digit:
            return_list.append(ex_digit)

    return ''.join(return_list)

def create_scroll_window(tex):
    if cmds.window('scrollableDialog', exists=True):
        cmds.deleteUI('scrollableDialog', window=True)

    window = cmds.window('scrollableDialog', title='スクロール可能なダイアログ')

    # スクロールレイアウトを作成
    cmds.scrollLayout(verticalScrollBarAlwaysVisible=True)

    # コラムレイアウト（縦にUI要素を並べる）
    cmds.columnLayout(adjustableColumn=True)

    cmds.scrollField(text=tex, height=500, editable=False, wordWrap=True,)

    # ダイアログにOKボタンを追加
    cmds.button(label='Close', command=lambda *args: cmds.deleteUI(window, window=True))

    # ウィンドウを表示
    cmds.showWindow(window)

def translate_blendshape_garbled():
    selected_object = cmds.ls(selection=True)
    if selected_object:
        # 最初の選択オブジェクトに関連付けられているブレンドシェイプを探す
        blend_shape_nodes = cmds.ls(cmds.listHistory(selected_object[0]), type='blendShape')

        if blend_shape_nodes:
            result = ''
            for blend_shape in blend_shape_nodes:
                # ブレンドシェイプ内のすべてのターゲット名を取得
                blend_shape_targets = cmds.listAttr(blend_shape + '.w', multi=True)
                for i, target in enumerate(blend_shape_targets):
                    translated = fbxasc_to_chr(target)
                    result += translated + '\n' + blend_shape_targets[i] # 翻訳前の文字列を下に表示

            create_scroll_window(result)

        else:
            print('選択されたオブジェクトにはブレンドシェイプがありません。')
    else:
        print('オブジェクトが選択されていません。')

translate_blendshape_garbled()