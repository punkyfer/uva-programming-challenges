#include<iostream>
#include <string.h>
#include <cstdlib>

using namespace std;

#define maxsteps 50
#define inf 9999999
int puzzle[4][4], allrows[16], blank_x, blank_y;
// UP - DOWN - LEFT - RIGHT
int dirs[4][2] = {{0,-1},{0,1},{1,0},{-1,0}};
int dirn[4] = {'L', 'R', 'D', 'U'};
string path;


int lower_bound() {
  int lbound = 0;
  for (int i=0; i<4; i++) {
    for (int j=0; j<4; j++) {
      if (puzzle[i][j]==0) continue;

      int g_x = (puzzle[i][j] - 1) / 4;
      int g_y = (puzzle[i][j] - 1) % 4;

      lbound += abs(i-g_x) + abs(j-g_y);
    }
  }
  return lbound;
}

int dfs(int num_steps, int prev_dir, int lim) {
  int lbound = lower_bound();
  if (lbound==0) return -1;
  if (num_steps + lbound > lim) return num_steps+lbound;

  int minv = inf; 

  for (int i=0; i<4; i++) {
    if (i == (prev_dir ^ 1)) continue;

    int new_x = blank_x + dirs[i][0];
    int new_y = blank_y + dirs[i][1];

    if (new_x < 0 or new_x > 3) continue;
    if (new_y < 0 or new_y > 3) continue;

    path.push_back(dirn[i]);
    int t_x, t_y;
    t_x = blank_x;
    t_y = blank_y;
    puzzle[blank_x][blank_y] = puzzle[new_x][new_y];
    puzzle[new_x][new_y] = 0;
    blank_x = new_x;
    blank_y = new_y;
    int t = dfs(num_steps+1, i, lim);
    if (t==-1) return -1;
    if (t<minv) minv = t;
    blank_x = t_x;
    blank_y = t_y;
    puzzle[new_x][new_y] = puzzle[blank_x][blank_y];
    puzzle[blank_x][blank_y] = 0;
    path = path.substr(0, path.size()-1);
  }

  return minv;
}

bool test_solvability() {
  int numinversions = 0;
  for (int i=0; i<16; i++) {
    if (allrows[i] != 0) {
      for (int j=i+1; j<16; j++) {
        if (allrows[j] != 0) {
          if (allrows[j] < allrows[i]) numinversions += 1;
        }
      }
    }
  }
  int numrow = (3-blank_x)+1;
  return (numinversions % 2 == 0) == (numrow % 2 != 0);
}

bool ida_star() {
  int bound = lower_bound();
  while(true) {
    int t = dfs(0,-1, bound);
    if (t==-1) return true;
    if (t==inf) return false;
    if (t>=50) return false;
    bound = t;
  }
  return false;
}


int main()
{ 
  int numcases;
  cin >> numcases;

  for (int k=0; k<numcases; k++) {
    memset(puzzle, 0, sizeof(puzzle));
    memset(allrows, 0, sizeof(allrows));
    path.clear();
    int t1;
    for (int i=0; i<4; i++) {
      for (int j=0; j<4; j++) {
        cin >> t1;
        if (t1==0) {
          blank_x = i;
          blank_y = j;
        }
        puzzle[i][j] = t1;
        allrows[i*4 + j] = t1;
      }
    }

    if (test_solvability()) {
      if (ida_star()) cout << path << "\n";
      else cout << "This puzzle is not solvable.\n";
    }
    else {
      cout << "This puzzle is not solvable.\n";
    }
  }

  return 0;
}