import edu.princeton.cs.algs4.BST;

import java.util.Random;
import java.util.Scanner;

public class Prueba {
    private int mode;
    private int questions;
    private int correct;
    private boolean over;
    private BST<Integer, Elemento> usedElements;
    private TablaPeriodica table;

    Prueba(TablaPeriodica t) {
        table = t;
        mode = selectTest();
        questions = 0;
        correct = 0;
        over = false;
        usedElements = new BST<>();
    }

    public void printScore() {
        if (mode == 1) {
            System.out.printf("Puntaje: %d \n", questions);
        } else {
            System.out.printf("Puntaje: %.2f" + "% \n", percent());
        }
    }

    private double percent() {
        return correct * 100 / questions;
    }

    private int selectTest(){
        int testNum = 0;
        Scanner in = new Scanner(System.in);
        String input = new String();
        boolean proper = false;
        while (!proper) {
            System.out.println("Ingresa el número de prueba");
            System.out.println("1) Racha");
            System.out.println("2) Diez preguntas");
            input = in.next();
            if (input.matches(".*\\d.*")) {
                testNum = Integer.parseInt(input);
                proper = (testNum == 1 || testNum == 2);
            }
        }
        return testNum;
    }

    public void test() {
        while (!over) {
            if (askQuestion()) {
                correct++;
            } else if (mode == 1 || questions >= 10) {
                over = true;
            }
        }
    }

    private boolean askQuestion() {
        int number;
        Elemento e;
        Scanner in = new Scanner(System.in);
        Random random = new Random();
        do {
            number = random.nextInt(118);
            e = table.getElement(number);
        } while (usedElements.contains(number));
        questions++;
        usedElements.put(number, e);
        number = random.nextInt(2);
        if (number == 0) {
            System.out.printf("Escribe la abreviación de %s \n", e.nombre);
            return in.next().equals(e.abreviacion);
        } else {
            System.out.printf("Escribe el número atómico de %s \n", e.nombre);
            String input = in.next();
            return input.matches(".*\\d.*") && Integer.parseInt(input) == e.numero;
        }
    }
}
