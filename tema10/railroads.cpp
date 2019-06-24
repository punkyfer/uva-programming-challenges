#include <iostream>
#include <string.h>
#include <map>
#include <sstream>
#include <stdlib.h>

using namespace std;
struct route {
  int time;
  int etime;
  int city;
  string name;
};

int numroutes[105], dist[2400][105];
map<string,int> citymap;
int starttime, startcity, endcity, numcities;
int maxtime = 0;
route tmp, aux;
route troutes[105][105];

void split_string(string st) {
  int pos = st.find(" ");
  tmp.time = atoi(st.substr(0,pos).c_str());
  st.erase(0, pos+1);
  tmp.name = st;
}

string format_time(int time) {
  stringstream ss;
  ss << time;
  string res = ss.str();
  while( res.length() < 4 ) res = "0"+res;
  return res;
}

int memoized_railroads(){

  for (int i=0; i<numroutes[startcity]; i++) {
    if (troutes[startcity][i].time >= starttime) {
      dist[troutes[startcity][i].etime][troutes[startcity][i].city] = max(
        dist[troutes[startcity][i].etime][troutes[startcity][i].city],
        troutes[startcity][i].time);
    }
  }

  for (int i=starttime; i<maxtime+1; i++) {
    for (int j=0; j<numcities; j++) {
      for (int k=0; k<numroutes[j]; k++) {
        if (troutes[j][k].time >= i) {
          dist[troutes[j][k].etime][troutes[j][k].city] = max(
            dist[troutes[j][k].etime][troutes[j][k].city],
            dist[i][j]);
        }
      } 
    }

    if (dist[i][endcity] != -1) return i;
  }
  return -1;
}

int main()
{ 
  int numcases, numr, numstops, ttime, ptime, pcity;
  string city, tcity, st;
  
  getline(cin, st);
  numcases = atoi(st.c_str());
  for (int k=1; k<=numcases; k++) {
    memset(&troutes, 0, sizeof(troutes));
    memset(numroutes, 0, sizeof(numroutes));
    memset(dist, -1, sizeof(dist));
    citymap.clear();

    cout << "Scenario " << k << "\n";

    getline(cin, st);
    numcities = atoi(st.c_str());
    for (int i=0; i<numcities; i++) {
      getline(cin, city);
      citymap[city] = i;
    }

    getline(cin, st);
    numr = atoi(st.c_str());;
    for (int i=0; i<numr; i++) {
      getline(cin, st);
      numstops = atoi(st.c_str());
      if (numstops > 0) {
        getline(cin, st);
        split_string(st);
        ptime = tmp.time;
        pcity = citymap[tmp.name];
        for (int j=1; j<numstops; j++) {
          getline(cin, st);
          split_string(st);
          ttime = tmp.time;
          tcity = tmp.name;
          // Falla desde aqui
          troutes[pcity][numroutes[pcity]].time = ptime;
          troutes[pcity][numroutes[pcity]].etime = ttime;
          troutes[pcity][numroutes[pcity]].city = citymap[tcity];
          numroutes[pcity]++;
          // Hasta aqui
          ptime = ttime;
          pcity = citymap[tcity]; 
          if (ttime > maxtime) maxtime = ttime;
        }
      }
    }
    getline(cin, st);
    starttime = atoi(st.c_str());
    getline(cin, city);
    getline(cin, tcity);
    startcity = citymap[city];
    endcity = citymap[tcity];

    int atime = memoized_railroads();
    //int atime = -1;
    if (atime==-1) cout << "No connection\n";
    else {
      cout << "Departure " << format_time(dist[atime][endcity]) << " " << city << "\n";
      cout << "Arrival   " << format_time(atime) << " " << tcity << "\n";
    }
    cout << "\n";
  }

  return 0;
}