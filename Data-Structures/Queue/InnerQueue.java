class Node{
    int data;
    Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class Queue{
    private Node front, rear;
    private int size;

    public Queue(){
        rear = front = null;
        size = 0;
    }
    

    public void enqueue(int data){
        Node newNode = new Node(data);
        if(front == null){
            rear = newNode;
            size++;
        }
        else{
            rear.next = newNode;
            newNode = rear;
        }
        size++;
    }
    public int dequeue(){
        if(front == null){
            System.out.println("Queue is empty.");
            return -1;
        }
        int poppedData = front.data;
        front = front.next;
        if(front == null){
            rear = null;
        }
        return data;
        size--;
    }

    public boolean isEmpty(){
        return front == null;
    }

    public int peek(){
        if(isEmpty()){
            System.out.println("The queue is empty.");
            return -1;
        }
        return front.data;
    }
    public int size(){
        return size;
    }
    
}

public class InnerQueue {

    public static void main(String[] args){
        Queue q1 = new Queue();

       
        System.out.println(q1.size());
        q1.enqueue(12);
        q1.enqueue(13);
        q1.enqueue(14);
        q1.enqueue(15);
        q1.enqueue(16);
        q1.enqueue(17);
        q1.enqueue(18);

        System.out.println(q1.size());
        System.out.println(q1.dequeue());
        System.out.println(q1.peek());
        
    }
}