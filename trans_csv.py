import csv

text = '''
ACDC_STATUS[0]:
id: 0
vol: 0
cur: 0
status0: 0
status1: 0
status2: 0
temperature: 0
AB_vol: 0
BC_vol: 0
CA_vol: 0

ACDC_STATUS[1]:
id: 0
vol: 0
cur: 0
status0: 0
status1: 0
status2: 0
temperature: 0
AB_vol: 0
BC_vol: 0
CA_vol: 0

target_mode: 0
pulse_ware: 0
DC_mode: 0
DC_P_mode: 0
DC_N_value: 0.00
DC_P_value: 0.00
pulse_freq: 0
pulse_N_width: 0
pulse_P_width: 0
target_time_stamp: 0
control_mode: 0
protect_sens: 0
modbus_addr: 0

addr: hu
state: hu
before_state: hu
error_status: 0
status: 0
temperatures:
Sensor 1: 0.00
Sensor 2: 0.00
Sensor 3: 0.00
Sensor 4: 0.00
running_time: 0
up_time: 0
stop_time: 0
cur_peak_mean: 0.00
pwm_da_duty: 0.00
ACDC_error_stop_count: 0
impedance_mismatch_count: 0

ACDC_CONF:
DC_N.targetVol: 0
DC_N.targetCur: 0
DC_N.targetPowerP: 0
DC_N.currentVol: 0
DC_N.currentCur: 0
DC_N.currentPowerP: 0
DC_P.targetVol: 0
DC_P.targetCur: 0
DC_P.targetPowerP: 0
DC_P.currentVol: 0
DC_P.currentCur: 0
DC_P.currentPowerP: 0

duty_N_percent: 0.00
duty_P_percent: 0.00
output_vol_avg_N: 0.00
output_vol_peak_N: 0.00
output_vol_avg_P: 0.00
output_vol_peak_P: 0.00
input_L1_vol: 0.00
input_L2_vol: 0.00
input_L3_vol: 0.00

a: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
b: 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
'''

rows = []

# 以空行为分隔符切分文本内容
sections = [section.strip() for section in text.split('\n\n') if section.strip()]

# 遍历每个分节
for section in sections:
    # 储存键值对的临时字典
    row = {}

    # 以行为分隔符切分分节内容
    lines = [line.strip() for line in section.split('\n') if line.strip()]

    for line in lines:
        # 根据冒号切分键值对
        parts = line.split(':')
        key = parts[0].strip()
        value = ':'.join(parts[1:]).strip()

        # 检查是否为嵌套的字典
        if '[' in key:
            continue

        row[key] = value

    rows.append(row)

# 获取所有字段名
fieldnames = set()
for row in rows:
    fieldnames.update(row.keys())

filename = 'output.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"转换成功，已将内容保存为 {filename} 文件。")