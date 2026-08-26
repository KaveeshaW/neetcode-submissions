class Node {
    private String url;
    private Node prev;
    private Node next;
    
    public Node() {
        this.url = "";
        this.prev = null;
        this.next = null;
    }

    public Node(String url) {
        this.url = url;
        this.prev = null;
        this.next = null;
    }
}

class BrowserHistory {
    Node curr;

    public BrowserHistory(String homepage) {
        Node visited = new Node(homepage);
        curr = visited;
    }
    
    public void visit(String url) {
        Node visited = new Node(url);
        visited.prev = curr;
        curr.next = visited;
        curr = curr.next;
    }
    
    public String back(int steps) {
        while(steps > 0 && curr.prev != null) {
            curr = curr.prev;
            steps--;
        }
        return curr.url;
    }
    
    public String forward(int steps) {
        while(steps > 0 && curr.next != null) {
            curr = curr.next;
            steps--;
        }
        return curr.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */