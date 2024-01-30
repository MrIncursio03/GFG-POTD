/*

Author : Shuvam Kumar Singh
Date : 30/01/2024
Problem : LCS of three strings
Difficulty : Medium

*/


class Solution
{
    public:

        int LCSof3 (string A, string B, string C, int n1, int n2, int n3)
        {
            int dp[n1 + 1][n2 + 1][n3 + 1];
            
            for(int i = 0; i < n1 + 1; i++){
                for(int j = 0; j < n2 + 1; j++){
                    for(int k = 0; k < n3 + 1; k++)
                        dp[i][j][k] = 0;
                }
            }
            
            for(int i = n1 - 1; i > -1; i--){
                for(int j = n2 - 1; j > -1; j--){
                    for(int k = n3 - 1; k > -1; k--){
                        if(A[i] == B[j] and A[i] == C[k]){
                            dp[i][j][k] = 1 + dp[i + 1][j + 1][k + 1];
                        }
                        else{
                            dp[i][j][k] = max({dp[i + 1][j][k], dp[i][j + 1][k], dp[i][j][k + 1]});
                        }
                    }
                }
            }
            
            return dp[0][0][0];
        }
};
