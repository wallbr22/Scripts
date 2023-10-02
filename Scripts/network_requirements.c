#include <stdio.h>
#include <stdlib.h>

void ping_check(char *ip_address) {
    char command[100];

    sprintf(command, "ping -c 4 %s", ip_address);
    system(command);
}

void latency_check(float latency) {
    if(latency < 5) {
        printf("Latency Check Passed\n");
    } else {
        printf("Latency Check Failed\n");
    }
}

void packet_loss_check(float packet_loss) {
    if(packet_loss == 0) {
        printf("Packet Loss Check Passed\n");
    } else {
        printf("Packet Loss Check Failed\n");
    }
}

int main() {
    char *ip_address = "8.8.8.8"; // Google's public DNS server, replace with your target IP
    float latency = 0.0; // replace with actual value, obtained from the output of the ping command
    float packet_loss = 0.0; // replace with actual value, obtained from the output of the ping command

    ping_check(ip_address);
    latency_check(latency);
    packet_loss_check(packet_loss);

    return 0;
}
