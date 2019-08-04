import java.util.*;

class TablaPeriodica {
    private static Elemento[] elementos;
    private static HashMap<String, Elemento> elementoNumero;

    TablaPeriodica() {
        elementoNumero = new HashMap<>();
        elementos = readElements();
    }

    private Elemento[] readElements() {
        Reader reader = new Reader("NombresDeElementos.txt");
        Elemento[] els = new Elemento[reader.lines.size()];
        for (String s : reader.lines) {
            String[] section = s.split("\\s+");
            String name = section[0];
            String acronym = section[1];
            int number = Integer.parseInt(section[2]);
            double mass = Double.parseDouble(section[3]);
            Elemento e = new Elemento(name, acronym, number, mass);
            els[elementoNumero.size()] = e;
            elementoNumero.put(acronym, e);
        }
        return els;
    }

    private static void print(String s) {
        System.out.println(s);
        System.out.println();
    }

    private static Elemento processSyntax(String input) {
        if (input == null) {
            print("Ingresa nombre, abreviación o número");
        }
        if (input.matches(".*\\d.*")) {
            Integer n = Integer.parseInt(input);
            if (n > elementos.length || n < 0) {
                print("Ingresa un número apropiado");
                return null;
            }
            return elementos[n - 1];
        } else {
            if (!elementoNumero.containsKey(input)) {
                print("Ingresa una abreviación apropriada");
                return null;
            }
            return elementoNumero.get(input);
        }
    }

    public static void main(String[] args) {
        TablaPeriodica t = new TablaPeriodica();
        while (true) {
            Scanner in = new Scanner(System.in);
            String input = in.next();
            Elemento e = processSyntax(input);
            if (e == null) {
                continue;
            }
            e.imprimirElemento();
        }
    }
}
