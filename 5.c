Software Used: Turbo c++/Devc++/Code blocks

Program:

#include<stdio.h>

#include<conio.h>

struct node

{

unsigned dist[20];

unsigned from [20];

}rt[10];

Dept of CSE

SCIENT INSTITUTE OF TECHNOLOGY

Ibrahimpatnam. R.R Dist - 501506

(Approved by AICTE & Affiliated to JNTUH, Hyderabad)

int main()

{

intcostmat[20][20];

intnodes,i,j,k,count=0;

printf("\nEnter the number of nodes: ");

scanf("%d",&nodes);//Enter the nodes

printf("\nEnter the cost matrix :\n");

for(i=0;i<nodes;i++)

{

for(j=0;j<nodes;j++)

{

scanf("%d",&costmat[i][j]);

costmat[i][i]=0;

rt[i].dist[j]=costmat[i][j];//initialise the distance equal to cost matrix

rt[i].from[j]=j;

}

}

do

{
