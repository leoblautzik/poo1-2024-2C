import java.util.Scanner;

public class Ejercicio_8 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese un valor entero positivo: ");
        int v = entrada.nextInt();
        while (v > 0) {
            if (v % 2 == 0) {
                System.out.println("Es par");
            } else {
                System.out.println("Es impar");
            }
            System.out.print("Ingrese un valor entero positivo: ");
            v = entrada.nextInt();
        }
        entrada.close();

    }

}
