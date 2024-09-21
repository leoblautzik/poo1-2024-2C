package cuentasBancarias;

import java.util.ArrayList;

public class Banco {

    ArrayList<Cuenta> cuentas;

    public Banco() {
        this.cuentas = new ArrayList<Cuenta>();
    }

    public CuentaCorriente abrirCuentaCorriente(int dni, double descubierto) {
        return new CuentaCorriente(dni, descubierto);
    }

    public CajaAhorro abrirCajaDeAhorro(int dni) {
        return new CajaAhorro(dni);
    }

    public void agregarCuenta(Cuenta c) {
        this.cuentas.add(c);
    }

    public void listarCuentas() {
        for (Cuenta cadaCuenta : this.cuentas) {
            System.out.println(cadaCuenta);
        }
    }

    public static void main(String[] args) {
        Banco coban = new Banco();

        CajaAhorro ca1 = coban.abrirCajaDeAhorro(12345678);
        CuentaCorriente cc1 = coban.abrirCuentaCorriente(3456123, 25000);
        CajaAhorro ca2 = coban.abrirCajaDeAhorro(5671245);

        coban.agregarCuenta(ca2);
        coban.agregarCuenta(cc1);
        coban.agregarCuenta(ca1);

        coban.listarCuentas();

        ca1.depositar(100000);
        ca1.reservar(20000);
        cc1.depositar(50000);
        cc1.extraer(34567.67);
        cc1.transferir(ca2, 60000);
        System.out.println("-------------------------------------");
        coban.listarCuentas();

    }

}
