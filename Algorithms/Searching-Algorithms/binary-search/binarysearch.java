import java.util.Arrays;
public class binarysearch {

    public static int binarySearch(int[] arr, int target){
        int low = 0;
        int high = arr.length - 1;

        while(low <= high){
            int mid = (low + high)/ 2;

            if(arr[mid] == target){
                return mid;
            }else if(arr[mid] < target){
                low = mid + 1;
            }
                
            else{
                high = mid -1;
            }
        }
        return -1;
    }
    
    public static void main(String[] args){
        int[] arr = {1,260,23,54,7,8,89,0};
        Arrays.sort(arr);
        int target = 54;
        

        int result = binarySearch(arr, target);
        if(result == -1){
            System.out.println("Element not found");
        }
        else{
            System.out.println("Element " + target + " found at the index " + result);
        }
    }


}
