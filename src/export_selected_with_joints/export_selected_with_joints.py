import pymel.core as pm

def export_selected_with_joints():
    # テキスト入力ダイアログでエクスポート先ディレクトリを入力
    result = pm.promptDialog(
        title='エクスポート先ディレクトリ',
        message='エクスポート先ディレクトリを入力してください:',
        button=['OK', 'キャンセル'],
        defaultButton='OK',
        cancelButton='キャンセル',
        dismissString='キャンセル'
    )
    
    # キャンセルされた場合
    if result == 'キャンセル':
        pm.warning("エクスポートがキャンセルされました。")
        return

    # 入力されたディレクトリパスを取得
    output_directory = pm.promptDialog(query=True, text=True)

    # 選択したオブジェクトを取得
    selected_objects = pm.selected()

    if not selected_objects:
        pm.warning("エクスポートするオブジェクトを選択してください。")
        return

    # 各オブジェクトを個別にエクスポート
    for obj in selected_objects:
        # オブジェクト名を取得して出力パスを生成
        object_name = obj.name()
        output_path = f"{output_directory}/{object_name}.fbx".replace("|", "")
        
        # オブジェクトのスキンクラスターを取得
        skin_clusters = pm.listHistory(obj, type='skinCluster')
        
        if not skin_clusters:
            pm.warning(f"{object_name} にはスキンクラスターがありません。")
            continue

        # スキンクラスターから影響を与えるジョイントを取得
        joints = set()
        for skin_cluster in skin_clusters:
            joints.update(pm.skinCluster(skin_cluster, query=True, influence=True))

        # オブジェクトとそのジョイントを選択
        pm.select([obj] + list(joints), replace=True)

        # エクスポート実行
        pm.exportSelected(output_path, type='FBX export', force=True)
        print(f"エクスポートが完了しました: {output_path}")

    # 選択解除
    pm.select(clear=True)
    print("すべてのオブジェクトのエクスポートが完了しました。")

# スクリプトの実行
export_selected_with_joints()
