package elClubUno;

public abstract class Deportista {

    private int numeroDeSocio;
    private int diasPorSemanaDeEntreno;
    private static double cuotaBase = Club.getCuotaBase();
    private boolean esVitalicio = false;

    public Deportista(int n, int d) {
        if (d < 1 || d > 7)
            throw new Error("Cantidad de dias incorrecta");
        this.numeroDeSocio = n;
        this.diasPorSemanaDeEntreno = d;
    }

    public double getCuotaBase() {
        double descuento = 0;
        if (this.esVitalicio)
            descuento = 0.5;

        return Deportista.cuotaBase * (1 - descuento);
    }

    public abstract double getCuotaMensual();

    public double getDias() {
        return this.diasPorSemanaDeEntreno;
    }

    void hacerVitalicio() {
        this.esVitalicio = true;
    }

    @Override
    public String toString() {
        return "Deportista [numeroDeSocio=" + numeroDeSocio + ", diasPorSemanaDeEntreno=" + diasPorSemanaDeEntreno
                + ", esVitalicio=" + esVitalicio + ", Cuota Mensual: " + this.getCuotaMensual() + "]";
    }

}
