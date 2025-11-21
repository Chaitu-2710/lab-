#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct frame{
    int seq_no;
    char text[20];
} fr[50], shuf[50];

char msg[200];

int assign_seq(){
    int len=strlen(msg), i,j=0;
    for(i=0;i<len;i+=4){
        fr[j].seq_no=j+1;
        strncpy(fr[j].text,&msg[i],4);
        fr[j].text[4]='\0';
        j++;
    }
    return j;
}

void shuffle(int n){
    int used[50]={0}, i,r;
    srand(time(NULL));
    for(i=0;i<n;i++){
        do r = rand()%n; while(used[r]);
        used[r]=1;
        shuf[i]=fr[r];
    }
}

void sort(int n){
    int i,j;
    struct frame temp;
    for(i=0;i<n;i++)
        for(j=0;j<n-1;j++)
            if(shuf[j].seq_no > shuf[j+1].seq_no){
                temp=shuf[j];
                shuf[j]=shuf[j+1];
                shuf[j+1]=temp;
            }
}

int main(){
    int n,i;
    printf("Enter message: ");
    fgets(msg,200,stdin);
    msg[strcspn(msg,"\n")] = '\0';

    n = assign_seq();
    shuffle(n);
    sort(n);

    printf("\nOutput: ");
    for(i=0;i<n;i++) printf("%s",shuf[i].text);
    printf("\n");
    return 0;
}