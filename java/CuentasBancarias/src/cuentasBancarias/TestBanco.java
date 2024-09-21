package cuentasBancarias;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestBanco {

    @Test
    public void creoCajaAhorroTest() {
        CajaAhorro ca = new CajaAhorro(123);
        assertEquals(0.0, ca.getSaldo());
        assertEquals(123, ca.getDni());
    }

    @Test
    public void depositoEnCAtest() {
        CajaAhorro ca = new CajaAhorro(123);
        ca.depositar(123456.79);
        assertEquals(123456.79, ca.getSaldo());
    }

    @Test
    public void transferirDeCCaCAtest() {
        CuentaCorriente cc = new CuentaCorriente(345, 20000);
        cc.depositar(10000);
        CajaAhorro ca = new CajaAhorro(123);
        cc.transferir(ca, 15000);
        assertEquals(-5000, cc.getSaldo());
        assertEquals(15000, ca.getSaldo());
        cc.transferir(ca, 15000);
        assertEquals(-20000, cc.getSaldo());
        assertEquals(30000, ca.getSaldo());
    }
}
