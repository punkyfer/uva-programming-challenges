#include <iostream>
#include <string.h>
#include <queue>
#include <numeric>
#include <algorithm>
#include <stdlib.h>

#define INF 9999999
using namespace std;
int cost[501][501], edges[501][501], neighbours[501], stations[101], dist[101], tdist[101], isstation[101];
int tarr[101];
int numstations, numintersections;

// MINIMIZE MAX DISTANCE FROM ANY NODE, NOT SUM OF ALL DISTANCES!!!!!!

int find_cost(int b){
  int cost = 0;
  for (int i=1; i<=numintersections; i++){
    if (b==0) {
      if (dist[i] > cost) cost = dist[i];
    }
    if (b==1) {
      if (tdist[i] > cost) cost = tdist[i];
    }
  }
  return cost;
}

int copy_dist(int b){
  int cost = 0;
  for (int i=1; i<=numintersections; i++){
    if (tdist[i] < dist[i]) {
      if (b==0) dist[i] = tdist[i];
      if (tdist[i] > cost) cost = tdist[i];
    }
    else {
      if (b==1) tdist[i] = dist[i];
      if (dist[i] > cost) cost = dist[i];
    }
  }
  return cost;
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



void dijkstra(int source_node, int distarr) {
  if (distarr == 0) {
    memset(dist, INF, sizeof(dist));
    dist[source_node] = 0;
  }
  else {
    memset(tdist, INF, sizeof(tdist));
    tdist[source_node] = 0;
  }
  int visited[numintersections+1];
  memset(visited, 0, sizeof(visited));
  queue <int> nqueue;
  nqueue.push(source_node);
  int node;
  while(!nqueue.empty()){
    node = nqueue.front();
    nqueue.pop();
    visited[node] = 1;

    for (int i=0; i<neighbours[node]; i++) {
      if (visited[edges[node][i]] == 0) {
        if (distarr==0) {
          if (dist[node]+cost[node][edges[node][i]] < dist[edges[node][i]]) {
            dist[edges[node][i]] = dist[node]+cost[node][edges[node][i]];
          }
        }
        if (distarr==1) {
          if (tdist[node]+cost[node][edges[node][i]] < tdist[edges[node][i]]) {
            tdist[edges[node][i]] = tdist[node]+cost[node][edges[node][i]];
          } 
        }
        nqueue.push(edges[node][i]);
      }
    }
  }
}

int findstation(){
  int minnode = -1;
  int mincost = INF;
  if (numstations > 0) {
    dijkstra(stations[0], 0);
    for (int i=1; i<numstations; i++){
      dijkstra(stations[i], 1);
      copy_dist(0);
    }
  }
  minnode = stations[0];
  mincost = find_cost(0);

  for (int i=1; i<=numintersections; i++) {
    if (isstation[i] == 0) {
      dijkstra(i, 1);
      int newcost = copy_dist(1);
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
    memset(cost, 0, sizeof(cost));
    memset(tdist, INF, sizeof(tdist));
    memset(dist, INF, sizeof(dist));
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