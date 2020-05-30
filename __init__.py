bl_info = {
    "name": "Build Skeleton",
    "author": "Liat V",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Build Skeleton",
    "location": "View3D",
    "category": "Object",
}

# Blender imports
import bpy
from bpy.props import *
from bpy.types import AddonPreferences
import rna_keymap_ui
from bpy.types import Panel
from . build_skeleton_panel import Build_Skeleton_Panel
from . build_skeleton_op import FC_Build_Skeleton_Operator
from . clear_all_op import FC_Clear_All_Operator
# from . mechanic_bone_panel import Mechanic_Bone_Panel

# Scene properties
#TODO: I think this should be moved elsewhere
bpy.types.Scene.bones_count = bpy.props.IntProperty(
        name="number of bones",
        description="choosing the number of connected bones",
        default=3,
        min=1,
        max=10,
    )

# Addon preferences
class FC_AddonPreferences(AddonPreferences):
    bl_idname = __name__
    
    def draw(self, context):
        wm = bpy.context.window_manager 
        km_items = wm.keyconfigs.addon.keymaps['3D View'].keymap_items         

addon_keymaps = []

classes = (
    FC_Clear_All_Operator,
    FC_Build_Skeleton_Operator,
    Build_Skeleton_Panel,
    # Mechanic_Bone_Panel,
)     
    
def register():
    for c in classes:
        bpy.utils.register_class(c)
   
    # add keymap entry
    kc = bpy.context.window_manager.keyconfigs.addon
    kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    bpy.types.Object.expanded = bpy.props.BoolProperty(default=True)
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    del bpy.types.Object.expanded
    addon_keymaps.clear()

#TODO: separate to logic folder
#TODO: change name conventions
#TODO: mesh deform?