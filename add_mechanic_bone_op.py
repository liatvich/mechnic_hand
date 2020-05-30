import bpy
from bpy.types import Operator
from bpy.props import *

# Add Mechanic Bone Operation
# todo - add a plus button icon
class Add_Mechanic_Bone_Operation(bpy.types.Operator):
    """Add Mechanic Bone Operation"""
    bl_idname = "armature.add_mechanic_bone" 
    bl_label = "Add new mechanic bone"
    bl_description = "Adding another bone to the mechanic structure."
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
        context.active_bone.select=True
        # bpy.data.armatures['mechanical_arm_'+index].show_axes --- to see the axis the armature is 
        # bpy.data.armatures['mechanical_arm_'+index].display_type ---
            # change the display type to b-bone

        # moving

        # row = layout.row()
        # add the bone with limit rotation constraint - can oly move in in the X axis  - to local space! 
        # Check what it the last bone (save all reference bones in a local array) 
        # make the last bone the perant of this node



        return {'FINISHED'}
