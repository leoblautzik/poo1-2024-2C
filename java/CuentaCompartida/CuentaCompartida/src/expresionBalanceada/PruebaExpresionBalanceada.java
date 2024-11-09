package expresionBalanceada;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class PruebaExpresionBalanceada {
    ExpresionBalanceada eb = new ExpresionBalanceada();

    @Test
    public void ejemploBalanceada() {
        String expresion = "[()]{}{[()()]()}";
        assertTrue(eb.estaBalanceada(expresion));
    }

    @Test
    public void ejemploDesBalanceada() {
        String expresion = "[(])";
        assertFalse(eb.estaBalanceada(expresion));
    }

    @Test
    public void ejemploExpresionVacia() {
        String expresion = "";
        assertTrue(eb.estaBalanceada(expresion));
    }

    @Test
    public void ejemploExpresionUnSoloSimboloDeAbrir() {
        String expresion = "[";
        assertFalse(eb.estaBalanceada(expresion));
    }

    @Test
    public void ejemploExpresionUnSoloSimboloDeCerrar() {
        String expresion = "]";
        assertFalse(eb.estaBalanceada(expresion));
    }
}
