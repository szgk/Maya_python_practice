import pymel.core as pm
import re

def copy_weight_to_same_name_object():
    # 現在の選択を取得
    selection = pm.ls(selection=True)
    
    # 2つのオブジェクトが選択されていることを確認
    if len(selection) != 2:
        pm.error("2つの親オブジェクトを選択してください。1つ目が元オブジェクト、2つ目がターゲットオブジェクトです。")
        return
    
    # 最初に選択されたオブジェクトの子供を取得
    children = pm.listRelatives(selection[0], children=True, fullPath=True)
    children2 = pm.listRelatives(selection[1], children=True, fullPath=True)
    
    if not children:
        pm.warning(f"{selection[0]}には子オブジェクトがありません")
        return None
    
    if not children2:
        pm.warning(f"{selection[1]}には子オブジェクトがありません")
        return None
    
    print(f"{selection[0]}の子オブジェクト: {children}")
    print(f"{selection[1]}の子オブジェクト: {children2}")
    
    for source_obj in children:
        obj_name = re.sub(r'.*\|', '', source_obj.name())
        print(obj_name)
        resultArr = [s for s in children2 if re.search(fr'{obj_name}$', s.name())]

        if len(resultArr) == 0:
            pm.warning(f"{selection[1]}には{obj_name}オブジェクトがありません")
            continue

        target_obj = resultArr[0]
        print(f'ターゲット{target_obj}')

        source_skin_cluster = pm.mel.findRelatedSkinCluster(source_obj)

        if not source_skin_cluster:
            pm.error(f"元オブジェクト {source_obj} に関連する skinCluster が見つかりませんでした。")
            continue
        
        target_skin_cluster = pm.mel.findRelatedSkinCluster(target_obj)

        pm.copySkinWeights(
            sourceSkin=source_skin_cluster, 
            destinationSkin=target_skin_cluster, 
            noMirror=True,
            surfaceAssociation='closestPoint',
            influenceAssociation=('name', 'closestJoint', 'oneToOne')
        )
        

        # joints = pm.skinCluster(source_skin_cluster, query=True, influence=True)
        # target_skin_cluster = pm.skinCluster(joints, target_obj, toSelectedBones=True)
        # pm.select(clear=True)

        # source_skin_cluster_node = pm.PyNode(source_skin_cluster)
        # target_skin_cluster_node = pm.PyNode(target_skin_cluster)

        # vertices = pm.PyNode(source_obj).vtx

        # print(source_skin_cluster_node)
        # print(target_skin_cluster_node)

        # # ウェイトのコピー
        # for i, vertex in enumerate(vertices):
        #     print(vertex)
        #     print(type(i))
        #     print(type(vertex))
        #     # 元のオブジェクトのウェイトを取得
        #     source_weights = source_skin_cluster_node.getWeights(source_obj, vertex)
            
        #     # 対応するターゲットオブジェクトの頂点を取得
        #     target_vertex = target_obj.vtx[vertex.index()]
            
        #     # ウェイトをターゲットオブジェクトの頂点に適用
        #     target_skin_cluster_node.setWeights(target_obj, target_vertex, source_skin_cluster_node.getInfluence(), source_weights)

        print(f"ウェイトが {source_obj} から {target_obj} にコピーされました。")


# スクリプトを実行
copy_weight_to_same_name_object()