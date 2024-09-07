package encapsulamiento;
class Cubo {
    
    private double lado;

    /**
     * pre : longitudLado es un valor mayor a 0.
     * post: inicializa el cubo a partir de la longitud de lado dada
     */
    public Cubo (double longitudLado) { 
        if(longitudLado <= 0){
            throw new Error("El lado debe ser mayor que cero");
        }
        this.lado=longitudLado;
    }

    /**
     * post: devuelve la longitud de todos los lados del cubo
     */
    public double getLado() {
        return this.lado;
     }
    
    /**
     * pre : longitudLado es un valor mayor a 0.
     * post: cambia la longitud de todos los lados del cubo
     */
    public void setLado(double longitudLado) { 
        if(longitudLado <= 0){
            throw new Error("El lado debe ser mayor que cero");
        }
        this.lado = longitudLado;

    }
    
    /**
     * post: devuelve el área de la superficie de las caras del cubo
     */
    public double obtenerAreaCara() { }
    
    /**
     * pre: areaCara es un valor mayor a 0.
     * post: cambia el área de las caras del cubo
     */
    public void cambiarAreaCara(double areaCara) { }

    /**
     * post: devuelve el volumen que encierra el cubo
     */
    public double obtenerVolumen() { }

    /**
     * pre: volumen es un valor mayor a 0.
     * post: cambia el volumen del cubo
     */
    public void cambiarVolumen(double volumen) { }
}