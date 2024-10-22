/*Write a program to print Fibonacci series of n terms where n is input by user :
        0 1 1 2 3 5 8 13 21 .....
        In the Fibonacci series, a number is the sum of the previous 2 numbers that came before it.
*/
import java.util.Scanner;
public class Fibonacci_series {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter term upto which you want to print the series:");
        int a = in.nextInt();
        Fibonacci(a);
    }
    public static void Fibonacci(int n){
        for(int i = 0 ; i<=n ; i++){
            int sum = 0 ;
            if(i==0 || i==1){
                System.out.println(i);
            }
            else {
                sum = (i-1)+(i-2);
                System.out.println(sum);
            }
        }
    }
}
