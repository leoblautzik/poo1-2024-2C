package bibliotecaTN;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.ArrayList;
import org.junit.jupiter.api.Test;

public class BibliotecaTest {

    @Test
    public void cuantosLibrosTest() {

        Biblioteca elNegrito = new Biblioteca();
        assertEquals(0, elNegrito.cuantosLibros());
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        elNegrito.agregarLibro("Crepusculo - Luna Nueva", "Mayer", Genero.NOVELA, 689);
        assertEquals(3, elNegrito.cuantosLibros());
    }

    @Test
    public void libroEnLaPosicionTest() {

        Biblioteca elNegrito = new Biblioteca();
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        String esperado = "Moby-Dick";
        String obtenido = elNegrito.libroEnLaPosicion(1);
        assertEquals(esperado, obtenido);

    }

    @Test
    public void libroEnLaUltimaPosicionTest() {

        Biblioteca elNegrito = new Biblioteca();
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        String esperado = "Crepusculo";
        String obtenido = elNegrito.libroEnLaUltimaPosicion();
        assertEquals(esperado, obtenido);

    }

    // @Test(expected = Error.class)
    // public void libroaPosicionFueraDeRangoTest() {

    // Biblioteca elNegrito = new Biblioteca();
    // elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
    // elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
    // String esperado = "Crepusculo";
    // String obtenido = elNegrito.libroEnLaPosicion(3);
    // assertEquals(esperado, obtenido);

    // }

    @Test
    public void libroconMasPaginasTest() {

        Biblioteca elNegrito = new Biblioteca();
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        elNegrito.agregarLibro("Cien años de soledad", "Gabriel García Márquez", Genero.NOVELA, 400);
        elNegrito.agregarLibro("El ingenioso hidalgo Don Quijote de la Mancha", "Miguel de Cervantes", Genero.NOVELA,
                900);
        elNegrito.agregarLibro("Crónicas de una muerte anunciada", "Gabriel García Márquez", Genero.NOVELA, 120);
        elNegrito.agregarLibro("Harry Potter y la piedra filosofal", "J.K. Rowling", Genero.AVENTURA, 309);
        elNegrito.agregarLibro("El Principito", "Antoine de Saint-Exupéry", Genero.INFANTILES, 96);
        Libro esperado = new Libro("El ingenioso hidalgo Don Quijote de la Mancha", "Miguel de Cervantes",
                Genero.NOVELA, 900);
        assertEquals(esperado, elNegrito.libroConMasPaginas());
    }

    @Test
    public void LibrosDelAutorTest() {

        Biblioteca elNegrito = new Biblioteca();
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        elNegrito.agregarLibro("Crepusculo - Nueva Luna", "Mayer", Genero.NOVELA,
                689);

        ArrayList<Libro> librosEsperados = new ArrayList<Libro>();
        librosEsperados.add(new Libro("Crepusculo", "Mayer", Genero.NOVELA, 789));
        librosEsperados.add(new Libro("Crepusculo - Nueva Luna", "Mayer", Genero.NOVELA, 689));

        assertEquals(librosEsperados, elNegrito.librosDelAutor("Mayer"));
    }
}
