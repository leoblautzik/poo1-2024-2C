package elClubUno;

public class Basquetbolista extends Deportista {

    public Basquetbolista(int numeroDeSocio, int diasPorSemanaDeEntreno) {
        super(numeroDeSocio, diasPorSemanaDeEntreno);

    }

    @Override
    public double getCuotaMensual() {
        return super.getCuotaBase();
    }

}
