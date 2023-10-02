#include <stdlib.h>

int main() {
    int return_value;

    // Run the network check script.
    return_value = system("./network");

    if(return_value == 0) {
        printf("Network check passed.\n");
        
        // Continue with setup.
        
    } else {
        printf("Network check failed. Aborting setup.\n");
        return 1;
    }

    // Continue with other setup tasks.

    return 0;
}
