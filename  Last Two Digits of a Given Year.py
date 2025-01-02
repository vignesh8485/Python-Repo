import java.util.Scanner;

public class LastTwoDigitsOfYear {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        int lastTwoDigits = year % 100;
        System.out.printf("%02d\n", lastTwoDigits);
    }
}