package elClubUno;

import java.util.ArrayList;

public class Club {

    private static int numeroDeSocio = 100;
    private static double cuotaBase;

    private ArrayList<Deportista> socios;

    public Club() {
        cuotaBase = 30000.00;
        socios = new ArrayList<Deportista>();
    }

    public static double getCuotaBase() {
        return Club.cuotaBase;
    }

    public void agregarSocio(Deportista s) {
        this.socios.add(s);
    }

    public static int getProximoNumerDeSocio() {
        Club.numeroDeSocio++;
        return Club.numeroDeSocio;
    }

    public static void main(String[] args) {
        Club elProgreso = new Club();

        Tenista rafa = new Tenista(Club.getProximoNumerDeSocio(), 4);

        rafa.hacerVitalicio();

        System.out.println(rafa);

    }

}
