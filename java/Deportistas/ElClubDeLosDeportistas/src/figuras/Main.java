package figuras;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Circulo c1 = new Circulo(5);
        Elipse e1 = new Elipse(4, 5);

        Figura[] figuritas = new Figura[2];

        figuritas[0] = c1;
        figuritas[1] = e1;

        for (Figura figura : figuritas) {
            System.out.println(figura.getArea());

        }

        Arrays.sort(figuritas);

        for (Figura figura : figuritas) {
            System.out.println(figura.getArea());

        }
    }
}
