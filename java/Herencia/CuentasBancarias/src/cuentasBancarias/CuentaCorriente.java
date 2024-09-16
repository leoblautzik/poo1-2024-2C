package cuentasBancarias;

public class CuentaCorriente extends Cuenta {

    private double descubierto;

    public CuentaCorriente(int dni, double descubierto) {
        super(dni);
        this.descubierto = descubierto;
    }

    @Override
    public boolean hayDineroSuficiente(double monto) {
        return super.getSaldo() + this.descubierto >= monto;
    }

    @Override
    public double get_dinero_disponible() {
        return super.getSaldo() + this.descubierto;
    }

    @Override
    public String toString() {
        return super.toString() + ", descubierto: " + this.descubierto;
    }

    public static void main(String[] args) {

        Cuenta cc = new CuentaCorriente(12345678, 50000);
        cc.depositar(30000);
        cc.extraer(60000);
        cc.extraer(20000);
        System.out.println(cc);
        System.out.println(cc.get_dinero_disponible());

    }

}
