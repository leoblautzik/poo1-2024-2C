package cuentasBancarias;

public abstract class Cuenta {

    private int dni;
    private double saldo;

    public Cuenta(int dni) {
        this.dni = dni;
        this.saldo = 0;
    }

    protected void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            throw new Error("Monto invalido");
        }
        this.saldo += monto;
    }

    public abstract void extraer(double monto);

    public abstract double getDineroDisponible();

    public void transferir(Cuenta destino, double monto) {
        if (monto <= 0) {
            throw new Error("Monto invalido");
        }
        this.extraer(monto);
        destino.depositar(monto);
    }

    @Override
    public String toString() {
        return "Cuenta [dni=" + dni + ", saldo=" + saldo + "]";
    }

    public int getDni() {
        return dni;
    }

    public double getSaldo() {
        return saldo;
    }

}
