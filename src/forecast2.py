import random
import copy

def _96度生命之水(自己,对手,回合数,回合状态):
    if 回合状态=='攻击后' and 对手['名字']=='阿琳双子':
        if 对手['濒死'] == 0 and 对手['生命值'] < 0:
            对手['生命值']=20
            对手['濒死']=1
            return 0
        return 0
    return 0
        

def 变成星星吧(自己,对手,回合数,回合状态):
    if 回合状态=='攻击中' and 自己['名字']=='艾琳双子':
        if 自己['濒死']==1:
            伤害 = 0
            r=random.uniform(0,100)
            if r <= 50:
                伤害=233
            else:
                伤害=50
def 摸鱼的快乐(自己,对手,回合数,回合状态):
    if 回合状态=='攻击前':
        自己['攻击力']+=3
        print(f'{自己["名字"]}攻击力增加了3')
        return 0
def 反弹反弹无效(自己,对手,回合数):
    pass
def 女仆的温柔清理(自己,对手,回合数,回合状态):
    '''普通攻击时有35%的概率本次伤害降低3点，同时使对方攻击力永久下降4点'''
    if 自己['名字']=='丽塔' and 回合状态 == '攻击中':
        r=random.uniform(0,100)
        if r <= 35:
            伤害 = 自己['攻击力']-对手['防御力']-3
            对手['攻击力']-=4
            if 对手['攻击力'] < 0:
                对手['攻击力']=0
            if 伤害<=0:
                伤害=0
            对手['生命值']-=伤害
            自己['攻击状态']=True
            print(f"丽塔使用女仆的温柔清理对对手造成{伤害}点伤害,攻击力下降4点")
def 完美心意(自己,对手,回合数,回合状态):
    '''每4个回合发动一次，为对方回复4点血量并使其陷入2个回合魅惑状态，无法使用技能。伤害永久下降60%（不可叠加）'''
    if 自己['名字']=='丽塔' and 回合状态 == '攻击前' and 回合数 % 4 == 0:
        对手['生命值']+=4
        对手['状态']='魅惑1'
        print('丽塔使用完美心意对手陷入魅惑状态')
    if 自己['名字']=='丽塔' and 回合状态 == '攻击前' and 回合数 % 6 == 0:
        对手['状态']='魅惑2'
def 血犹第一可爱(自己,对手,回合数,回合状态):
    '''攻击后有30%的概率降低对方5点的防御'''
    if 自己['名字']=='德丽莎' and 回合状态 == '攻击后':
        if 自己['状态']=='魅惑1'  or 自己['血犹'] == False:
            return
        r=random.uniform(0,100)
        if r <= 30:
            #对手['状态']='流血1'
            对手['防御力']-=5
            print('德丽莎使用血犹第一可爱对方防御力下降5点')
def 在线踢人(自己,对手,回合数,回合状态):
    '''每3回合发动一次，造成5次16点伤害'''
    if 自己['名字']=='德丽莎' and 回合状态 == '攻击前' and 回合数 % 3 == 0:
        自己['血犹'] = True
        if 自己['状态']=='魅惑1':
            return
        伤害 = 5 * (16 - 对手['防御力'])
        if 自己['状态']=='魅惑2':
            伤害-=伤害*0.6
        if 伤害<=0:
            伤害=0
        r=random.uniform(0,100)
        if not r <= 自己['命中率']:
            伤害=0
        对手['生命值']-=伤害
        print(f'德丽莎使用在线踢人对对手造成{伤害}点伤害')
def 凭神化剑(自己,对手,回合数,回合状态):
    '''所有攻击为无视防御的元素伤害'''
    if 自己['名字']=='符华' and 回合状态 == '攻击中':
        伤害 = 自己['攻击力']
        if 自己['状态']=='魅惑1':
            伤害-=对手['防御力']
            伤害-=伤害*0.6
        if 自己['状态']=='魅惑2':
            伤害-=伤害*0.6
        if 伤害>0:
            对手['生命值']-=伤害
        自己['攻击状态']=True
        print(f'符华对对手造成{伤害}点伤害')
def 形之笔墨(自己,对手,回合数,回合状态):
    '''每3个回合发动一次，泼对手一脸墨水，造成18点伤害，对手命中率下降25%'''
    if 自己['名字']=='符华' and 回合状态 == '攻击前' and 回合数 % 3 == 0:
        if 自己['状态']=='魅惑1':
            return
        伤害 = 18
        if 自己['状态']=='魅惑2':
            伤害-=伤害*0.6
        对手['命中率']-=25
        对手['生命值']-=伤害
        print('符华使用形之笔墨对对手造成18点伤害，对手命中下降25%')

