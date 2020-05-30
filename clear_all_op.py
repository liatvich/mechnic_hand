import bpy
from bpy.types import Operator
from bpy.props import *

# Build skeleton operator
class FC_Clear_All_Operator(bpy.types.Operator):
    """Build Skeleton"""
    bl_idname = "object.clear_all"
    bl_label = "Clear All"
    bl_description = "Clear all mesh and objects"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    # def invoke(self, context, event):
    #     return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        for mesh in bpy.data.meshes:
            bpy.data.meshes.remove(mesh)

        for armature in bpy.data.armatures:
            bpy.data.armatures.remove(armature)

        return {'FINISHED'}
