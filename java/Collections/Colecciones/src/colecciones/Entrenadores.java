package colecciones;

import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Map.Entry;

/*Por ejemplo, si dicciEntrena, 
en la clave “Bielsa” contiene la lista [“Juan”, “Alberto”], 
y en la clave “Alvarez” contiene la lista [“Tom”, “Alberto”, “Vero”], 
el resultado debe ser otro diccionario de la forma:
“Alberto”, “Alvarez”, “Bielsa”
“Juan”, “Bielsa”
“Tom”, “Alvarez”
“Vero”, “Alvarez” 
*/

public class Entrenadores {

    public Map<String, List<String>> entrenadosPor(Map<String, List<String>> entrenadores) {

        TreeMap<String, List<String>> entrenados = new TreeMap<String, List<String>>();
        List<String> listaEntrenadores;

        for (Entry<String, List<String>> cu : entrenadores.entrySet()) {
            String entrenador = cu.getKey();
            List<String> socios = cu.getValue();

            for (String cadaSocio : socios) {
                listaEntrenadores = entrenados.getOrDefault(cadaSocio, new LinkedList<String>());
                listaEntrenadores.add(entrenador);
                entrenados.put(cadaSocio, listaEntrenadores);

            }

        }

        return entrenados;
    }

    public static void main(String[] args) {
        List<String> entrenadosPorBielsa = new LinkedList<>();
        entrenadosPorBielsa.add("Juan");
        entrenadosPorBielsa.add("Alberto");
        entrenadosPorBielsa.add("Vero");
        entrenadosPorBielsa.add("Tucu");
        List<String> entrenadosPorAlvarez = new LinkedList<>();
        entrenadosPorAlvarez.add("Tom");
        entrenadosPorAlvarez.add("Vero");
        entrenadosPorAlvarez.add("Alberto");
        Map<String, List<String>> dicc = new TreeMap<String, List<String>>();
        dicc.put("Bielsa", entrenadosPorBielsa);
        dicc.put("Alvarez", entrenadosPorAlvarez);

        Entrenadores e = new Entrenadores();

        System.out.println(e.entrenadosPor(dicc));

    }
}

// for (Map.Entry<String, List<String>> cu : entrenadores.entrySet()) {
// String entrenador = cu.getKey();
// List<String> socios = cu.getValue();
// for (String s : socios) {
// List<String> l;
// l = entrenados.getOrDefault(s, new LinkedList<String>());
// l.add(entrenador);
// entrenados.put(s, l);
// }
// }