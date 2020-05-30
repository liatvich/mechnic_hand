import bpy 
import bmesh
from bpy.types import Operator
from bpy.props import *

# Build skeleton operator
class FC_Build_Skeleton_Operator(bpy.types.Operator):
    """Build Skeleton"""
    bl_idname = "armature.build_skeleton"
    bl_label = "Build Skeleton"
    bl_description = "Build Skeleton"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    # def invoke(self, context, event):
    #     return context.window_manager.invoke_props_dialog(self)
    

    def execute(self, context):
        bpy.ops.object.armature_add()
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        arm_obj = context.view_layer.objects.active
        context.active_bone.select=True
        bpy.ops.armature.subdivide(number_cuts=(context.scene.bones_count-1))

        return {'FINISHED'}
