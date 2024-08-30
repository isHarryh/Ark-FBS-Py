# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class enum__Torappu_AbnormalFlag(object):
    STUNNED = 0
    SP_RECOVER_STOPPED = 1
    TARGET_FREE = 2
    BLOCK_FREE = 3
    HIDDEN = 4
    INVINCIBLE = 5
    UNDEADABLE = 6
    HEAL_FREE = 7
    UNBALANCE_IMMUNE = 8
    INVISIBLE = 9
    UNUSED_PLACEHOLDER_1 = 10
    DISARMED = 11
    SILENCED = 12
    UNMOVABLE = 13
    UNUSED_PLACEHOLDER_2 = 14
    ALLY_TARGET_FREE = 15
    FROZEN = 16
    CAMOUFLAGE = 17
    FORCE_DISARMED = 18
    STUNNED_NO_AMPLIFY_DAMAGE = 19
    DISABLE_COMBAT = 20
    ELEMENT_FREE_ALL = 21
    UNMOVABLE_PRIVATE = 22
    COLD = 23
    SKILL_NOT_ACTIVATABLE = 24
    LEVITATE = 25
    DURANCE = 26
    NOT_WITHDRAWABLE = 27
    OUT_OF_GROUND = 28
    SP_MODIFY_STOPPED = 29
    ANTI_STATUS_RESISTABLE = 30
    DISARMED_COMBAT = 31
    TOWER_TARGET_FREE = 32
    FEARED = 33
    SKILL_ACTIVABLE_IN_ABNORMAL = 34
    E_NUM = 35


class enum__Torappu_AbnormalCombo(object):
    SLEEPING = 0
    SHELTERING = 1
    E_NUM = 2


class enum__Torappu_AttributeType(object):
    MAX_HP = 0
    ATK = 1
    DEF = 2
    MAGIC_RESISTANCE = 3
    COST = 4
    BLOCK_CNT = 5
    MOVE_SPEED = 6
    ATTACK_SPEED = 7
    BASE_ATTACK_TIME = 8
    RESERVED_0 = 9
    RESERVED_1 = 10
    RESERVED_2 = 11
    RESERVED_3 = 12
    HP_RECOVERY_PER_SEC = 13
    SP_RECOVERY_PER_SEC = 14
    ABILITY_RANGE_FORWARD_EXTEND = 15
    MAX_DEPLOY_COUNT = 16
    DEF_PENETRATE = 17
    MAGIC_RESIST_PENETRATE = 18
    HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO = 19
    TAUNT_LEVEL = 20
    RESPAWN_TIME = 21
    MAX_DECK_STACK_CNT = 22
    MASS_LEVEL = 23
    BASE_FORCE_LEVEL = 24
    DEF_PENETRATE_FIXED = 25
    ONE_MINUS_STATUS_RESISTANCE = 26
    MAGIC_RESIST_PENETRATE_FIXED = 27
    MAX_EP = 28
    EP_RECOVERY_PER_SEC = 29
    SP_RECOVER_RATIO = 30
    EP_DAMAGE_RESISTANCE = 31
    EP_RESISTANCE = 32
    DAMAGE_HITRATE_PHYSICAL = 33
    DAMAGE_HITRATE_MAGICAL = 34
    E_NUM = 35


class enum__Torappu_AttributeModifierData_AttributeModifier_FormulaItemType(object):
    ADDITION = 0
    MULTIPLIER = 1
    FINAL_ADDITION = 2
    FINAL_SCALER = 3


class enum__Torappu_BuffData_StatusResistable(object):
    NO = 0
    YES = 1
    AUTOMATIC = 2


class enum__Torappu_BuffData_OverrideType(object):
    DEFAULT = 0
    STACK = 1
    UNIQUE = 2
    EXTEND = 3
    EXTEND_TIME = 4


class enum__Torappu_BuffData_OnEventPriority(object):
    LOWEST_PRIORITY = -3000
    LOWER_PRIORITY = -2000
    LOW_PRIORITY = -1000
    DEFAULT = 0
    HIGH_PRIORITY = 1000
    HIGHER_PRIORITY = 2000


class enum__Torappu_LifeType(object):
    IMMEDIATELY = 0
    LIMITED = 1
    INFINITY = 2


class clz_Torappu_AttributeModifierData_AttributeModifier(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = clz_Torappu_AttributeModifierData_AttributeModifier()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsclz_Torappu_AttributeModifierData_AttributeModifier(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # clz_Torappu_AttributeModifierData_AttributeModifier
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # clz_Torappu_AttributeModifierData_AttributeModifier
    def AttributeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_AttributeModifierData_AttributeModifier
    def FormulaItem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_AttributeModifierData_AttributeModifier
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # clz_Torappu_AttributeModifierData_AttributeModifier
    def LoadFromBlackboard(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_AttributeModifierData_AttributeModifier
    def FetchBaseValueFromSourceEntity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def clz_Torappu_AttributeModifierData_AttributeModifierStart(builder):
    builder.StartObject(5)

def clz_Torappu_AttributeModifierData_AttributeModifierAddAttributeType(builder, attributeType):
    builder.PrependInt32Slot(0, attributeType, 0)

def clz_Torappu_AttributeModifierData_AttributeModifierAddFormulaItem(builder, formulaItem):
    builder.PrependInt32Slot(1, formulaItem, 0)

def clz_Torappu_AttributeModifierData_AttributeModifierAddValue(builder, value):
    builder.PrependFloat32Slot(2, value, 0.0)

def clz_Torappu_AttributeModifierData_AttributeModifierAddLoadFromBlackboard(builder, loadFromBlackboard):
    builder.PrependBoolSlot(3, loadFromBlackboard, 0)

def clz_Torappu_AttributeModifierData_AttributeModifierAddFetchBaseValueFromSourceEntity(builder, fetchBaseValueFromSourceEntity):
    builder.PrependBoolSlot(4, fetchBaseValueFromSourceEntity, 0)

def clz_Torappu_AttributeModifierData_AttributeModifierEnd(builder):
    return builder.EndObject()



class clz_Torappu_AttributeModifierData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = clz_Torappu_AttributeModifierData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsclz_Torappu_AttributeModifierData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # clz_Torappu_AttributeModifierData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # clz_Torappu_AttributeModifierData
    def AbnormalFlags(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalFlagsAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalFlagsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalFlagsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # clz_Torappu_AttributeModifierData
    def AbnormalImmunes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalImmunesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalImmunesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalImmunesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # clz_Torappu_AttributeModifierData
    def AbnormalAntis(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalAntisAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalAntisLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalAntisIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # clz_Torappu_AttributeModifierData
    def AbnormalCombos(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalCombosAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalCombosLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalCombosIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # clz_Torappu_AttributeModifierData
    def AbnormalComboImmunes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalComboImmunesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalComboImmunesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AbnormalComboImmunesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

    # clz_Torappu_AttributeModifierData
    def AttributeModifiers(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = clz_Torappu_AttributeModifierData_AttributeModifier()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # clz_Torappu_AttributeModifierData
    def AttributeModifiersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_AttributeModifierData
    def AttributeModifiersIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def clz_Torappu_AttributeModifierDataStart(builder):
    builder.StartObject(6)

def clz_Torappu_AttributeModifierDataAddAbnormalFlags(builder, abnormalFlags):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(abnormalFlags), 0)

def clz_Torappu_AttributeModifierDataStartAbnormalFlagsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataAddAbnormalImmunes(builder, abnormalImmunes):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(abnormalImmunes), 0)

def clz_Torappu_AttributeModifierDataStartAbnormalImmunesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataAddAbnormalAntis(builder, abnormalAntis):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(abnormalAntis), 0)

def clz_Torappu_AttributeModifierDataStartAbnormalAntisVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataAddAbnormalCombos(builder, abnormalCombos):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(abnormalCombos), 0)

def clz_Torappu_AttributeModifierDataStartAbnormalCombosVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataAddAbnormalComboImmunes(builder, abnormalComboImmunes):
    builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(abnormalComboImmunes), 0)

def clz_Torappu_AttributeModifierDataStartAbnormalComboImmunesVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataAddAttributeModifiers(builder, attributeModifiers):
    builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(attributeModifiers), 0)

def clz_Torappu_AttributeModifierDataStartAttributeModifiersVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_AttributeModifierDataEnd(builder):
    return builder.EndObject()



class clz_Torappu_Blackboard_DataPair(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = clz_Torappu_Blackboard_DataPair()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsclz_Torappu_Blackboard_DataPair(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # clz_Torappu_Blackboard_DataPair
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # clz_Torappu_Blackboard_DataPair
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_Blackboard_DataPair
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # clz_Torappu_Blackboard_DataPair
    def ValueStr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def clz_Torappu_Blackboard_DataPairStart(builder):
    builder.StartObject(3)

def clz_Torappu_Blackboard_DataPairAddKey(builder, key):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)

def clz_Torappu_Blackboard_DataPairAddValue(builder, value):
    builder.PrependFloat32Slot(1, value, 0.0)

def clz_Torappu_Blackboard_DataPairAddValueStr(builder, valueStr):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(valueStr), 0)

def clz_Torappu_Blackboard_DataPairEnd(builder):
    return builder.EndObject()



class clz_Torappu_BuffData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = clz_Torappu_BuffData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsclz_Torappu_BuffData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # clz_Torappu_BuffData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # clz_Torappu_BuffData
    def Attributes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = clz_Torappu_AttributeModifierData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # clz_Torappu_BuffData
    def BuffKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def LoadFromDb(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsDurableBuff(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsDamageMissable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsSilenceable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsStunnable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsFreezable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def IsLevitatable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def StatusResistable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def TemplateKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def DisableOverride(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def OverrideKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def OverrideType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def MaxStackCnt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def RefreshRemainingTimeWhenStackMax(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def ClearAllStackCntWhenTimeUp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def MaxValidStackCnt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def OverrideEffectKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def OverrideOnEventPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def OnEventPriority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def AudioSignal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def LifeTimeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def TakeSnapshotWhenExtend(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def DurationKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # clz_Torappu_BuffData
    def LifeTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # clz_Torappu_BuffData
    def TriggerLifeType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def TriggerCnt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def TriggerInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # clz_Torappu_BuffData
    def WaitFirstTriggerInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def FirstTriggerInterval(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # clz_Torappu_BuffData
    def Priority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # clz_Torappu_BuffData
    def PriorityBbkeys(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # clz_Torappu_BuffData
    def PriorityBbkeysLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_BuffData
    def PriorityBbkeysIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        return o == 0

    # clz_Torappu_BuffData
    def StripBlackboardParamsWithBuffKey(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # clz_Torappu_BuffData
    def Blackboard(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = clz_Torappu_Blackboard_DataPair()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # clz_Torappu_BuffData
    def BlackboardLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_BuffData
    def BlackboardIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        return o == 0

def clz_Torappu_BuffDataStart(builder):
    builder.StartObject(35)

def clz_Torappu_BuffDataAddAttributes(builder, attributes):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(attributes), 0)

def clz_Torappu_BuffDataAddBuffKey(builder, buffKey):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(buffKey), 0)

def clz_Torappu_BuffDataAddLoadFromDb(builder, loadFromDb):
    builder.PrependBoolSlot(2, loadFromDb, 0)

def clz_Torappu_BuffDataAddIsDurableBuff(builder, isDurableBuff):
    builder.PrependBoolSlot(3, isDurableBuff, 0)

def clz_Torappu_BuffDataAddIsDamageMissable(builder, isDamageMissable):
    builder.PrependBoolSlot(4, isDamageMissable, 0)

def clz_Torappu_BuffDataAddIsSilenceable(builder, isSilenceable):
    builder.PrependBoolSlot(5, isSilenceable, 0)

def clz_Torappu_BuffDataAddIsStunnable(builder, isStunnable):
    builder.PrependBoolSlot(6, isStunnable, 0)

def clz_Torappu_BuffDataAddIsFreezable(builder, isFreezable):
    builder.PrependBoolSlot(7, isFreezable, 0)

def clz_Torappu_BuffDataAddIsLevitatable(builder, isLevitatable):
    builder.PrependBoolSlot(8, isLevitatable, 0)

def clz_Torappu_BuffDataAddStatusResistable(builder, statusResistable):
    builder.PrependUint8Slot(9, statusResistable, 0)

def clz_Torappu_BuffDataAddTemplateKey(builder, templateKey):
    builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(templateKey), 0)

def clz_Torappu_BuffDataAddDisableOverride(builder, disableOverride):
    builder.PrependBoolSlot(11, disableOverride, 0)

def clz_Torappu_BuffDataAddOverrideKey(builder, overrideKey):
    builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(overrideKey), 0)

def clz_Torappu_BuffDataAddOverrideType(builder, overrideType):
    builder.PrependInt32Slot(13, overrideType, 0)

def clz_Torappu_BuffDataAddMaxStackCnt(builder, maxStackCnt):
    builder.PrependInt32Slot(14, maxStackCnt, 0)

def clz_Torappu_BuffDataAddRefreshRemainingTimeWhenStackMax(builder, refreshRemainingTimeWhenStackMax):
    builder.PrependBoolSlot(15, refreshRemainingTimeWhenStackMax, 0)

def clz_Torappu_BuffDataAddClearAllStackCntWhenTimeUp(builder, clearAllStackCntWhenTimeUp):
    builder.PrependBoolSlot(16, clearAllStackCntWhenTimeUp, 0)

def clz_Torappu_BuffDataAddMaxValidStackCnt(builder, maxValidStackCnt):
    builder.PrependInt32Slot(17, maxValidStackCnt, 0)

def clz_Torappu_BuffDataAddOverrideEffectKey(builder, overrideEffectKey):
    builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(overrideEffectKey), 0)

def clz_Torappu_BuffDataAddOverrideOnEventPriority(builder, overrideOnEventPriority):
    builder.PrependBoolSlot(19, overrideOnEventPriority, 0)

def clz_Torappu_BuffDataAddOnEventPriority(builder, onEventPriority):
    builder.PrependInt32Slot(20, onEventPriority, 0)

def clz_Torappu_BuffDataAddAudioSignal(builder, audioSignal):
    builder.PrependUOffsetTRelativeSlot(21, flatbuffers.number_types.UOffsetTFlags.py_type(audioSignal), 0)

def clz_Torappu_BuffDataAddLifeTimeType(builder, lifeTimeType):
    builder.PrependUint8Slot(22, lifeTimeType, 0)

def clz_Torappu_BuffDataAddTakeSnapshotWhenExtend(builder, takeSnapshotWhenExtend):
    builder.PrependBoolSlot(23, takeSnapshotWhenExtend, 0)

def clz_Torappu_BuffDataAddDurationKey(builder, durationKey):
    builder.PrependUOffsetTRelativeSlot(24, flatbuffers.number_types.UOffsetTFlags.py_type(durationKey), 0)

def clz_Torappu_BuffDataAddLifeTime(builder, lifeTime):
    builder.PrependFloat32Slot(25, lifeTime, 0.0)

def clz_Torappu_BuffDataAddTriggerLifeType(builder, triggerLifeType):
    builder.PrependUint8Slot(26, triggerLifeType, 0)

def clz_Torappu_BuffDataAddTriggerCnt(builder, triggerCnt):
    builder.PrependInt32Slot(27, triggerCnt, 0)

def clz_Torappu_BuffDataAddTriggerInterval(builder, triggerInterval):
    builder.PrependFloat32Slot(28, triggerInterval, 0.0)

def clz_Torappu_BuffDataAddWaitFirstTriggerInterval(builder, waitFirstTriggerInterval):
    builder.PrependBoolSlot(29, waitFirstTriggerInterval, 0)

def clz_Torappu_BuffDataAddFirstTriggerInterval(builder, firstTriggerInterval):
    builder.PrependFloat32Slot(30, firstTriggerInterval, 0.0)

def clz_Torappu_BuffDataAddPriority(builder, priority):
    builder.PrependInt32Slot(31, priority, 0)

def clz_Torappu_BuffDataAddPriorityBbkeys(builder, priorityBbkeys):
    builder.PrependUOffsetTRelativeSlot(32, flatbuffers.number_types.UOffsetTFlags.py_type(priorityBbkeys), 0)

def clz_Torappu_BuffDataStartPriorityBbkeysVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_BuffDataAddStripBlackboardParamsWithBuffKey(builder, stripBlackboardParamsWithBuffKey):
    builder.PrependBoolSlot(33, stripBlackboardParamsWithBuffKey, 0)

def clz_Torappu_BuffDataAddBlackboard(builder, blackboard):
    builder.PrependUOffsetTRelativeSlot(34, flatbuffers.number_types.UOffsetTFlags.py_type(blackboard), 0)

def clz_Torappu_BuffDataStartBlackboardVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_BuffDataEnd(builder):
    return builder.EndObject()



class dict__string__clz_Torappu_BuffData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = dict__string__clz_Torappu_BuffData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsdict__string__clz_Torappu_BuffData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # dict__string__clz_Torappu_BuffData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # dict__string__clz_Torappu_BuffData
    def Key(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # dict__string__clz_Torappu_BuffData
    def Value(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = clz_Torappu_BuffData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def dict__string__clz_Torappu_BuffDataStart(builder):
    builder.StartObject(2)

def dict__string__clz_Torappu_BuffDataAddKey(builder, key):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(key), 0)

def dict__string__clz_Torappu_BuffDataAddValue(builder, value):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)

def dict__string__clz_Torappu_BuffDataEnd(builder):
    return builder.EndObject()



class clz_Torappu_SimpleKVTable_clz_Torappu_BuffData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = clz_Torappu_SimpleKVTable_clz_Torappu_BuffData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsclz_Torappu_SimpleKVTable_clz_Torappu_BuffData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # clz_Torappu_SimpleKVTable_clz_Torappu_BuffData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # clz_Torappu_SimpleKVTable_clz_Torappu_BuffData
    def Buffs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = dict__string__clz_Torappu_BuffData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # clz_Torappu_SimpleKVTable_clz_Torappu_BuffData
    def BuffsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # clz_Torappu_SimpleKVTable_clz_Torappu_BuffData
    def BuffsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def clz_Torappu_SimpleKVTable_clz_Torappu_BuffDataStart(builder):
    builder.StartObject(1)

def clz_Torappu_SimpleKVTable_clz_Torappu_BuffDataAddBuffs(builder, buffs):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buffs), 0)

def clz_Torappu_SimpleKVTable_clz_Torappu_BuffDataStartBuffsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def clz_Torappu_SimpleKVTable_clz_Torappu_BuffDataEnd(builder):
    return builder.EndObject()

ROOT_TYPE = clz_Torappu_SimpleKVTable_clz_Torappu_BuffData
