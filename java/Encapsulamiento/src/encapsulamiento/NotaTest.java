package encapsulamiento;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class NotaTest {

  @Test
  public aprobadoTest() {
    Nota p1  = new Nota(7);
    assertTrue(p1.aprobado());
  }

}
