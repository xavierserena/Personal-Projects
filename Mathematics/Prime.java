public class Prime {
    public static boolean isPrime(int n) {
        return isPrime(n, 2);
    }

    public static boolean isPrime(int n, int x) {
        if (x > Math.sqrt(n)) {
            return true;
        } else if (n % x == 0) {
            return false;
        }
        return isPrime(n, x++);
    }

    public static void printPrimes(int n) {
        printPrimes(1, n);
    }

    public static void printPrimes(int min, int max) {
        int count = 0;
        for(int i = min; i < max; i++) {
            if (isPrime(i)) {
                System.out.println(i);
                count++;
            }
        }
        System.out.printf("There are %d primes between %d and %d", count, min, max);
    }

    public static void main(String[] args) {
        System.out.println(args.length);
        System.out.println(Integer.parseInt(args[0]));
        if (args.length == 0 || args.length > 2) {
            throw new IllegalArgumentException("Input must 1 or 2 integers");
        }

        int min, max;
        if (args.length == 1) {
            min = 1;
            max = Integer.parseInt(args[0]);
        } else {
            min = Integer.parseInt(args[0]);
            max = Integer.parseInt(args[1]);
        }
        printPrimes(min, max);
    }
}