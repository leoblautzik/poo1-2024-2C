package ejercicios;

import java.util.Scanner;

/**
 * Leer tres valores numéricos enteros, indicar cual es el mayor,
 * cuál es el del medio y cuál el menor.
 * Considerar que los tres valores son diferentes.
 */

public class Ejercicio06 {

    public static void main(String[] args) {
        int mayor, medio, menor;
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese un valor entero: ");
        int a = sc.nextInt();
        System.out.println("Ingrese otro valor entero: ");
        int b = sc.nextInt();
        System.out.println("Ingrese un valor entero mas: ");
        int c = sc.nextInt();
        sc.close();

        mayor = a;
        if (b > a) {
            medio = a;
            mayor = b;
        } else {
            medio = b;
        }
        if (c > mayor) {
            menor = medio;
            medio = mayor;
            mayor = c;
        } else if (c > medio) {
            menor = medio;
            medio = c;
        } else {
            menor = c;
        }

        System.out.println("Mayor: " + mayor + ", Medio: " + medio + ", Menor: " + menor);
    }
}
