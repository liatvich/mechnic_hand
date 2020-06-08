import bpy
from bpy.types import (PropertyGroup,
                       Bone)
from bpy.props import (StringProperty, 
                        FloatProperty,
                        PointerProperty, 
                        EnumProperty)

# Enum property.
axis_enum = [
    ("X", "x", "", 0),
    ("Y", "y", "", 1),
    ("Z", "z", "", 2),
]

def update_bone_length(self, context):
    context.object.pose.bones[self.name].scale[1] = self.length

def update_bone_angle(self, context):
    a, b, c, axis_variable = [item for item in axis_enum if self.axis in item][0]
    context.object.pose.bones[self.name].rotation_euler[axis_variable] = self.angle_display
    if self.axis == 'X':
        self.angle_x = self.angle_display
    elif self.axis == 'Y':  
        self.angle_y = self.angle_display
    elif self.axis == 'Z':
        self.angle_z = self.angle_display

def update_axis(self, context):
    if self.axis == 'X':
        self.angle_display = self.angle_x

        #TODO: super ugly unify!
        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        try:
            bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        except: 
            pass
        bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = False
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_y = self.angle_y
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_y = self.angle_y
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_z = self.angle_z
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_z = self.angle_z
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'

    elif self.axis == 'Y':
        self.angle_display = self.angle_y

        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        try:
            bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        except: 
            pass
        bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_x = self.angle_x
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_x = self.angle_x
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = False
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_z = self.angle_z
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_z = self.angle_z
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'
    elif self.axis == 'Z':
        self.angle_display = self.angle_z

        # changing constraint
        if context.mode != 'POSE':
            bpy.ops.object.mode_set(mode='POSE')

        try:
            bpy.context.object.pose.bones[self.name].constraints.remove(bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"])
        except: 
            pass
        bpy.context.object.pose.bones[self.name].constraints.new('LIMIT_ROTATION')
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_x = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_x = self.angle_x
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_x = self.angle_x
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_y = True
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].max_y = self.angle_y
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].min_y = self.angle_y
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].use_limit_z = False
        bpy.context.object.pose.bones[self.name].constraints["Limit Rotation"].owner_space = 'LOCAL'
        bpy.context.object.pose.bones[self.name].rotation_mode = 'XYZ'

class MECHANIC_BONES_objectCollection(PropertyGroup):
    name: StringProperty()
    angle_display: FloatProperty(default=0.0, subtype='ANGLE', update=update_bone_angle)
    angle_x: FloatProperty(default=0.0, subtype='ANGLE')
    angle_y: FloatProperty(default=0.0, subtype='ANGLE')
    angle_z: FloatProperty(default=0.0, subtype='ANGLE')
    length: FloatProperty(default=1, min=0.0, soft_min=0, update=update_bone_length)
    axis: EnumProperty(name='axis', items=axis_enum, default='X', update=update_axis)
