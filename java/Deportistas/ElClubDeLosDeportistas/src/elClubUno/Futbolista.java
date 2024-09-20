package elClubUno;

public class Futbolista extends Deportista {

    public Futbolista(int numeroDeSocio, int diasPorSemanaDeEntreno) {
        super(numeroDeSocio, diasPorSemanaDeEntreno);

    }

    // más un plus por uso de cancha del 10% de la cuota
    // base por cada día que entrena,
    @Override
    public double getCuotaMensual() {
        double diego = super.getCuotaBase() * 0.1;
        return super.getCuotaBase() + diego * super.getDias();
    }

}
