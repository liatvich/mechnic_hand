from bpy.types import (PropertyGroup,
                       Bone)
from bpy.props import (StringProperty, 
                        FloatProperty,
                        PointerProperty)

def update_bone_length(self, context):
    context.object.pose.bones[self.name].scale[1] = self.length

def update_bone_angle(self, context):
    context.object.pose.bones[self.name].rotation_euler[0] = self.angle

class MECHANIC_BONES_objectCollection(PropertyGroup):
    name: StringProperty()
    angle: FloatProperty(default=0.0, subtype='ANGLE', update=update_bone_angle) # Angle only indicate the X axis (Y,Z have limit rotation constraint) 
    length: FloatProperty(default=1, min=0.0, soft_min=0, update=update_bone_length)
