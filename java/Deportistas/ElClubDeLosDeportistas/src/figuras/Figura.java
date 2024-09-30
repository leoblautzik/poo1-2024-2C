package figuras;

public abstract class Figura implements Comparable<Figura> {

    private double area;

    public Figura(double area) {
        this.area = area;
    }

    @Override
    public int compareTo(Figura otra) {
        return Double.compare(this.area, otra.area);
    }

    public final double getArea() {
        return this.area;
    }

}
