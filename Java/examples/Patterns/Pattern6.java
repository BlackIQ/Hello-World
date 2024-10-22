/*      *
        **
        ***
        ****
        *****

 */
public class Pattern6 {
    public static void main(String[] args) {
        int n = 5;
        int spaces= 4;
        for (int i = 1; i<=5; i++){
            for(int j = 1; j<= spaces ; j++){
                System.out.print(" ");
            }
            for (int k = 1; k<=i ; k++){
                System.out.print("*");
            }
            spaces--;
            System.out.println();
        }
    }
}
