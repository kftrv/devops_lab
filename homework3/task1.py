import psutil
import configparser
import time
import json


config = configparser.ConfigParser()
config.read("config.ini")
interval = int(config["cpu"]["interval"])
outfile = config["out"]["output_file"]
outformat = config["out"]["format"]


class SysMon:
    snap = 1

    def get_info(self):
        while True:
            p_out = {}
            p_out["SNAPSHOT:"] = self.snap
            p_out["SNAPTIME:"] = time.ctime()
            p_out["CPU Usage:"] = psutil.cpu_percent(interval=interval)
            p_out["VM Usage:"] = psutil.virtual_memory().used
            p_out["Swap Usage"] = psutil.swap_memory().used
            p_out["HDD I/O:"] = psutil.disk_io_counters()
            p_out["Net stat:"] = psutil.net_if_stats()
            # p_out = [p_time, p_cpu, p_vm, p_swap, p_hdd, p_net]
            if outformat == 'json':
                with open(outfile, "a") as file:
                    json.dump(p_out, file, indent=4)
            else:
                with open(outfile, "a") as file:
                    file.write(str(p_out) + "\n")
            self.snap += 1
            time.sleep(int(config["wait"]["sleep"]))


Mon = SysMon()
Mon.get_info()
