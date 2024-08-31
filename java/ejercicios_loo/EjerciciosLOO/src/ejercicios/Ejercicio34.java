public class Ejercicio34 {

    static int[] mezcla(int[] a, int[] b) {
        int[] resultado = new int[a.length + b.length];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < a.length && j < b.length) {
            if (a[i] < b[j]) {
                resultado[k] = a[i];
                i++;
            } else {
                resultado[k] = b[j];
                j++;
            }
            k++;
        }
        if (i == a.length) {
            while (j < b.length) {
                resultado[k] = b[j];
                k++;
                j++;
            }
        } else {
            while (i < a.length) {
                resultado[k] = a[i];
                k++;
                i++;
            }
        }
        return resultado;
    }

    public static void main(String[] args) {
        int[] a = { 1, 2, 3 };
        int[] b = { 3, 5, 7 };

        int[] resultado = mezcla(b, a);
        for (int r : resultado)
            System.out.print(r + " ");

    }
}
