# スライダーで指定した位置に球体を作成するwindow
import maya.cmds as cmds

x_slider_name = ""
y_slider_name = ""
z_slider_name = ""

def createPolySphere(*args):
    cmds.polySphere(r=1, sx=20, ax=(0, 1, 0), cuv=2, ch=1)
    x_value = cmds.floatSliderGrp(x_slider_name, q=True, value=True)
    y_value = cmds.floatSliderGrp(y_slider_name, q=True, value=True)
    z_value = cmds.floatSliderGrp(z_slider_name, q=True, value=True)
    cmds.move(x_value, y_value, z_value, r=True)

window = cmds.window(title="Create Sphere", iconName='Create Sphere', widthHeight=(200, 55))
cmds.columnLayout(adjustableColumn=True)

x_slider_name = cmds.floatSliderGrp(label='Move X', field=True, minValue=-10.0, maxValue=10.0, value=0.0)
y_slider_name = cmds.floatSliderGrp(label='Move Y', field=True, minValue=-10.0, maxValue=10.0, value=0.0)
z_slider_name = cmds.floatSliderGrp(label='Move Z', field=True, minValue=-10.0, maxValue=10.0, value=0.0)
cmds.button(label='Create Polygon Sphere', command=createPolySphere)
cmds.button(label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)'))
cmds.setParent('..')
cmds.showWindow(window)
