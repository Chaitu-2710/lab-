#include <stdio.h>

struct node {
    unsigned dist[20];
    unsigned from[20];
} rt[10];

int main() {
    int cost[20][20], nodes, i, j, k, updated;

    printf("Enter number of nodes: ");
    scanf("%d", &nodes);

    printf("Enter cost matrix:\n");
    for (i = 0; i < nodes; i++) {
        for (j = 0; j < nodes; j++) {
            scanf("%d", &cost[i][j]);
            cost[i][i] = 0;
            rt[i].dist[j] = cost[i][j];
            rt[i].from[j] = j;
        }
    }

    do {
        updated = 0;
        for (i = 0; i < nodes; i++)
            for (j = 0; j < nodes; j++)
                for (k = 0; k < nodes; k++)
                    if (rt[i].dist[j] > cost[i][k] + rt[k].dist[j]) {
                        rt[i].dist[j] = cost[i][k] + rt[k].dist[j];
                        rt[i].from[j] = k;
                        updated = 1;
                    }
    } while (updated);

    for (i = 0; i < nodes; i++) {
        printf("\nRouter %d:\n", i + 1);
        for (j = 0; j < nodes; j++)
            printf("Node %d via %d distance %d\n", j + 1, rt[i].from[j] + 1, rt[i].dist[j]);
    }

    return 0;
}