import java.util.Scanner;

/**
 * Tables
 */
public class Tables {

    public static void main(String[] args) {
        Scanner s = null;
        try {
            s = new Scanner(System.in);
            System.out.println("enter table number to end");
            int number = s.nextInt();
            System.out.println("enter ends table");
            int number1 = s.nextInt();
            for (int i = 1; i <= number; i++) {
                int k = 0;
                for (int j = 1; j <= number1; j++) {
                    if (j >= 10) {

                        System.out.println(i + " X " + j + " = " + i * j);
                    } else {

                        System.out.println(i + " X " + k + j + " = " + i * j);
                    }
                }
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            if (s != null)
                s.close();
        }

    }
}