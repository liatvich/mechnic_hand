bl_info = {
    "name": "Build Mechanic Hand",
    "author": "Liat V",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "description": "Build Mechanic Hand",
    "location": "View3D",
    "category": "Object",
}

# Blender imports
import bpy
from bpy.props import *
from bpy.types import AddonPreferences
import rna_keymap_ui
from bpy.types import Panel
from . mechanic_bones_op import MECHANIC_BONES_OT_actions
from . mechanic_bones_panel import MECHANIC_BONES_UL_items
from . mechanic_bones_panel import MECHANIC_BONES_PT_ObjectList
from . mechanic_bones_objectCollection import MECHANIC_BONES_objectCollection
from . import_stl_op import Import_STL_Mechanic_Operator
from . clear_all_op import FC_Clear_All_Operator

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
    MECHANIC_BONES_OT_actions,
    MECHANIC_BONES_UL_items,
    MECHANIC_BONES_PT_ObjectList,
    MECHANIC_BONES_objectCollection,
    Import_STL_Mechanic_Operator,
    FC_Clear_All_Operator,
)     
    
def register():
    for c in classes:
        bpy.utils.register_class(c)
   
    # add keymap entry
    kc = bpy.context.window_manager.keyconfigs.addon
    kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    # Custom scene properties
    bpy.types.Scene.mechanic_bones = bpy.props.CollectionProperty(type=MECHANIC_BONES_objectCollection)
    bpy.types.Scene.mechanic_bones_index = bpy.props.IntProperty()
    bpy.types.Scene.mechanic_hand_armature = bpy.props.PointerProperty(type=bpy.types.Armature)
    
def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)

    # remove keymap entry
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)

    addon_keymaps.clear()

    del bpy.types.Scene.mechanic_bones
    del bpy.types.Scene.mechanic_bones_index
    del bpy.types.Scene.mechanic_hand_armature

#TODO: separate to logic folder
#TODO: change name conventions
#TODO: mesh deform?
#TODO: separate to functions
#TODO: watch the rest of blender videos
#TODO: Understand how to build mesh from a CAD file
#TODO: understand how to parent mesh to bones
#TODO: understand how to rigify 
#TODO: understand how to rigify the created hand shape
#TODO: set the position of the end bone - with innverse kinematics get the angles (rotation of the other skeleton bones)
#TODO: !! Create mechanic hand instread of with constraints with IK (elbow example)
#---------------------------------
#TODO: quick win - add clear all button
#TODO: enable the remove bone operation
#TODO: autocomplete doesn't load fast :(
# bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1) - 
#       operation that paint action in blender to see progress
