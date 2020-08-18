from collections import deque
from threading import Thread

import struct
import sys
import time

import numpy as np
import serial
import serial.tools.list_ports


class SerialReader():
    def __init__(self, port, baud, timeout=None, buf_size=128, data_size=2, fmt='H'):
        
        # Serial port info
        self.port_name = port
        self.baudrate = baud
        self.timeout = timeout

        self.available_ports = serial.tools.list_ports.comports()

        # Thread
        self.thread = None
        self.is_running = True
        
        # Data Buffer
        self.data_size = data_size
        self.buf = deque(buf_size*[0], buf_size)#np.empty(data_size, dtype=float)
        self.buf_max_size = buf_size

        self.__raw_data = bytearray(data_size)
        self.__fmt = fmt

        # Time
        self.time_buf = deque(buf_size*[0], buf_size)


    def open(self):
        
        print(">> Trying to connect to %s at %d baudrate...\n" % (self.port_name, self.baudrate))
        
        try:
            self.serial_connection = serial.Serial(port=self.port_name, baudrate=self.baudrate, timeout=self.timeout)
            print(">> Successfully connected to %s at %d baudrate.\n" % (self.port_name, self.baudrate))

        except ValueError:
            print("\nBaudrate out of range. Use one of the standard values:")
            print([std_baud for std_baud in self.serial_connection.BAUDRATES])
            sys.exit(1)

        except serial.SerialException:
            print("Device could not be found or could not be configured. NOTE: Available ports are: ")
            print([comport.device for comport in self.available_ports])
            sys.exit(1)

        print(">> Starting reading from %s" % self.port_name)
        self.__start_thread()
    

    def close(self):
        self.is_running = False
        self.thread.join()
        self.serial_connection.close()
        print(">> Closed")

    def stop(self):
        self.is_running = False
        self.is_stopped = True
        self.thread.join()
        
        print(">> Stopped")

        while self.is_running is False:
            time.sleep(0.1)

    def resume(self):
        if self.is_stopped:
            self.is_running = True
            self.is_stopped = False
            self.open()
            self.__start_thread()
            print(">> Restarted")
    
    def __start_thread(self):
        if self.thread is None:
            self.thread = Thread(target=self.__worker)
            self.thread.start()
            print(">> Ready!")
    
    def __worker(self):
        time.sleep(0.001)
        self.serial_connection.reset_input_buffer()

        while self.is_running:
            self.serial_connection.readinto(self.__raw_data)
            val, = struct.unpack(self.__fmt, self.__raw_data)
            self.buf.append(val)
            self.time_buf.append(time.perf_counter())
