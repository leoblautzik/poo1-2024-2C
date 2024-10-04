package bibliotecaConLista;

public class Libro implements Comparable<Libro> {
    private String titulo;
    private String autor;
    private Genero genero;
    private int cantidadDePaginas;

    public Libro(String titulo, String autor, Genero genero, int cantidadDePaginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.cantidadDePaginas = cantidadDePaginas;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((titulo == null) ? 0 : titulo.hashCode());
        result = prime * result + ((autor == null) ? 0 : autor.hashCode());
        result = prime * result + ((genero == null) ? 0 : genero.hashCode());
        result = prime * result + cantidadDePaginas;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Libro other = (Libro) obj;
        if (titulo == null) {
            if (other.titulo != null)
                return false;
        } else if (!titulo.equals(other.titulo))
            return false;
        if (autor == null) {
            if (other.autor != null)
                return false;
        } else if (!autor.equals(other.autor))
            return false;
        if (genero != other.genero)
            return false;
        if (cantidadDePaginas != other.cantidadDePaginas)
            return false;
        return true;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public Genero getGenero() {
        return genero;
    }

    public int getCantidadDePaginas() {
        return cantidadDePaginas;
    }

    @Override
    public int compareTo(Libro otro) {
        if (this.genero.compareTo(otro.genero) == 0) {
            return this.autor.compareTo(otro.autor);
        } else
            return this.genero.compareTo(otro.genero);
    }

    @Override
    public String toString() {
        return "\n[titulo=" + titulo + ", autor=" + autor + ", genero=" + genero + ", cantidadDePaginas="
                + cantidadDePaginas + "]";
    }

}
