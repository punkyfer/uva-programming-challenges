#include<iostream>
#include <string.h>

using namespace std;

int mem[52][52];
int cuts[52];

int iter_dp(int num_cuts)
{
  for (int k = 0; k<num_cuts; k++) {
    for (int i=0; i<num_cuts-1-k; i++) {
      int j = i+1+k;
      if (k==0) mem[i][j] = 0;
      else {
        int minv = 9999999;
        for (int l=i+1; l<j; l++) {
          int tmp = mem[i][l] + mem[l][j];
          if (tmp < minv) minv = tmp;
        }
        mem[i][j] = cuts[j]-cuts[i] + minv;
      }
    }
  }

  return mem[0][num_cuts-1];
}

int main()

{ 
  int stick_length, num_cuts, aux;
  while (true) 
  {
    memset(cuts, -1, sizeof(cuts));
    cin >> stick_length;

    if (stick_length == 0) break;

    cin >> num_cuts;

    for (int i=0; i<num_cuts; i++) {
      cin >> aux;
      cuts[i+1] = aux;
    }

    cuts[0] = 0;
    cuts[num_cuts+1] = stick_length;

    memset(mem, -1, sizeof(mem));

    cout << "The minimum cutting is " << iter_dp(num_cuts+2) << ".\n";
  }
}