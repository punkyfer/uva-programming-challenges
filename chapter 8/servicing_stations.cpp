#include<iostream>
#include<algorithm>
#include <string.h>

using namespace std;

int edges[35][35], neighbours[35], visited[35];
int numtowns, numtownpairs, minstations;

void dfs(int curstation, int numstations, int visited_towns)
{
  if (visited_towns == numtowns){
    // All Towns have been visited
    if (numstations < minstations) minstations = numstations;
    return;
  }
  // Prune branch if no more stations or current number of stations is bigger than previously found minimum 
  if (curstation > numtowns or numstations >= minstations) return;

  for (int i=1; i<curstation; i++) {
    // For all previous points, if it is not covered and
    // it does not have an edge to any node >= than our current one, remove
    if (visited[i]==0 and edges[i][neighbours[i]-1] < curstation) return;
  }

  // Put Shop in Town
  int counter = 0;
  for (int i=0; i<neighbours[curstation]; i++) {
    if (visited[edges[curstation][i]] == 0) counter++;
    visited[edges[curstation][i]]++;
  }
  if (counter > 0) dfs(curstation+1, numstations+1, visited_towns+counter);

  // Do Not Put Shop in Town
  for (int i=0; i<neighbours[curstation]; i++) {
    visited[edges[curstation][i]]--;
  }
  dfs(curstation+1, numstations, visited_towns);
}

int main()
{ 
  while(true) {
    memset(neighbours, 0, sizeof(neighbours));
    memset(edges, 0, sizeof(edges));
    memset(visited, 0, sizeof(visited));
    cin >> numtowns >> numtownpairs;
    if (numtowns==numtownpairs and numtowns==0) break;

    int t1, t2;
    for (int i=0; i<numtownpairs; i++) {
      cin >> t1 >> t2;
      edges[t1][neighbours[t1]++] = t2;
      edges[t2][neighbours[t2]++] = t1;
    }
    for (int i=1; i<=numtowns; i++) {
      edges[i][neighbours[i]++] = i;
      sort(edges[i], edges[i]+neighbours[i]);
    }

    minstations = numtowns;
    dfs(1,0,0);
    cout << minstations << "\n";
  }

  return 0;
}