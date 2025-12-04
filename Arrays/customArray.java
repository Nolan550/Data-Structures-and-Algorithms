
public class customArray{

    private int [] data;
    private int size;

    public customArray(int capacity){
        data = new int[capacity];
        size = 0;
    }


    public void add(int value){
        if(size == data.length){
            resize();
        }
        data[size] = value;
        size++;
    }

    private void resize(){
        int[] newData = new int[data.length * 2];
        for(int i = 0; i < data.length; i++){
            newData[i] = data[i];
        }
        data = newData;
    }

    public int get(int index){
        if(index < 0 || index >= size){
            throw new IndexOutOfBoundsException("Index is out of bound");
        }
        return data[index];
    }

    public void print(){
        for(int i = 0; i < size; i++){
            System.out.println(data[i]);
        }
    }

    public int size(){
        return size;
    }

    public static void main(String[] args){
        customArray array1 = new customArray(7);

       
        array1.add(7);
        array1.add(23);
        array1.add(21);
        array1.add(45);
        array1.add(56);
        array1.add(87);
        array1.add(76);
        array1.add(743);
        

        array1.print();
        System.out.println("The size of an array is:" + array1.size());
        System.out.println( array1.get(3));
    }
}
