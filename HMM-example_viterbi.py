# -*- coding:utf-8 -*-
# Filename: viterbi.py
# Author：hankcs
# Date: 2014-05-13 下午8:51
 
states = ('Rainy', 'Sunny')
 
observations = ('walk', 'shop', 'clean')
 
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
 
transition_probability = {
    'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }
 
emission_probability = {
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
}
 
# 打印路径概率表
def print_dptable(V):
    print("    "),
    for i in range(len(V)):
        print("%7d" % i),
    print ()
    for y in V[0].keys():
        print("%.5s: " % y),
        for t in range(len(V)):
            print("%.7s" % ("%f" % V[t][y]) ),
        print()
 
 
def viterbi(obs, states, start_p, trans_p, emit_p):
    """
 
    :param obs:观测序列
    :param states:隐状态
    :param start_p:初始概率（隐状态）
    :param trans_p:转移概率（隐状态）
    :param emit_p: 发射概率 （隐状态表现为显状态的概率）
    :return:
    """
    # 路径概率表 V[时间][隐状态] = 概率
    V = [{}]
    # 一个中间变量，代表当前状态是哪个隐状态
    path = {}
 
    # 初始化初始状态 (t == 0)
    print('Day 1(walk): ')
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
        print (y, V[0][y], '=', start_p[y] ,'*', emit_p[y][obs[0]])
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print('V: ',V)
    print('__________________________________________')
    # 对 t > 0 跑一遍维特比算法
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        print ('Day', t+1, '('+obs[t]+')')
        for y in states:
            # 概率 隐状态 =    前状态是y0的概率 * y0转移到y的概率 * y表现为当前状态的概率
            # (prob, state) = max([(V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            tmpList = []
            print()
            for y0 in states:
                tmpList.append((V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0))

                print ('當天'+y+': ', "%.7s" % (V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]]),)
                print ('=',)
                print (V[t - 1][y0], '(前一天 '+y0+')', '*' ,)
                print (trans_p[y0][y], '('+y0+' to '+y+')', '*',)
                print (emit_p[y][obs[t]],'('+y, obs[t]+')')
            print ('當天'+y+'  最大的是: ',max(tmpList)[0])
            (prob, state) = max(tmpList)

            # 记录最大概率
            V[t][y] = prob
            # 记录路径
            newpath[y] = path[state] + [y]
 
        # 不需要保留旧路径
        path = newpath
        print('__________________________________________')
 
    print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])
 
 
def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
 
 
print(example())

print('\n訣竅: 從最後一天推算，\n1. Day3 機率最大的那條路徑\n2. 其Day2 機率最大那條路徑\n3. 的最可能Day1')
