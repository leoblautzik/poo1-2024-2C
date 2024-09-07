public class App {
    public static void main(String[] args) {
        TarjetaBaja tb = new TarjetaBaja(100);
        System.out.println(tb.obtenerSaldo());
        tb.pagarViajeEnColectivo();
        System.out.println("Saldo despues de un viaje en bondi: " + tb.obtenerSaldo());
        tb.pagarViajeEnColectivo();
        System.out.println(tb.obtenerSaldo());
        tb.pagarViajeEnSubte();
        System.out.println(tb.obtenerSaldo());
        tb.pagarViajeEnSubte();
        System.out.println(tb.obtenerSaldo());
        tb.pagarViajeEnSubte();

        System.out.println(tb.contarViajes());

    }
}
