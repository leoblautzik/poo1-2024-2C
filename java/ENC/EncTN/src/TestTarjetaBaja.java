import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class TestTarjetaBaja {

    @Test
    public void saldoInicialTest() {
        TarjetaBaja tb = new TarjetaBaja(100);
        double esperado = 100;
        double obtenido = tb.obtenerSaldo();
        assertEquals(esperado, obtenido, 0.01);
    }

    @Test
    public void saldoLuegoDerecargar() {
        TarjetaBaja tb = new TarjetaBaja(100);
        tb.cargar(50);
        double esperado = 150;
        double obtenido = tb.obtenerSaldo();
        assertEquals(esperado, obtenido, 0.01);
    }

    @Test
    public void saldoLuegoDePagarColectivo() {
        TarjetaBaja tb = new TarjetaBaja(100);
        double esperado = tb.obtenerSaldo() - TarjetaBaja.VIAJE_EN_COLECTIVO;
        tb.pagarViajeEnColectivo();
        assertEquals(esperado, tb.obtenerSaldo(), 0.01);
    }

    @Test
    public void saldoLuegoDePagarSubte() {
        TarjetaBaja tb = new TarjetaBaja(100);
        double esperado = tb.obtenerSaldo() - TarjetaBaja.VIAJE_EN_SUBTE;
        tb.pagarViajeEnSubte();
        assertEquals(esperado, tb.obtenerSaldo(), 0.01);
    }

    @Test
    public void saldoJustitoParaUnViajeEnSubte() {
        TarjetaBaja tb = new TarjetaBaja(19.50);
        tb.pagarViajeEnSubte();
        assertEquals(0, tb.obtenerSaldo(), 0.01);
    }
}
