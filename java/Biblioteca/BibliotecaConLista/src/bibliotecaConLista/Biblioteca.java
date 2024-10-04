package bibliotecaConLista;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Biblioteca {

    private ArrayList<Libro> libros;

    public Biblioteca() {
        this.libros = new ArrayList<Libro>();
    }

    public int cuantosLibros() {
        return this.libros.size();
    }

    public void agregarLibro(String titulo, String autor, Genero genero, int paginas) {
        Libro libro = new Libro(titulo, autor, genero, paginas);
        this.libros.add(libro);

    }

    public String libroEnLaPosicion(int posicion) {
        if (posicion < 1 || posicion > libros.size())
            throw new Error("Posicion fiera de rango");

        return libros.get(posicion - 1).getTitulo();
    }

    public String libroEnLaUltimaPosicion() {
        int ultimaPosicion = libros.size();
        return this.libroEnLaPosicion(ultimaPosicion);
    }

    public Libro libroConMasPaginas() {
        int maxPag = libros.get(0).getCantidadDePaginas();
        Libro libroMax = libros.get(0);

        for (Libro cadaLibro : libros) {
            if (cadaLibro.getCantidadDePaginas() > maxPag) {
                maxPag = cadaLibro.getCantidadDePaginas();
                libroMax = cadaLibro;
            }

        }

        return libroMax;
    }

    /**
     * Se pueda consultar cuantos libros hay de determinado autor.
     */
    public int cuantosLibrosDelAutor(String autor) {
        int contador = 0;

        for (Libro cadaLibro : libros) {
            if (cadaLibro.getAutor().equals(autor)) {
                contador++;
            }
        }
        return contador;
    }

    /**
     * Devuelva una lista con todos los Libros de un autor que se pasa por
     * parámetro.
     */
    public List<Libro> librosDelAutor(String autor) {
        List<Libro> aux = new LinkedList<Libro>();

        for (Libro cadaLibro : libros) {
            if (cadaLibro.getAutor().equals(autor)) {
                aux.add(cadaLibro);
            }
        }

        return aux;
    }

    public void ordenarLibros() {

        Collections.sort(this.libros);
    }

    public void listarLibros() {
        System.out.println(libros);

    }

    public static void main(String[] args) {

        Biblioteca elNegrito = new Biblioteca();
        elNegrito.agregarLibro("Moby-Dick", "Melville", Genero.AVENTURA, 823);
        elNegrito.agregarLibro("Crepusculo", "Mayer", Genero.NOVELA, 789);
        elNegrito.agregarLibro("Cien años de soledad", "Gabriel García Márquez", Genero.NOVELA, 400);
        elNegrito.agregarLibro("El ingenioso hidalgo Don Quijote de la Mancha", "Miguel de Cervantes", Genero.NOVELA,
                900);
        elNegrito.agregarLibro("Crónicas de una muerte anunciada", "Gabriel García Márquez", Genero.NOVELA, 120);
        elNegrito.agregarLibro("Harry Potter y la piedra filosofal", "J.K. Rowling", Genero.AVENTURA, 309);
        elNegrito.agregarLibro("El Principito", "Antoine de Saint-Exupéry", Genero.INFANTILES, 96);

        elNegrito.ordenarLibros();
        elNegrito.listarLibros();
    }
}
