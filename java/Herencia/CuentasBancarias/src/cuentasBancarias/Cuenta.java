package cuentasBancarias;

public abstract class Cuenta {

    private int dni;
    private double saldo = 0.0;

    public Cuenta(int dni) {
        this.dni = dni;
    }

    public abstract boolean hayDineroSuficiente(double monto);

    public abstract double get_dinero_disponible();

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            throw new Error("Montomincorrecto");
        }
        this.setSaldo(monto);
    }

    public void extraer(double monto) {
        if (hayDineroSuficiente(monto)) {
            this.setSaldo(this.getSaldo() - monto);
        }
    }

    /**
     * this es la cuenta origen
     * 
     * @param destino
     * @param monto
     */
    public void transferir(Cuenta destino, double monto) {
        if (this.hayDineroSuficiente(monto)) {
            this.extraer(monto);
            destino.depositar(monto);
        }
    }

    @Override
    public String toString() {
        return "dni: " + dni + ", saldo: " + saldo;
    }

}
