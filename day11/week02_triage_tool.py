def triage_tool(temperature, blood_pressure_systolic, symptoms):
    """
    简单分诊工具
    :param temperature: 体温 (摄氏度 float/int)
    :param blood_pressure_systolic: 收缩压 (mmHg int)
    :param symptoms: 症状列表 (list), 可选值: ['发热', '胸痛', '咯血', '呼吸困难', '意识障碍',"无"]
    :return: 分诊分级 (str)
    """
    # 初始化分级
    level = "4级（非急症/观察）"

    # 1. 判断危重症条件 (1级)
    if (temperature >= 40) or (blood_pressure_systolic <= 90) or \
       (set(symptoms) & {'呼吸困难', '意识障碍'}):
        level = "1级（危重症/立即抢救）"
    
    # 2. 判断急症条件 (2级)，仅当未达到1级时判断
    elif (temperature >= 39) or (blood_pressure_systolic <= 100) or \
         ('胸痛' in symptoms or '咯血' in symptoms):
        level = "2级（急症/紧急处理）"
    
    # 3. 判断亚急症条件 (3级)
    elif (temperature >= 38) or (blood_pressure_systolic <= 120) :
        level = "3级（亚急症/常规就诊）"
    elif (temperature >= 36) or (blood_pressure_systolic <= 139) :
        level = "4级（非急症/观察）"
    return level

def main():
    print("=== 简单分诊工具 ===")
    try:
        # 获取用户输入
        temp = float(input("请输入体温 (℃): "))
        bp = int(input("请输入收缩压 (mmHg): "))
        # 处理症状输入（支持逗号分隔）
        symptom_input = input("请输入症状（可多选，用逗号分隔，可选：发热、胸痛、咯血、呼吸困难、意识障碍、无）：")
        # 清洗输入并转换为列表
        symptom_list = [s.strip() for s in symptom_input.split(',') if s.strip()]

        # 执行分诊并输出结果
        result = triage_tool(temp, bp, symptom_list)
        print(f"\n【分诊结果】: {result}")

        # 辅助建议
        if result.startswith("1级"):
            print("⚠️ 建议：立即拨打急救电话或前往急诊抢救室！")
        elif result.startswith("2级"):
            print("⚠️ 建议：尽快前往急诊就诊，避免延误。")
        else:
            print("ℹ️ 建议：休息观察，如不适加重请及时就医。")

    except ValueError:
        print("输入错误，请确保体温/血压输入为数字。")

if __name__ == "__main__":
    main()