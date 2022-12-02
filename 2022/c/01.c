#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

// this will be the death of me.

int main(int argc, char const *argv[])
{
    int *calories;
    FILE *fp;
    char *token, line[256];

    /* user handling */
    if(argc!=2){
        printf("usage: ./01 <input>\n");
        exit(EXIT_FAILURE);
    }

    if(access(argv[1], R_OK)==-1){
        printf("error: file does not exist");
        exit(EXIT_FAILURE);
    }
    /* user handling end */

    if(!(calories = (int *) calloc(1, sizeof(int)))){
        printf("error: unable to allocate memory - 01");
        exit(EXIT_FAILURE);
    }

    fp = fopen(argv[1], "r");
    
    while(fgets(line, 256, fp)){
        
        token = strtok(line, ",");
        while(token){
            printf("%s\n", line);
            token = strtok(NULL, ",");
        }
    }



    return 0;
}
