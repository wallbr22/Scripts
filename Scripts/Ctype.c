#include <stdio.h>

void get_cpu_info() {
    printf("CPU Information:\n");
    system("wmic cpu get name, numberOfCores");
}

void get_ram_info() {
    printf("\nRAM Information:\n");
    system("wmic MEMORYCHIP get Capacity");
}

void get_gpu_info() {
    printf("\nGPU Information:\n");
    system("wmic path win32_VideoController get name");
}

void get_disk_info() {
    printf("\nDisk Information:\n");
    system("wmic diskdrive get name,size,model");
}

int main() {
    get_cpu_info();
    get_ram_info();
    get_gpu_info();
    get_disk_info();
    return 0;
}