class ListNode {
    private int val;
    private ListNode next;
    private ListNode prev;

    public ListNode() {}

    public ListNode(int val) {
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class MyLinkedList {
    private ListNode head;
    private int size;

    public MyLinkedList() {
        head = new ListNode();
        size = 0;
    }
    
    public int get(int index) {
        if(index >= size) return -1;
        ListNode temp = head.next;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp.val;
    }
    
    public void addAtHead(int val) {
        ListNode newHead = new ListNode(val);
        newHead.next = head.next;
        newHead.prev = head;
        head.next = newHead;
        this.size++;
    }
    
    public void addAtTail(int val) {
        ListNode temp = head;
        while(temp.next != null) {
            temp = temp.next;
        }
        ListNode newTail = new ListNode(val);
        temp.next = newTail;
        newTail.prev = temp;
        this.size++;
    }
    
    public void addAtIndex(int index, int val) {
        if(index > this.size) return;
        ListNode temp = head;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        ListNode newNode = new ListNode(val);
        newNode.next = temp.next;
        newNode.prev = temp;
        temp.next = newNode;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if(index >= size) return;
        ListNode temp = head;
        for(int i = 0; i < index; i++) {
            temp = temp.next;
        }
        temp.next = temp.next.next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */