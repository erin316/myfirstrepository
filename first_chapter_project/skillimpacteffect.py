
class SkillImpactEffect:
    """
    技能影响效果
    """
    def impact(self):
        raise NotImplementedError
class DamageEffect(SkillImpactEffect):
    def __init__(self,value):
        self.value=value
    def impact(self):
        print("扣你血%d"%self.value)
class LowerDeffenseEffect(SkillImpactEffect):
    """
    降低防御力
    """
    def __init__(self,value,time):
        self.value=value
        self.time=time
    def impact(self):
        print("降低%d防御力，持续%d秒"%(self.value,self.time))
class DizzinessEffect(SkillImpactEffect):
    """
    眩晕
    """
    def __init__(self,time):
        self.time=time
    def impact(self):
        print("眩晕%d秒"%self.time)

class SkillDeployer:
    """
    技能释放器
    """
    def __init__(self,name):
        self.name=name
        #加载配置文件{技能名称：[效果]}
        self.__dict_skill_config=self.__load_config_file()
        #创建效果对象
        self.__effect_object=self.__creat_effect_object()
    def __load_config_file(self):
        return{
            "相龙十八掌":["DamageEffect(200)","LowerDeffenseEffect(10,2)","DizzinessEffect(6)"],
            "六脉神剑":["DamageEffect(100)","LowerDeffenseEffect(5,1)","DizzinessEffect(6)"]
            }
    def __creat_effect_object(self):
        list_effect_name= self.__dict_skill_config[self.name]
        list_effect_object=[]
        for item in list_effect_name:
            list_effect_object.append(eval(item))
        return list_effect_object
    #生成技能(执行效果)
    def generate_skill(self):
        print("释放技能啦！")
        for item in self.__effect_object:
            item.impact()

xlsbz=SkillDeployer("相龙十八掌")
xlsbz.generate_skill()









