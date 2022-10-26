from pymodbus3.client.sync import ModbusTcpClient
from pymodbus3.transaction import ModbusRtuFramer as ModbusFramer


class ModBus:
    def __init__(self, host, port):
        self.client = ModbusTcpClient(host, port=port, framer=ModbusFramer)
        self.success = self.client.connect()

    def get_data_modbus(self, unit):
        read = self.client.read_input_registers(address=1001, count=1, unit=unit)
        return read.registers[0] if read.registers else None
