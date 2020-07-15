import bpy
from bpy.types import Operator
from bpy.props import *
import collections
import math
import mathutils

# Create bones
class FC_Geneate_Bones_Operation(bpy.types.Operator):
    """generate bones"""
    bl_idname = "mechanic_bones.generate_bones"
    bl_label = "generate Bones"
    bl_description = "generate bones from a pre define meshes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    # can be static
    @classmethod 
    def get_center(self, ref_object):
        vcos = [ ref_object.matrix_world @ v.co for v in ref_object.data.vertices ]
        findCenter = lambda l: ( max(l) + min(l) ) / 2
        x,y,z  = [ [ v[i] for v in vcos ] for i in range(3) ]
        center = [ findCenter(axis) for axis in [x,y,z] ]
        return( center )

    
    # def get_distance(self, first_point, seconde_point):
    #     return math.sqrt((first_point[0] - seconde_point[0]) ** 2 + (first_point[1] - seconde_point[1]) ** 2 + (first_point[2] - seconde_point[2]) ** 2)

    # def get_angle(self, first_point, seconde_point):
    #     return math.sqrt((first_point[0] - seconde_point[0]) ** 2 + (first_point[1] - seconde_point[1]) ** 2 + (first_point[2] - seconde_point[2]) ** 2)

    def execute(self, context):
        bones_to_generate = {}
        for current_object in bpy.data.objects:
            if('end' in current_object.name or 'start' in current_object.name):
                bone_index = int(current_object.name.split('_')[0].split('Bone')[1])
                if(bone_index not in bones_to_generate):
                    bones_to_generate[bone_index] = {}
                bones_to_generate[bone_index][current_object.name.split('_')[1]] = self.get_center(current_object)
        
        ordered_bones_to_generate = collections.OrderedDict(sorted(bones_to_generate.items()))

        for bone_index in ordered_bones_to_generate:
            # ordered_bones_to_generate[bone_index]['distance'] = self.get_distance(ordered_bones_to_generate[bone_index]['start'], ordered_bones_to_generate[bone_index]['end'])
            # ordered_bones_to_generate[bone_index]['angle'] = self.get_angle(ordered_bones_to_generate[bone_index]['start'], ordered_bones_to_generate[bone_index]['end'])


            scene = context.scene
            # Panel list UI
            selected_bone = scene.mechanic_bones.add()
            selected_bone.id = len(scene.mechanic_bones)
            scene.mechanic_bones_index = (len(scene.mechanic_bones)-1)

            if scene.mechanic_bones_index == 0:
                # adding armature bone object - the armature that bones are added to
                if context.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.armature_add(enter_editmode=True, location=(0,0,0))
                
                arm_index = bpy.data.armatures.__len__() - 1
                scene.mechanic_hand_armature = bpy.data.armatures[arm_index]
                selected_bone.name = bpy.data.armatures[arm_index].edit_bones[0].name

                # setting the created bone as active
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index]

                # setting the bone length 
                if context.mode != 'EDIT':
                    bpy.ops.object.mode_set(mode='EDIT')

                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active.head = mathutils.Vector((ordered_bones_to_generate[bone_index]['start'][0],ordered_bones_to_generate[bone_index]['start'][1],ordered_bones_to_generate[bone_index]['start'][2]))
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active.tail = mathutils.Vector((ordered_bones_to_generate[bone_index]['end'][0],ordered_bones_to_generate[bone_index]['end'][1],ordered_bones_to_generate[bone_index]['end'][2]))

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
                bpy.ops.armature.parent_set(type='OFFSET')

                # setting the created bone as active
                bpy.ops.armature.select_all(action='DESELECT')
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active = bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones[scene.mechanic_bones_index]

                # setting the bone length 
                if context.mode != 'EDIT':
                    bpy.ops.object.mode_set(mode='EDIT')

                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active.head = mathutils.Vector((ordered_bones_to_generate[bone_index]['start'][0],ordered_bones_to_generate[bone_index]['start'][1],ordered_bones_to_generate[bone_index]['start'][2]))
                bpy.data.armatures[scene.mechanic_hand_armature.name].edit_bones.active.tail = mathutils.Vector((ordered_bones_to_generate[bone_index]['end'][0],ordered_bones_to_generate[bone_index]['end'][1],ordered_bones_to_generate[bone_index]['end'][2]))


        return {'FINISHED'}
