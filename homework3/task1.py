import psutil
import configparser
import time


config = configparser.ConfigParser()
config.read("config.ini")
interval = int(config["cpu"]["interval"])
outfile = config["out"]["output_file"]


class SysMon:
    snap = 1

    def get_info(self):
        while True:
            p_time = "SNAPSHOT", self.snap, time.ctime()
            p_cpu = "\nCPU Usage:", psutil.cpu_percent(interval=interval)
            p_vm = "\nVM Usage:", psutil.virtual_memory().used 
            p_swap = "\nSwap Usage", psutil.swap_memory().used
            p_hdd = "\nHDD I/O:", psutil.disk_io_counters()
            p_net = "\nNet stat:", psutil.net_if_stats(), "\n"
            p_out = [p_time, p_cpu, p_vm, p_swap, p_hdd, p_net]
            with open(outfile, "a") as file:
                for i in range(len(p_out)):
                    file.write(' '.join(map(str, p_out[i])))
            self.snap += 1
            time.sleep(10)


Mon = SysMon()
Mon.get_info()
