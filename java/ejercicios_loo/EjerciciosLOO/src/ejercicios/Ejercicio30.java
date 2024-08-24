/**
 * Escribir una función que reciba un arreglo de
 * enteros y devuelva true si el arreglo está ordenado de
 * mayor a menor y false si está desordenado.
 */
public class Ejercicio30 {

    static boolean estaOrdenadoDeMenorAmayor(int[] v) {
        for (int i = 0; i < v.length - 1; i++) {
            if (v[i] > v[i + 1]) {
                return false;
            }
        }

        return true;
    }

    static boolean estaOrdenadoDeMayorAmenor(int[] v) {
        for (int i = 0; i < v.length - 1; i++) {
            if (v[i] < v[i + 1]) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        int[] v = { 1, 2, 3, 4, 5, 6, 7, 8, 6 };
        int[] a = { 9, 8, 7, 6, 5, 4, 4, 4, 3, 2, 1 };
        int[] vacio = {};
        int[] uno = { 1 };
        int[] repe = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };

        // Ejercicio30 e30 = new Ejercicio30();

        System.out.println(estaOrdenadoDeMayorAmenor(v));
        System.out.println(estaOrdenadoDeMenorAmayor(v));
        System.out.println(estaOrdenadoDeMayorAmenor(a));
        System.out.println(estaOrdenadoDeMayorAmenor(vacio));
        System.out.println(estaOrdenadoDeMenorAmayor(vacio));
        System.out.println(estaOrdenadoDeMayorAmenor(uno));
        System.out.println(estaOrdenadoDeMenorAmayor(uno));
        System.out.println(estaOrdenadoDeMayorAmenor(repe));
        System.out.println(estaOrdenadoDeMenorAmayor(repe));

        for (int i = 0; i < repe.length; i++) {
            System.out.println(repe[i]);
        }

    }

}
