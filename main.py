from db import DataBase
from device import ModBus
import time
import keyboard


def read_ans_save_one_device(sensor):
    # {'sensor_id': 1, 'host': '192.168.1.254', 'port': 8880, 'unit': 1}
    host = sensor['host']
    port = sensor['port']
    unit = sensor['unit']
    modbus = ModBus(host=host, port=port)
    temp = modbus.get_data_modbus(unit)
    # temp = 3
    status = 1 if temp else 2

    # insert
    temp_model = DataBase('temperature')
    temp_model.insert_one(temp=temp, status=status, sensor_id=sensor['sensor_id'])

    return {'temp': temp, 'status': status}


def read_and_save_all_device(sensors):
    # [{'sensor_id': 1, 'host': '192.168.1.254', 'port': 8880, 'unit': 1}, {'sensor_id': 2, 'host': '192.168.1.254', 'port': 8880, 'unit': 2}]
    for sensor in sensors:
        read_ans_save_one_device(sensor)
    return list(map(read_ans_save_one_device, sensors))


def get_sensor():
    sensor_model = DataBase(table_name='sensor')
    sensor_raw_data = sensor_model.get_list()
    sensors = []
    for sensor in sensor_raw_data:
        sensors.append({
            'sensor_id': sensor[0], 'host': sensor[2], 'port': sensor[3], 'unit': sensor[4]
        })
    return sensors


def init():
    sensors = get_sensor()
    num = 0
    while True:
        num += 1
        read_and_save_all_device(sensors)
        time.sleep(2)
        print('running')
        if keyboard.is_pressed("q"):
            print("q pressed, ending loop")
            break


print(get_sensor())
# init()
