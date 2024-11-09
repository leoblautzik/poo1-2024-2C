package cuenta_compartida;

import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class CuentaCompartida {

    private Map<Integer, List<Consumo>> cuenta;
    private double cubierto; 

    public CuentaCompartida(){
        this.cuenta = new TreeMap<Integer,List<Consumo>>();             
    }

    public void agregarconsumo(Integer comensal, String descripcion, double precio){
        
    }

    public void agregarconsumo(Integer comensal, Consumo c){
        if(!cuenta.containsKey(comensal)){
            throw new Error();
        }
        else{
            
        }
        
    }

    public void mostrarConsumos(){
        for (Map.Entry<Integer, List<Consumo>> entry : cuenta.entrySet()) {
            Integer comensal = entry.getKey();
            List<Consumo> consumos = entry.getValue();
            System.out.println("Comensal: " + comensal);
            for (Consumo consumo : consumos) {
                System.out.println(consumo);;
                
            }
        }
    }
}
