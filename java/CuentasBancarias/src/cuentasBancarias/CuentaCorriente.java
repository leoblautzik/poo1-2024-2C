package cuentasBancarias;

public class CuentaCorriente extends Cuenta {

    private double descubierto;

    public CuentaCorriente(int dni, double descubierto) {
        super(dni);
        this.descubierto = descubierto;
    }

    @Override
    public void extraer(double monto) {
        if (monto <= 0)
            throw new Error("Monto incorrecto");

        if (super.getSaldo() + this.descubierto >= monto)
            super.setSaldo(super.getSaldo() - monto);
        else
            System.err.println("No te alcanza");
    }

    @Override
    public double getDineroDisponible() {
        return super.getSaldo() + this.descubierto;
    }

    @Override
    public String toString() {
        return super.toString() + "CuentaCorriente [descubierto=" + descubierto + "]";
    }

}
