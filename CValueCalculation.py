import math
import os

def p_from_c(c):
    # 根据 传入 C 值，计算该C值下，最大暴击范围的综合暴击率
    d_pre_success_p = 0.0
    d_pe = 0.0
    # 确定最大暴击范围
    n_max_fail = math.ceil(1.0 / c)
    for i in range(1, n_max_fail + 1):
        # 计算“在之前i-1次攻击均未暴击的情况下，当次攻击为首次暴击的成功概率”
        d_cur_p = min(1.0, i * c) * (1 - d_pre_success_p)
        # 将当次攻击为首次暴击的成功概率累加到一个变量中，作为“已经考虑到的成功概率范围”
        d_pre_success_p += d_cur_p
        # 根据数学期望公式计算当前C值下，打出暴击需要的平均攻击次数
        d_pe += d_cur_p * i
        # 使用倒数，根据“当前C值下，打出暴击需要的平均攻击次数”求出“当前C值下的综合暴击率”
    return 1.0 / d_pe


def c_from_p(p):
    # 根据传入的暴击率，计算 PRD 算法中的概率增量 C

    # 初始化上界为输入概率p
    d_up = p
    # 初始化下界为0
    d_low = 0.0
    # 使用无限循环进行二分查找
    while True:
        # 取上下界的中值作为待测的概率增量
        d_mid = (d_up + d_low) / 2.0
        # 将中值当做概率增量去算综合暴击率
        d_p_tested = p_from_c(d_mid)

        # 如果当次计算出的综合暴击率与理论暴击率的差值已经足够小，那么可以认为已经找到了符合要求的C值，这个时候退出循环
        if abs(d_p_tested - p) <= 0.000000000000002:
            break

        # 若新计算的综合暴击率较大，则调整上界
        if d_p_tested > p:
            d_up = d_mid
        else:
            # 否则调整下界
            d_low = d_mid

    # 循环结束后返回最终估算的综合暴击率
    return d_mid

# print(c_from_p(0.7))  # 计算在理论暴击率为0.7的情况下，概率增量C的值

# i = 0.001
# while i<=1:
#     with open('F:/Users/AshEc/Downloads/example.txt', 'a') as f:
#         f.write('{'+str(round(i,3))+','+str(f"{c_from_p(i):.15f}")+'},\n')
#         i+=0.001

file = os.path.join(os.path.dirname(__file__), 'CValues.txt')
with open(file, 'w') as f:
    Decimal = input("请输入要计算多少位小数的概率(范围2到3位小数):")
    IsNewLine = input("输出结果是否需要换行(输入'是'或'否'):")
    if (Decimal.isnumeric()):
        Decimal = int(Decimal)
    else:
        Decimal = int(ord(Decimal))
    Decimal = max(min(Decimal, 3), 2)
    print(str(Decimal)+'位小数')
    print('计算中请稍等...')
    Decimal =10 ** Decimal
    if (IsNewLine == '是'):
                IsNewLine = '\n'
    else:
                IsNewLine = ''
    with open(file, 'a') as f:
        f.write('{\n')
    for i in range(1,Decimal):
        with open(file, 'a') as f:
            p = i/Decimal
            f.write('{'+str(p)+','+str(f"{c_from_p(p):.15f}")+'},'+IsNewLine)
    with open(file, 'a') as f:
        f.write('\n};')
    print('计算完成,查看结果请打开'+file)