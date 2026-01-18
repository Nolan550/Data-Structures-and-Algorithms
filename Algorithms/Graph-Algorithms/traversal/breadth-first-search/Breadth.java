import java.util.*;

public class Breadth {

    // Directions: up, right, down, left
    private static final int[] dx = {-1, 0, 1, 0};
    private static final int[] dy = {0, 1, 0, -1};

    static class Point {
        int x, y, dist;
        Point(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
    }

    public static int shortestPath(char[][] grid, int startX, int startY, int targetX, int targetY) {
        if (grid == null || grid.length == 0) return -1;

        int rows = grid.length;
        int cols = grid[0].length;

        boolean[][] visited = new boolean[rows][cols];
        Queue<Point> queue = new LinkedList<>();

        queue.offer(new Point(startX, startY, 0));
        visited[startX][startY] = true;

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            int x = current.x;
            int y = current.y;
            int dist = current.dist;

            // Found target
            if (x == targetX && y == targetY) {
                return dist;
            }

            // Explore 4 directions
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && nx < rows && 
                    ny >= 0 && ny < cols && 
                    !visited[nx][ny] && 
                    grid[nx][ny] != '#') {   // '#' = wall
                    
                    visited[nx][ny] = true;
                    queue.offer(new Point(nx, ny, dist + 1));
                }
            }
        }

        return -1; // no path found
    }

    public static void main(String[] args) {
        char[][] grid = {
            {'S', '.', '.', '#', '.'},
            {'.', '#', '.', '.', '.'},
            {'.', '.', '.', '#', '.'},
            {'#', '#', '.', '.', 'T'},
            {'.', '.', '.', '#', '.'}
        };

        int result = shortestPath(grid, 0, 0, 3, 4);
        System.out.println("Shortest path length: " + result);  // should print 7
    }
}