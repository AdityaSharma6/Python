import smbus

''' MAIN ADDRESSES '''
PCF8591_ADDR    = 0x48
REG_ADDR        = 0x40

''' ADC CHANNELS '''
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
ADC_CHANNELS = [A0, A1, A2, A3]

file = open("sample.txt", "w+")
file.close()
def twos_complement(val):
    return -((255 - val) + 1) if val >= 0x80 else val

class PCF8591:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.set_channel(0)
 
    def set_channel(self, num):
        self.bus.write_byte(PCF8591_ADDR, ADC_CHANNELS[num])
        self.current_channel = num
 
    def get_reading(self):
        return self.bus.read_byte(PCF8591_ADDR)

    def get_channel(self, num):
        if self.current_channel != num:
            self.set_channel(num)
        return twos_complement(self.get_reading())
    
        
def main():
    from time import sleep
    adc = PCF8591()
    while True:
        print (adc.get_channel(0))
        sleep(0.2)
        


        
if __name__ == "__main__":
    main()
