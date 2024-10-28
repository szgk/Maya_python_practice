# Maya_python_practice

Maya での Python プログラミングの学習

---

1. [toggle_local_axis_ui](https://github.com/szgk/maya_python_practice/tree/main/src/toggle_local_axis_ui)
   - 選択した全ての joint のローカル軸を表示・表示にする（Maya デフォルト機能では、表示非表示が混ざっている場合、表示しているものは非表示、非表示のものは表示になってしまうので作成
2. [copy_blendshape_target_object](https://github.com/szgk/maya_python_practice/tree/main/src/copy_blendshape_target_object)
   - ブレンドシェイプターゲットを反映させた同名のコピーオブジェクトを作成する
   - ソースメッシュを修正してブレンドシェイプターゲットに反映させるとブレンドシェイプ登録ができなくなったりするのを回避するために作成
3. [translate_blendshape_garbled](https://github.com/szgk/maya_python_practice/tree/main/src/translate_blendshape_garbled)
   - 文字化けしたブレンドシェイプ名を翻訳してコピー可能な形で表示する
4. [reset_all_blendshape_value](https://github.com/szgk/maya_python_practice/tree/main/src/reset_all_blendshape_value)
   - 選択したオブジェクトの Blendshape の値を全て 0 にする
5. [copy_weight_to_same_name_object](https://github.com/szgk/maya_python_practice/tree/main/src/copy_weight_to_same_name_object)
   - 選択した二つのオブジェクトの子オブジェクトで、同じ名前の物があればウェイトコピーする
6. [export_selected_with_joints](https://github.com/szgk/maya_python_practice/tree/main/src/export_selected_with_joints)
   - 選択したスキニングされた複数オブジェクトをオブジェクト名でファイル名にして、入力したディレクトリへ一括書き出し
