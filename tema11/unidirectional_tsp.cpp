#include<iostream>
#include <string.h>

using namespace std;

int matrix[10][100];
int cost[10][100];
int path[10][100];

int minimum(int x, int y, int z)
{
  return x < y ? (x < z ? x : z) : (y < z ? y : z);
}

void memoized_tsp(int num_rows, int num_cols)
{
  int final_cost = 9999999;
  int min_row = 0;
  if (num_rows == num_cols and num_rows == 1) {
    final_cost = matrix[0][0];
    min_row = 0;
  }
  else if (num_rows > num_cols and num_cols == 1) {
    for (int i=0; i<num_rows; i++) {
      if (matrix[i][0] < final_cost) {
        final_cost = matrix[i][0];
        min_row = i;
      }
    }
  }
  else if (num_cols > num_rows and num_rows == 1) {
    final_cost = 0;
    for (int j=0; j<num_cols; j++) {
      path[0][j] = 0;
      final_cost += matrix[0][j];
    }
    min_row = 0;

  }
  else {
    for (int i=0; i<num_rows; i++) cost[i][num_cols-1] = matrix[i][num_cols-1];
    
    for (int j = num_cols-2; j>-1;j--) {
      for (int i=0; i<num_rows; i++) {
        if (i==0) {
          cost[i][j] = minimum(cost[i][j+1], cost[i+1][j+1], cost[num_rows-1][j+1]);
          if (cost[i][j]==cost[i][j+1]) path[i][j] = i;
          else if (cost[i][j]==cost[i+1][j+1]) path[i][j] = i+1;
          else path[i][j] = num_rows-1;
        }
        else if (i==num_rows-1){
          cost[i][j] = minimum(cost[0][j+1], cost[i][j+1], cost[i-1][j+1]);
          if (cost[i][j]==cost[0][j+1]) path[i][j] = 0;
          else if (cost[i][j]==cost[i-1][j+1]) path[i][j] = i-1;
          else path[i][j] = i;
        }
        else {
          cost[i][j] = minimum(cost[i-1][j+1], cost[i][j+1], cost[i+1][j+1]);
          if (cost[i][j]==cost[i-1][j+1]) path[i][j] = i-1;
          else if (cost[i][j]==cost[i][j+1]) path[i][j] = i;
          else path[i][j] = i+1;
        }
        cost[i][j] += matrix[i][j];
        if (j==0 and cost[i][j] < final_cost) {
          final_cost = cost[i][j];
          min_row = i;
        }
      }
    }
  }

  int i = min_row;
  for (int j=0; j<num_cols; j++) {
    if (j<num_cols-1) cout << i+1 << " ";
    else cout << i+1;
    i = path[i][j];
  }
  cout << "\n";

  cout << final_cost << "\n";
}


int main()

{ 
  int num_rows, num_cols, aux;
  while (cin >> num_rows) 
  {
    memset(matrix, -1, sizeof(matrix));
    memset(cost, 0, sizeof(cost));

    cin >> num_cols;

    for (int i=0; i<num_rows; i++) {
      for (int j=0; j<num_cols; j++) {
        cin >> aux;
        matrix[i][j] = aux;
      }
    }

    memoized_tsp(num_rows, num_cols);
  }
}