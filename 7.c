Software Used: Turbo c++/Devc++/Code blocks

Program:

#include<iostream>

#include<dos.h>

Dept of CSE

SCIENT INSTITUTE OF TECHNOLOGY

Ibrahimpatnam. R.R Dist-501506

(Approved by AICTE & Affiliated to JNTUH, Hyderabad)

L

#include<stdlib.h>

#define bucketSize 512 using namespace std; voidbktInput(inta,int b)

{

if(a>bucketSize)

cout<<"\n\t\tBucket overflow";

else

{

while(a>b)

{

cout<<"\n\t\t"<<b<<" bytes outputted.";

a-=b;

}

if(a>0)

cout<<"\n\t\tLast "<<a<<" bytes sent\t";

cout<<"\n\t\tBucket output successful";

}

}

int main()

{

randomize();

int op, pktSize; cout<<"Enter output rate: ";

cin>>op;

for(inti=1;i<=5;i++)

{
delay(random(1000));

pktSize=random(1000);

cout<<"\nPacket no "<<i<<"\tPacket size = "<<pktSize;

bktInput(pktSize,op);

}

return 0;

}
