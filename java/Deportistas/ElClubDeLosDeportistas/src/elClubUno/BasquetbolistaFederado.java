package elClubUno;

public class BasquetbolistaFederado extends Basquetbolista {

    public BasquetbolistaFederado(int numeroDeSocio, int diasPorSemanaDeEntreno) {
        super(numeroDeSocio, diasPorSemanaDeEntreno);

    }

    @Override
    public double getCuotaMensual() {
        return super.getCuotaBase() * 0.9;
    }

}
