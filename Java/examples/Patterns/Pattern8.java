/*      *
       ***
      *****
     *******
    *********

 */
public class Pattern8 {
    public static void main(String[] args) {
        int n = 5;
        int m = 1;
        int space = 4;
        for(int i = 1 ; i<=n ; i++){
            for(int j = 1 ; j<=space ; j++){
                System.out.print(" ");
            }
            for (int k = 1 ; k<=m ; k++){
                System.out.print("*");
            }
            space--;
            m=m+2;
            System.out.println();
        }
    }
}
