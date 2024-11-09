package bibliotecaConLista;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

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

    // Informe por pantalla la cantidad de libros que hay por cada Genero literario.
    public Map<Genero, Integer> cuantosLibrosPorGeneroLiterario() {
        Map<Genero, Integer> mapita = new HashMap<Genero, Integer>();

        for (Libro libro : libros) {

            Genero clave = libro.getGenero();
            int valor;

            if (mapita.containsKey(clave)) {
                // actualizar
                valor = mapita.get(clave) + 1;
            } else {
                // nueva entrada
                valor = 1;
            }
            // Hacer put actualizado
            mapita.put(clave, valor);

        }

        return mapita;

    }

    /** Devuelve un mapa con los libros que tengo de cada genero */
    public Map<Genero, List<Libro>> librosPorGeneroLiterario() {
        Map<Genero, List<Libro>> mapita = new HashMap<Genero, List<Libro>>();

        for (Libro libro : libros) {

            Genero genero = libro.getGenero();
            List<Libro> listaDeLibros;

            if (mapita.containsKey(genero)) {
                listaDeLibros = mapita.get(genero);
            } else {
                listaDeLibros = new ArrayList<Libro>();
            }
            listaDeLibros.add(libro);
            mapita.put(genero, listaDeLibros);
        }

        return mapita;
    }

    public String mostrarLibrosPorGeneroLiterario(Map<Genero, List<Libro>> m) {
        String s = "";
        List<Libro> lista;

        for (Map.Entry<Genero, List<Libro>> cadaFila : m.entrySet()) {

            Genero genero = cadaFila.getKey();
            s += "\n" + genero + "\n";
            lista = cadaFila.getValue();
            for (Libro libro : lista) {
                s += libro.toString() + "\n";
            }
        }

        return s;
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
        elNegrito.agregarLibro("Dracula", "Bram Stocker", Genero.TERROR, 345);

        elNegrito.ordenarLibros();
        elNegrito.listarLibros();
        System.out.println(elNegrito.cuantosLibrosPorGeneroLiterario());
        System.out.println(elNegrito.mostrarLibrosPorGeneroLiterario(elNegrito.librosPorGeneroLiterario()));
    }
}
