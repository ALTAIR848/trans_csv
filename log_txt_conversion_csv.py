import csv


# 作用： 将log文档转换成log列表
# 输入参数 input_text： 字符串形式的log文档
# 返回值： 每一条log形成的列表
def get_lines(input_text):
    lines = [line.strip() for line in input_text.strip().split('\n') if line.strip()]
    return lines


# 作用：将log列表转换成日志字典列表
# 输入参数： 每一条log形成的列表
# 返回值： 每一条log的key-val对应字典列表
def lines_conversion_dict(lines):
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
    return data


# 作用：将日志字典列表写入csv文件
# 输入参数：每一条log的key-val对应字典列表
# 输入参数：生成的csv文件名称
def save_log(data, filename):
    filename = filename + '.csv'
    fieldnames = ['消息类型', 'TAG标记', '上电后经过的秒数', 'RTOS的线程名称', '文件路径', '行号', '函数名称',
                  '日志内容']
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()  # 文件为空时，写入表头
        writer.writerows(data)
    print(f"转换成功，已将内容写入为 {filename} 文件。")


if __name__ == "__main__":
    text = '''
    V/can_jxps.main.working.heartbeat [39.113  TIM_ServiceCall] (../App/CAN_JXPS/Src/can_jxps.c:266 JXPS_CAN_Heartbeat_Event)发送心跳
    V/can_jxps.main.working.heartbeat [39.113  TIM_ServiceCall] (../App/CAN_JXPS/Src/can_jxps.c:266 JXPS_CAN_Heartbeat_Event)发送心跳
    V/can_jxps.main.working.heartbeat [2030.310  TIM_ServiceCall] (../App/CAN_JXPS/Src/can_jxps.c:266 JXPS_CAN_Heartbeat_Event)发送心跳
    V/can_jxps.main.watchdog.any.return [2.994  TIM_ServicTask] (../App/CAN_JXPS/Src/can_jxps_host.c:58 JXPS_CAN_HOST_INIT)设备数量过少
    '''
    log_lines = get_lines(text)
    log_dict = lines_conversion_dict(log_lines)
    save_log(log_dict, "log1")
