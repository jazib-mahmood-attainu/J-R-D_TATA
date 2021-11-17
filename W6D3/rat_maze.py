def No_of_ways(x,y,n,m,grid):
    if x>=n:
        return 0
    if y>=m:
        return 0
    if grid[x][y]==1:
        return 0
    if x == n-1 and y == m-1:
        return 1

    ans = No_of_ways(x,y+1,n,m,grid) + No_of_ways(x+1,y,n,m,grid) 
    return ans


if __name__=="__main__":
    grid = [[0,0,1,], [0,0,0],[1,0,0]]
    n = len(grid)
    m = len(grid[0])
    res = No_of_ways(0,0,n,m,grid)
    print(f"{res} no of ways are there")
