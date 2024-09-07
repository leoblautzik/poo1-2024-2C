public class Nota {

    private int valorNota;

    private boolean esNotaValida(int valor) {
        return (valor >= 0 && valor <= 10);
    }

    /**
     * pre : valorInicial está comprendido entre 0 y 10.
     * post: inicializa la Nota con el valor indicado.
     */
    public Nota(int valorInicial) {
        if (!esNotaValida(valorInicial)) {
            throw new Error("Nota inválida");
        }
        this.valorNota = valorInicial;
    }

    /**
     * post: devuelve el valor numérico de la Nota, comprendido entre 0 y 10.
     */
    public int obtenerValor() {
        return this.valorNota;
    }

    /**
     * post: indica si la Nota permite o no la aprobación.
     */
    public boolean aprobado() {
        return this.obtenerValor() >= 4;
    }

    /**
     * post: indica si la Nota implica desaprobación.
     */
    public boolean desaprobado() {
        return !this.aprobado();
    }

    /**
     * pre : nuevoValor está comprendido entre 0 y 10.
     * post: modifica el valor numérico de la Nota, cambiándolo por nuevoValor,
     * siempre y cuando nuevoValor sea superior al valor numérico actual de la Nota.
     */
    public void recuperar(int nuevoValor) {
        if (!esNotaValida(nuevoValor)) {
            throw new Error("Nota inválida");
        }

        if (nuevoValor > this.obtenerValor()) {
            this.valorNota = nuevoValor;
        }
    }

    public static void main(String[] args) {
        Nota parcial1 = new Nota(8);
        parcial1.recuperar(6);
        System.out.println("Nota parcial 1: " + parcial1.obtenerValor());
        System.out.println(parcial1.aprobado());
        System.out.println(parcial1.desaprobado());
        Nota parcial2 = new Nota(2);
        System.out.println("Nota parcial 2: " + parcial2.obtenerValor());
        System.out.println("Esta aprobado ?: " + parcial2.aprobado());
        System.out.println("Esta desaprobado?: " + parcial2.desaprobado());
        parcial2.recuperar(7);
        System.out.println("Recupera");
        System.out.println("Nota parcial2: " + parcial2.obtenerValor());
        System.out.println(parcial2.aprobado());
        System.out.println(parcial2.desaprobado());

        Nota examenFinal = new Nota(11);

    }

}
