class Node{
    int data;
    Node next;

    Node(int data){
        this.data = data;
        this.next = null;
    }
}

class myStack{
    private Node top;
    private int size;

    public myStack(){
        top = null;
        size = 0;
    }

    public void push(int data){
        Node newNode = new Node(data);
        newNode.next = top;
        top = newNode;
        size++;

    }
    public int pull(){
        if(top == null){
            throw new IllegalStateException("Stack is empt");
        }
        int pulled = top.data;
        top = top.next;
        size--;
        return pulled;
    }

    public boolean isEmpty(){
        return top == null;
    }

    public void display(){
        if(isEmpty()){
            System.out.println("Stack is empty");
        }
        else{
            Node current = top;
            System.out.println("Stack:");
            while(current != null){
                System.out.print(current.data + " ");
            
                current = current.next;
            
            }
        System.out.println("END");
        }
    }

    public int peek(){
        if (isEmpty()){
            throw new IllegalStateException("Stack is empty");
            
        }
        return top.data;
    }
}

public class Stack {

    public static void main(String[] args){
        myStack s1 = new myStack();


        s1.display();
        s1.push(10);
        s1.push(11);
        s1.push(12);
        s1.push(13);
        s1.push(14);
        s1.push(15);
        s1.push(16);
        s1.push(17);
        s1.push(18);
        s1.display();
        System.out.println("Popped element: " + s1.pull());
        System.out.println(s1.peek());



    }
}