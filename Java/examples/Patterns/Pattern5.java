/*      *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *

 */
public class Pattern5 {
    public static void main(String[] args) {
        int n = 5;
        for (int i = 1; i<10; i++){
            if (i<=n){
                for(int j =1; j<=i; j++){
                    System.out.print("*");
                }
            }
            else {
                for(int k = 1 ; k<n ; k++){
                    System.out.print("*");
                }
                n--;
            }
            System.out.println();
        }
    }
}
