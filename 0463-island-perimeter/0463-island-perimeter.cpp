class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<bool>> vis(row,vector<bool>(col, false));
        int dir[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                if(grid[i][j] == 1){
                    queue<pair<int, int>> qu;
                    qu.push({i, j});
                    vis[i][j] = true;
                    int peri =0 ;
                    while(!qu.empty()){
                        auto[a, b] = qu.front();
                        qu.pop();
                        for(auto& di: dir){
                            int nx = a + di[0], ny = b + di[1];
                            if(nx < 0 || nx >= row || ny < 0 || ny >= col || grid[nx][ny] == 0)peri++;
                            else if(vis[nx][ny] == false){
                                vis[nx][ny] = true;
                                qu.push({nx, ny});
                            }

                        }
                    }
                    return peri;
                }
            }
        }
        return 0;
    }
};