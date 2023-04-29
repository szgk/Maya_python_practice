import pymel.core as pm

class ToggleLocalAxisUI(object):
    def __init__(self):
        self.window_name = 'ToggleLocalAxisUI'
    
    def create(self):
        if pm.window(self.window_name, exists=True):
            pm.deleteUI(self.window_name)
        with pm.window(self.window_name, title='Toggle Local Axis') as self.window:
            with pm.columnLayout(adj=True):
                pm.text(label='Select bone(s) and toggle their local axis:')
                pm.separator()
                with pm.rowLayout(nc=2):
                    self.show_btn = pm.button(label='Show Local Axis', command=self.show_local_axis)
                    self.hide_btn = pm.button(label='Hide Local Axis', command=self.hide_local_axis)
    
    def show_local_axis(self, *args):
        sel = pm.selected(type='joint')
        if not sel:
            pm.warning('Please select at least one joint.')
            return
        for joint in sel:
            joint.displayLocalAxis.set(True)
    
    def hide_local_axis(self, *args):
        sel = pm.selected(type='joint')
        if not sel:
            pm.warning('Please select at least one joint.')
            return
        for joint in sel:
            joint.displayLocalAxis.set(False)
    
    def show(self):
        self.create()
        self.window.show()
    
toggle_local_axis_ui = ToggleLocalAxisUI()
toggle_local_axis_ui.show()

