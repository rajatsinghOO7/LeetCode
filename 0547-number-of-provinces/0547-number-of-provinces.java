class Solution {
    public int findCircleNum(int[][] isConnected) {
        List<List<Integer>> adjList = new ArrayList<>();
        int n = isConnected.length;
        for(int i=0; i<n; i++){
            adjList.add(new ArrayList<>());
        }

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(i == j)
                    continue;
                
                if(isConnected[i][j] == 1){
                    adjList.get(i).add(j);
                    adjList.get(j).add(i);
                }
            }
        }
        int count = 0;

        Set<Integer> visited = new HashSet<>();
        
        for(int i=0; i<n; i++){
            if(!visited.contains(i)){
                count++;
                dfs(i, adjList, visited);
            }
        }

        return count;
    }

    private void dfs(int node, List<List<Integer>> adjList, Set<Integer> visited){
        visited.add(node);

        for(int neighbour: adjList.get(node)){
            if(!visited.contains(neighbour)){
                dfs(neighbour, adjList, visited);
            }
        }
    }
}