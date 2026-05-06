package Alg_Complexity;

import java.util.Arrays;
import java.util.stream.Stream;

public class insertion {
    

    public static void main(String[] args) {
        int[] arr = {7,3,1,2,4,8};
        Arrays.stream(arr).forEach(e -> System.out.print(e + " "));
        System.out.println();
        
        for (int i = 0; i < arr.length; i++) {
            int a = arr[i];
            for (int j = 1; j < arr.length; j++) {
                if(a > arr[j]){
                    int temp = arr[j];
                    arr[j] = a;
                    a = temp;
                    arr[i]=a;
                }
            }
        }
        
        Arrays.stream(arr).forEach(e -> System.out.print(e + " "));
    }
}
