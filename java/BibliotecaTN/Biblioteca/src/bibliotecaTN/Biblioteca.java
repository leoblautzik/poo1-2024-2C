package bibliotecaTN;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Biblioteca {
    private ArrayList<Libro> libros;

    public Biblioteca() {

        this.libros = new ArrayList<Libro>();

    }

    // Se pueda consultar la cantidad de libros que contiene.
    public int cuantosLibros() {
        return this.libros.size();
    }

    /**
     * Se pueda agregar un libro indicando su título, autor, Genero y cantidad de
     * páginas,
     * siempre y cuando haya lugar en la Biblioteca.
     * Los Generos literarios que le gustan a éste bibiotecario son:
     * POESIA, CIENCIAFICCION, AVENTURA, NOVELA, HISTORIA, INFANTILES.
     */
    public void agregarLibro(String titulo, String autor, Genero genero, int paginas) {
        Libro nuevoLibro = new Libro(titulo, autor, genero, paginas);
        this.libros.add(nuevoLibro);
    }

    // Devuelva el título de un libro a partir de la posición.
    // pre: posicion debe estar entre 1 y la cantidad de libros.
    public String libroEnLaPosicion(int posicion) {
        if (posicion < 1 || posicion > this.cuantosLibros())
            throw new Error("Posicion fuera de la biblioteca");

        return this.libros.get(posicion - 1).getTitulo();
    }

    public String libroEnLaUltimaPosicion() {
        return this.libroEnLaPosicion(this.cuantosLibros());
    }

    // Devuelva el libro con más cantidad de páginas.
    public Libro libroConMasPaginas() {
        Libro maxiLibro = this.libros.get(0);

        // for (Libro cadaLibro : this.libros) {
        // if (cadaLibro.getCantidadDePaginas() > maxiLibro.getCantidadDePaginas()) {
        // maxiLibro = cadaLibro;
        // }
        // }
        for (int i = 1; i < this.cuantosLibros(); i++) {
            if (libros.get(i).getCantidadDePaginas() > maxiLibro.getCantidadDePaginas()) {
                maxiLibro = libros.get(i);
            }
        }

        return maxiLibro;
    }

    // Se pueda consultar cuantos libros hay de determinado autor.
    public int cuantosLibrosDelAutor(String autor) {
        int contador = 0;

        for (Libro libro : libros) {
            if (libro.getAutor().equals(autor)) {
                contador++;
            }
        }

        return contador;
    }

    // Devuelva una lista con todos los Libros de un autor que se pasa por
    // parámetro.
    public List<Libro> librosDelAutor(String autor) {
        List<Libro> aux = new LinkedList<Libro>();

        for (Libro libro : libros) {
            if (libro.getAutor().equals(autor)) {
                aux.add(libro);
            }
        }

        return aux;
    }

    // Calcule el tiempo (en minutos) que llevaría leer todos los libros, asumiendo
    // que se tarda 1 minuto por página.

    public int tiempoEnLeerTodosLosLibros() {
        int sumadorDeTiempos = 0;

        for (Libro libro : libros) {
            sumadorDeTiempos += libro.getCantidadDePaginas();
        }

        return sumadorDeTiempos;
    }

    // Informe por pantalla la cantidad de libros que hay por cada Genero literario.
    // Devuelve un Map con la cantidad de libros de cada genero
    public Map<Genero, Integer> cuantosLibrosPorGeneroLiterario() {
        Map<Genero, Integer> mapita = new TreeMap<Genero, Integer>();

        for (Libro cadaLibro : libros) {
            Genero key = cadaLibro.getGenero();
            int valor;

            if (mapita.containsKey(key)) {
                valor = mapita.get(key);
                valor++;
            } else {
                valor = 1;
            }
            mapita.put(key, valor);

        }

        return mapita;

    }

    public Map<Genero, List<Libro>> librosPorGeneroLiterario() {
        Map<Genero, List<Libro>> mapita = new TreeMap<Genero, List<Libro>>();

        for (Libro cadaLibro : libros) {
            Genero genero = cadaLibro.getGenero();
            List<Libro> librosDelGenero;

            if (mapita.containsKey(genero)) {
                librosDelGenero = mapita.get(genero);

            } else {
                librosDelGenero = new ArrayList<Libro>();
            }
            librosDelGenero.add(cadaLibro);
            mapita.put(genero, librosDelGenero);

        }

        return mapita;

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

        System.out.println(elNegrito.cuantosLibrosPorGeneroLiterario());
        System.out.println("\n");
        System.out.println(elNegrito.librosPorGeneroLiterario());
    }

}
