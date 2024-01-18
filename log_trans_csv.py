# V 消息类型
# can_jxps.main.working.heartbeat TAG 标记
# 343.960 上电后经过的秒数
# TIM_ServiceCall RTOS的线程名称
# ../App/CAN_JXPS/Src/can_jxps.c 文件路径
# 266 行号
# JXPS_CAN_Heartbeat_Event 函数名称
# 发送心跳 日志内容

import csv

text = '''
V/can_jxps.main.working.heartbeat [39.113  TIM_ServiceCall] (../App/CAN_JXPS/Src/can_jxps.c:266 JXPS_CAN_Heartbeat_Event)发送心跳
V/can_jxps.main.working.heartbeat [39.113  TIM_ServiceCall] (../App/CAN_JXPS/Src/can_jxps.c:266 JXPS_CAN_Heartbeat_Event)发送心跳
'''

lines = [line.strip() for line in text.strip().split('\n') if line.strip()]

fieldnames = ['消息类型', 'TAG标记', '上电后经过的秒数', 'RTOS的线程名称', '文件路径', '行号', '函数名称', '日志内容']
data = []

# 遍历文本的每一行
for line in lines:
    columns = line.split(' ')

    record = {
        '消息类型': line[0],
        'TAG标记': columns[0].split('/')[1],
        '上电后经过的秒数': columns[1][1:],
        'RTOS的线程名称': columns[3].strip('[]'),
        '文件路径': columns[4].split(':')[0][1:],
        '行号': columns[4].split(':')[1],
        '函数名称': columns[5].split(')')[0],
        '日志内容': columns[5].split(')')[1]
    }
    data.append(record)

filename = 'output.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"转换成功，已将内容保存为 {filename} 文件。")