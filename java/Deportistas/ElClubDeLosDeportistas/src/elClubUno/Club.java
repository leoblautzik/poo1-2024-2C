package elClubUno;

import java.util.ArrayList;

public class Club {

    private int numeroDeSocio = 100;
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

    public int getProximoNumerDeSocio() {
        this.numeroDeSocio++;
        return this.numeroDeSocio;
    }

    public void hacerVitalicio(Deportista d) {
        d.hacerVitalicio();
    }

    public static void main(String[] args) {
        Club elProgreso = new Club();

        Tenista rafa = new Tenista(elProgreso.getProximoNumerDeSocio(), 4);

        elProgreso.hacerVitalicio(rafa);

        System.out.println(rafa);

    }

}