# 角色模板 = {'名字':'','攻击力':0,'防御力':0,'速度':0,'技能1':'','技能2':''}
# 琪亚娜 = {'名字':'琪亚娜','攻击力':24,'防御力':11,'速度':23,'技能1':吃我一矛,'技能2':音浪太强}
# 芽衣 = {'名字':'芽衣','攻击力':22,'防御力':12,'速度':30,'技能1':崩坏世界的歌姬,'技能2':雷电家的龙女仆}
# 樱莲组 = {'名字':'樱莲组','攻击力':20,'防御力':9,'速度':18,'技能1':八重樱的饭团,'技能2':卡莲的饭团}
# 希儿 = {'名字':'希儿','攻击力':23,'防御力':13,'速度':26,'技能1':我换我自己,'技能2':拜托了另一个我,'人格':'白'}
# 布洛妮娅 = {'名字':'布洛妮娅','攻击力':21,'防御力':10,'速度':20,'技能1':天使重构,'技能2':摩托拜客哒}
# 阿琳姐妹 = {'名字':"阿琳姐妹",'攻击力':18,'防御力':10,'速度':10,'技能1':_96度生命之水,'技能2':变成星星吧,'濒死':0}
# 幽兰黛儿 = {'名字':'幽兰黛儿','攻击力':19,'防御力':10,'速度':15,'技能1':摸鱼的快乐,'技能2':反弹反弹无效}
丽塔 = {'名字':'丽塔','攻击力':26,'防御力':11,'速度':17,'技能1':女仆的温柔清理,'技能2':完美心意}
德丽莎 = {'名字':'德丽莎','攻击力':19,'防御力':12,'速度':22,'技能1':血犹第一可爱,'技能2':在线踢人,'血犹':True}
符华 = {'名字':'符华','攻击力':17,'防御力':15,'速度':16,'技能1':凭神化剑,'技能2':形之笔墨}

# def 随机测试():
#     c=1000000
#     cc = 0
#     print(f"随机{c}次")
#     for i in range(c):
#         r=random.uniform(0,100)
#         if r <= 35:
#             cc+=1
#     if cc == 0:
#         print("出现错误")
#         return
#     print(f"在{c}次里，有{cc}次命中，概率是{cc/c}")

def 技能处理(自己,对手,回合数,回合状态):
    #回合状态分发到各个技能
    自己['技能1'](自己,对手,回合数,回合状态)
    自己['技能2'](自己,对手,回合数,回合状态)
    对手['技能1'](自己,对手,回合数,回合状态)
    对手['技能1'](自己,对手,回合数,回合状态)
def 普攻处理(自己,对手):
    伤害=自己['攻击力']-对手['防御力']
    if 自己['状态']=='魅惑1' or 自己['状态']=='魅惑2':
        伤害-=伤害*0.6
    if 伤害 <= 0:
        伤害=0
    
    r=random.uniform(0,100)
    if not r <= 自己['命中率']:
        伤害=0
    对手['生命值']-=伤害
    print(自己['名字']+"普攻对对手造成"+f"{伤害}"+"点伤害")
def 回合处理(自己,对手,回合数):
    #负面状态处理
    if 自己['状态'] == '眩晕':
        自己['状态'] == ''
        return
    elif 自己['状态'] == '流血1':
        自己['防御力']-=5
        自己['状态'] = '流血2'
    elif 自己['状态']=='流血2':
        自己['防御力']+=5
        自己['状态'] = ''

    #回合开始前，技能
    技能处理(自己,对手,回合数,'攻击前')
    #回合中，技能
    技能处理(自己,对手,回合数,'攻击中')
    
    #如果未使用技能消耗攻击时，将进行普通攻击
    if 自己['攻击状态']==True:
        技能处理(自己,对手,回合数,'攻击后')
        return
    
    普攻处理(自己,对手)
    
    #回合结束时，技能
    技能处理(自己,对手,回合数,'攻击后')
def 对抗(对战者a,对战者b):
    对战者1 = copy.deepcopy(对战者a)
    对战者2 = copy.deepcopy(对战者b)

    #对抗前的初始化操作
    回合数 = 0
    对战者1['生命值']=100
    对战者2['生命值']=100
    对战者1['命中率']=100
    对战者2['命中率']=100
    对战者1['状态']=''
    对战者2['状态']=''
    本回合对战者 = ''
    等待回合的对战者 = ''
    
    #确定先手攻击的对战者
    if 对战者1['速度']>对战者2['速度']:
        本回合对战者 = 对战者1
        等待回合的对战者 = 对战者2
    else:
        本回合对战者 = 对战者2
        等待回合的对战者 = 对战者1
    print(f"回合{回合数} 战斗开始，{对战者1['名字']} 对战 {对战者2['名字']}，"+f"{本回合对战者['名字']} 先手")
    
    while(0 < 对战者1['生命值'] and 0 < 对战者2['生命值']):
        #输出对局状态
        回合数+=1
        print(f"第{回合数}回合 ",end=' ')
        print(对战者1["名字"] + "的生命值:"+ "{hp}".format(hp=对战者1['生命值']),end= ' ')
        print(对战者2["名字"] + "的生命值:"+ "{hp}".format(hp=对战者2['生命值']))
        
        #重置攻击状态
        对战者1['攻击状态']=False
        对战者2['攻击状态']=False

        回合处理(本回合对战者,等待回合的对战者,回合数)
        本回合对战者,等待回合的对战者=等待回合的对战者,本回合对战者

        if (0 > 对战者1['生命值'] or 0 > 对战者2['生命值']):
            break

        回合处理(本回合对战者,等待回合的对战者,回合数)
        本回合对战者,等待回合的对战者=等待回合的对战者,本回合对战者
    if 对战者1['生命值']>0:
        return 对战者1
    else:
        return 对战者2


def main():
    对抗次数 = 1000
    胜利次数 = 0

    global 希儿,布洛妮娅,琪亚娜,樱莲组,芽衣,阿琳姐妹,幽兰黛儿,丽塔,德丽莎,符华

    for i in range(对抗次数):
        胜利者=对抗(符华,德丽莎)
        print("胜利者:" + 胜利者['名字'])
        if 胜利者['名字'] == '德丽莎':
            胜利次数+=1
    print(f'胜率={胜利次数/对抗次数*100:.2f}%')

if __name__ == "__main__":
    main()