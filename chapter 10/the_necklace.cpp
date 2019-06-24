#include<iostream>
#include <string.h>

using namespace std;
int edges[55][55], visited[55], neighbours[55];

void dfs(int node) 
{
  int nextnode;
  for (nextnode=1; nextnode<=55; nextnode++) {
    if (edges[node][nextnode] >= 1){
      edges[node][nextnode] -= 1;
      edges[nextnode][node] -= 1;

      dfs(nextnode);

      cout << nextnode << " " << node << "\n";
    }
  }
}

int main()
{ 
  int numcases;
  cin >> numcases;

  for (int k=0; k<numcases; k++) {
    cout << "Case #" << k+1 << "\n";
    memset(edges, 0, sizeof(edges));
    memset(visited, 0, sizeof(visited));
    memset(neighbours, 0, sizeof(neighbours));
    int numbeads;
    cin >> numbeads;
    int b1, b2;
    for (int i=0; i<numbeads; i++) {
      cin >> b1 >> b2;
      neighbours[b1] += 1;
      neighbours[b2] += 1;
      edges[b1][b2] += 1;
      edges[b2][b1] += 1;
    }
    bool lostB = false;
    for (int i=0; i<55; i++){
      if (neighbours[i] % 2 == 1) {
        lostB = true;
        break;
      }
    }
    if (lostB){
      cout << "some beads may be lost\n";
    }
    else {
      for (int i=1; i<=50; i++) dfs(i);
    }
    if (k != numcases-1) cout << "\n";
  }

  return 0;
}