#include <iostream>
#include <string.h>
#include <queue>
#include <numeric>
#include <algorithm>
#include <stdlib.h>

#define INF 9999999
using namespace std;
int cost[501][501], edges[501][501], neighbours[501], stations[101], isstation[101], dist[101], tdist[101], rdist[101];
int tarr[101];
int numstations, numintersections;

int find_cost(int a){
  int cost = 0;
  for (int i=1; i<=numintersections; i++){
    if (a==0)
      if (tdist[i] > cost) cost = tdist[i];
    if (a==1)
      if (rdist[i] > cost) cost = rdist[i];
  }
  return cost;
}

void copy_both_dist(){
  for (int i=1; i<=numintersections; i++){
    if (dist[i] < tdist[i])
      rdist[i] = dist[i];
    else
      rdist[i] = tdist[i];
  }
}

void copy_dist(){
  /*cout << " COPY DIST\n";
  cout << "Dist - {";
  for (int k=1; k<=numintersections; k++){
    if (k<numintersections) cout << dist[k] << ", ";
    else cout << dist[k] << "}\n";
  }*/
  for (int i=1; i<=numintersections; i++)
    if (dist[i] < tdist[i])
      tdist[i] = dist[i];

  /*cout << "TDist - {";
  for (int k=1; k<=numintersections; k++){
    if (k<numintersections) cout << tdist[k] << ", ";
    else cout << tdist[k] << "}\n";
  }*/
}

void string_to_int(string s) {
  int pos = 0;
  int ctr = 0;
  while((pos = s.find(" ")) != std::string::npos){
    tarr[ctr] = atoi(s.substr(0,pos).c_str());
    s.erase(0, pos+1);
    ctr += 1;
  }
  tarr[ctr] = atoi(s.c_str());
}


int mindist(int visited[]){
  int minv = INF, mini;
  for (int i=1; i<=numintersections; i++){
    if (visited[i] == 0 and dist[i] <= minv){
      minv = dist[i], mini = i;
    }
  }
  return mini;
}

int dijkstra2(int source_node) {
  memset(dist, INF, sizeof(dist));
  dist[source_node] = 0;
  int visited[numintersections+1];
  memset(visited, 0, sizeof(visited));
  

  for (int ctr=1; ctr<=numintersections; ctr++) {
    
    int u = mindist(visited);
    visited[u] = 1;

    for (int j=0; j<neighbours[u]; j++){
      int nnode = edges[u][j];
      if (visited[nnode]==0 and dist[u] != INF and dist[u]+cost[u][nnode] < dist[nnode])
        dist[nnode] = dist[u]+cost[u][nnode];
    }
  }

}

int findstation(){
  /*for (int k=1; k<=numintersections; k++){
    cout << "Node: " << k << " - {";
    for (int m=0; m<neighbours[k]; m++){
      if (m<neighbours[k]-1) cout << edges[k][m] << " (" << cost[k][edges[k][m]] << "), ";
      else cout << edges[k][m] << " (" << cost[k][edges[k][m]] << ")}\n";
    }
  }*/
  int minnode = -1;
  int mincost = INF;
  if (numstations > 0) {
    dijkstra2(stations[0]);
    copy_dist();
    for (int i=1; i<numstations; i++){
      dijkstra2(stations[i]);
      copy_dist();
    }
  }
  minnode = stations[0];
  mincost = find_cost(0);

  /*cout << "S: {";
  for (int k=1; k<=numintersections; k++){
    if (k<numintersections) cout << tdist[k] << ", ";
    else cout << tdist[k] << " } - "<< mincost << "\n";
  }*/

  for (int i=1; i<=numintersections; i++) {
    if (isstation[i] == 0) {
      dijkstra2(i);
      copy_both_dist();
      int newcost = find_cost(1);
      /*cout << i << ": {";
      for (int k=1; k<=numintersections; k++){
        if (k<numintersections) cout << rdist[k] << ", ";
        else cout << dist[k] << " } - "<< newcost << "\n";
      }*/
      if (newcost < mincost) {
        mincost = newcost;
        minnode = i;
      }
    }
  }

  return minnode;
}

int main()
{ 
  string st;
  int numcases;
  cin >> numcases;
  for (int k=0; k<numcases; k++) {
    memset(edges, 0, sizeof(edges));
    memset(neighbours, 0, sizeof(neighbours));
    memset(stations, 0, sizeof(stations));
    memset(isstation, 0, sizeof(isstation));
    memset(tdist, INF, sizeof(tdist));
    memset(cost, 0, sizeof(cost));
    getline(cin, st);
    int t = st[0] - '0';
    while (t==-35) {
      getline(cin, st);
      t = st[0] - '0';
    }
    string_to_int(st);
    numstations = tarr[0];
    numintersections = tarr[1];

    if (numstations > 0) {
      getline(cin, st);
      string_to_int(st);
      for (int i=0; i<numstations; i++) {
        stations[i] = tarr[i];
        isstation[tarr[i]] = 1;
      }
      sort(stations, stations+numstations);
    }

    if (numintersections > 1) {
      string s;
      while (getline(cin, s)){
        string_to_int(s);
        if (tarr[0] == 0) break;
        edges[tarr[0]][neighbours[tarr[0]]++] = tarr[1];
        edges[tarr[1]][neighbours[tarr[1]]++] = tarr[0];
        cost[tarr[0]][tarr[1]] = tarr[2];
        cost[tarr[1]][tarr[0]] = tarr[2];
      }
    }
    
    if (numstations == numintersections) cout << stations[0] << "\n";
    else {
      cout << findstation() << "\n";
    }

    if (k != numcases-1) cout << "\n";
  }
}