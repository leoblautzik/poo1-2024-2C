package elClubUno;

public class Tenista extends Deportista {

    public Tenista(int numeroDeSocio, int diasPorSemanaDeEntreno) {
        super(numeroDeSocio, diasPorSemanaDeEntreno);

    }

    // 50% adicional al valor de la cuota base
    // si entrenan menos de 3 días por semana
    @Override
    public double getCuotaMensual() {
        double cincuenta = 0;

        if (this.getDias() < 3)
            cincuenta = super.getCuotaBase() * 0.5;

        return super.getCuotaBase() + cincuenta * super.getDias();
    }
}
