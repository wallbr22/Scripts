#Script author: Wallace Silveira

import platform
import psutil
import subprocess
from gpustat import GPUStatCollection

def get_cpu_info():
    cpu_info = {}
    cpu_info["brand"] = platform.processor()
    cpu_info["cores"] = psutil.cpu_count(logical=False)
    cpu_info["threads"] = psutil.cpu_count(logical=True)
    return cpu_info

def get_ram_info():
    ram_info = {}
    ram = psutil.virtual_memory()
    ram_info["total"] = round(ram.total / (1024 ** 3), 2)
    return ram_info

def get_gpu_info():
    try:
        gpu_stats = GPUStatCollection.new_query()
        gpus = []
        for gpu in gpu_stats:
            gpus.append({"name": gpu.name})
        return gpus
    except Exception as e:
        print(f"Error getting GPU information: {e}")
        return None

def get_storage_info():
    storage_info = []
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'fixed' in partition.opts:
            usage = psutil.disk_usage(partition.mountpoint)
            storage_info.append({
                "device": partition.device,
                "total": round(usage.total / (1024 ** 3), 2)
            })
    return storage_info

def get_motherboard_info():
    if platform.system() == 'Windows':
        try:
            base_board_info = subprocess.check_output("wmic baseboard get product, manufacturer", shell=True).decode().split("\n")
            manufacturer, product = base_board_info[1].strip().split("  ", 1)
            return {"manufacturer": manufacturer, "product": product}
        except Exception as e:
            print(f"Error getting motherboard information: {e}")
            return None
    else:
        print("Motherboard information is only available on Windows.")
        return None

def print_specs(title, specs):
    print(f"{title}:")
    for key, value in specs.items():
        print(f"  {key.capitalize()}: {value}")
    print()

def main():
    print_specs("CPU Information", get_cpu_info())
    print_specs("RAM Information", get_ram_info())

    gpu_info = get_gpu_info()
    if gpu_info:
        for idx, gpu in enumerate(gpu_info):
            print_specs(f"GPU {idx + 1} Information", gpu)

    storage_info = get_storage_info()
    for idx, storage in enumerate(storage_info):
        print_specs(f"Storage {idx + 1} Information", storage)

    motherboard_info = get_motherboard_info()
    if motherboard_info:
        print_specs("Motherboard Information", motherboard_info)

if __name__ == "__main__":
    main()
