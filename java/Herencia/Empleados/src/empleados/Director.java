package empleados;

public class Director extends Gerente {

    private double adicional;

    public Director(String nombre, double sueldoBasico, String departamento, double adicional) {
        super(nombre, sueldoBasico, departamento);
        this.adicional = adicional;
    }

    public double getSalario() {
        return super.getSalario() + this.adicional;
    }
}
