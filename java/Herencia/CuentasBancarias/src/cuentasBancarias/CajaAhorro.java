package cuentasBancarias;

public class CajaAhorro extends Cuenta {

    private double reserva;

    public CajaAhorro(int dni) {
        super(dni);
        this.reserva = 0.0;
    }

    @Override
    public boolean hayDineroSuficiente(double monto) {
        return this.getSaldo() >= monto;
    }

    @Override
    public double get_dinero_disponible() {
        return this.reserva + this.getSaldo();
    }

    public void reservar(double monto) {
        if (hayDineroSuficiente(monto)) {
            super.setSaldo(super.getSaldo() - monto);
            this.reserva += monto;
        }
    }

    public void recuperar(double monto) {
        if (this.reserva >= monto) {
            this.setSaldo(super.getSaldo() + monto);
        }
    }

}
