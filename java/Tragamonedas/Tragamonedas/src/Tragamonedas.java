public class Tragamonedas {

    private Tambor t1;
    private Tambor t2;
    private Tambor t3;

    /**
     * post: los 3 Tambores del Tragamonedas están en la posición 1.
     */
    public Tragamonedas() {
        t1 = new Tambor();
        t2 = new Tambor();
        t3 = new Tambor();
    }

    /**
     * post: activa el Tragamonedas haciendo girar sus 3 Tambores.
     */
    public void activar() {
        t1.girar();
        t2.girar();
        t3.girar();
    }

    /**
     * post: indica si el Tragamonedas entrega un premio a partir de la posición de
     * sus 3 Tambores.
     */
    public boolean entregaPremio() {
        return (t1.obtenerPosicion() == t2.obtenerPosicion() && t1.obtenerPosicion() == t3.obtenerPosicion());
    }

    /**
     * post: obtiene la posición del iésimo tambor del Tragamonedas
     * pre: i => 0; i < n (n = cantidad de tambores)
     */
    // public int obtenerPosicionDelTambor(int i) { }

    @Override
    public String toString() {
        return "[" + t1.toString() + t2.toString() + t3.toString() + "]";
    }

    public static void main(String[] args) {
        Tragamonedas laCueva = new Tragamonedas();

        laCueva.activar();
        int contadorDeMonedas = 0;

        while (!laCueva.entregaPremio()) {
            laCueva.activar();
            System.out.println(laCueva);
            contadorDeMonedas++;
        }
        // System.out.println(laCueva);
        System.out.println("luego de: " + contadorDeMonedas + " intentos");
    }
}
