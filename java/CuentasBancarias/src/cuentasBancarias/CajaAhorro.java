package cuentasBancarias;

public class CajaAhorro extends Cuenta {

    private double reserva;

    public CajaAhorro(int dni) {
        super(dni);
        this.reserva = 0;
    }

    @Override
    public void extraer(double monto) {
        if (monto <= 0)
            throw new Error("Monto incorrecto");

        if (super.getSaldo() >= monto)
            super.setSaldo(super.getSaldo() - monto);
        else
            System.err.println("No te alcanza");
    }

    @Override
    public double getDineroDisponible() {
        return super.getSaldo() + this.reserva;
    }

    public void reservar(double monto) {
        if (monto <= 0)
            throw new Error("Monto incorrecto");

        if (super.getSaldo() >= monto) {
            reserva += monto;
            super.setSaldo(super.getSaldo() - monto);
        }
    }

    public void reponerDeLaReserva(double monto) {
        if (monto <= 0)
            throw new Error("Monto incorrecto");

        if (this.reserva > monto) {
            super.setSaldo(super.getSaldo() + monto);
            this.reserva -= monto;
        } else
            System.err.println("No te alcanza");
    }

    @Override
    public String toString() {
        return super.toString() + "CajaAhorro [reserva=" + reserva + "]";
    }

}
