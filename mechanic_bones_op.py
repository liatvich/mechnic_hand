import bpy
from bpy.types import Operator
from bpy.props import *

class MECHANIC_BONES_OT_actions(bpy.types.Operator):
    """Mechanic Bones list: up and down, add and remove operations"""
    bl_idname = "mechanic_bones.list_action"
    bl_label = "List Actions"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_description = "Mechanic Bones list: up and down, add and remove operations"
    bl_options = {'REGISTER', 'UNDO'} #TODO: did I implement UNDO?

    action: bpy.props.EnumProperty(
        items=(
            ('REMOVE', "Remove", ""),
            ('ADD', "Add", "")))

    @classmethod
    def poll(cls, context):
        return True
    
    def invoke(self, context, event):
        scene = context.scene
        selected_bone_index = scene.mechanic_bones_index

        try:
            selected_bone = scene.mechanic_bones[selected_bone_index]
        except IndexError:
            pass
        else:
            if self.action == 'REMOVE':
                # Panel list UI
                selected_bone = scene.mechanic_bones[scene.mechanic_bones_index]
                info = 'selected_bone %s removed from scene' % (selected_bone.name)
                scene.mechanic_bones.remove(selected_bone_index)
                if scene.mechanic_bones_index == 0:
                    scene.mechanic_bones_index = 0
                else:
                    scene.mechanic_bones_index -= 1
                self.report({'INFO'}, info)

        if self.action == 'ADD':
            # Panel list UI
            selected_bone = scene.mechanic_bones.add()
            selected_bone.id = len(scene.mechanic_bones)
            scene.mechanic_bones_index = (len(scene.mechanic_bones)-1)

            if scene.mechanic_bones_index == 0:
                # adding armature bone object - the armature that bones are added to
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))
                arm_index = bpy.data.armatures.__len__() - 1
                bpy.data.armatures[arm_index].display_type = 'BBONE'
                scene.mechanic_hand_armature = bpy.data.armatures[arm_index]
                selected_bone.name = bpy.data.armatures[arm_index].edit_bones[0].name

                # setting the created bone as active
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index]

                # adding rotation constraint
                # unify to function ---1
                if context.mode != 'POSE':
                    bpy.ops.object.mode_set(mode='POSE')
    
                bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].use_limit_z = True
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].use_limit_y = True
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
                bpy.context.object.pose.bones[selected_bone.name].rotation_mode = 'XYZ'

            if scene.mechanic_bones_index > 0:
                if context.mode != 'EDIT':
                    bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.armature.bone_primitive_add()
                selected_bone.name = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index].name
                bpy.ops.armature.select_all(action='DESELECT')

                # parenting to previous node
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index].select = True
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index - 1].select = True
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index - 1]
                bpy.ops.armature.parent_set(type='CONNECTED')

                # setting the created bone as active
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index]

                # adding rotation constraint
                # unify to function ---1
                if context.mode != 'POSE':
                    bpy.ops.object.mode_set(mode='POSE')
                
                bpy.ops.pose.constraint_add(type='LIMIT_ROTATION')
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].use_limit_z = True
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].use_limit_y = True
                bpy.context.object.pose.bones[selected_bone.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
                bpy.context.object.pose.bones[selected_bone.name].rotation_mode = 'XYZ'


        return {"FINISHED"}

# TODO: add constants
