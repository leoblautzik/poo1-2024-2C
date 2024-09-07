public class TarjetaBaja {

    private double saldo;
    private int viajesEnColectivo;
    private int viajesEnSubte;

    public static double VIAJE_EN_SUBTE = 19.50;
    public static double VIAJE_EN_COLECTIVO = 21.50;

    /**
     * post: saldo de la Tarjeta en saldoInicial.
     */
    public TarjetaBaja(double saldoInicial) {
        saldo = saldoInicial;
        viajesEnColectivo = 0;
        viajesEnSubte = 0;

    }

    /**
     * post: devuelve el saldo actual de la Tarjeta
     */
    public double obtenerSaldo() {
        return saldo;
    }

    /**
     * post: agrega el monto al saldo de la Tarjeta.
     */
    public void cargar(double monto) {
        saldo += monto;
    }

    /**
     * pre : saldo suficiente.
     * post: utiliza 21.50 del saldo para un viaje en colectivo.
     */
    public void pagarViajeEnColectivo() {
        if (saldo >= VIAJE_EN_COLECTIVO) {
            saldo -= VIAJE_EN_COLECTIVO;
            viajesEnColectivo++;
        }
    }

    /**
     * pre : saldo suficiente.
     * post: utiliza 19.50 del saldo para un viaje en subte.
     */
    public void pagarViajeEnSubte() {
        if (saldo >= VIAJE_EN_SUBTE) {
            saldo -= VIAJE_EN_SUBTE;
            viajesEnSubte++;
        }
    }

    /**
     * post: devuelve la cantidad de viajes realizados.
     */
    public int contarViajes() {

        return viajesEnColectivo + viajesEnSubte;
    }

    /**
     * post: devuelve la cantidad de viajes en colectivo.
     */
    public int contarViajesEnColectivo() {

        return viajesEnColectivo;
    }

    /**
     * post: devuelve la cantidad de viajes en subte.
     */
    public int contarViajesEnSubte() {
        return viajesEnSubte;
    }
}