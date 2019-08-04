public class FelizCumple {

    private static void print(String arg) {
        System.out.print(arg);
    }

    private static void println(String arg) {
        System.out.println(arg);
    }

    public static void main(String[] args) {
        for (int i = 0; i < 4; i++) {
            print("Feliz cumpleaños ");
            if (i == 2) {
                println("Ana");
            } else {
                print("a ti ");
                println("*aplauso aplauso aplauso*");
            }
        }
        println("Mordida, mordida... *splat*");
    }
}
