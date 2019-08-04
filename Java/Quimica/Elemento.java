class Elemento {
    public String nombre;
    public String abreviacion;
    public int numero;
    public double masa;

    public Elemento(String nombre, String abreviacion, int numero, double masa) {
        this.nombre = nombre;
        this.abreviacion = abreviacion;
        this.numero = numero;
        this.masa = masa;
    }

    public void imprimirElemento() {
        System.out.printf("%s (%s) \n", this.nombre, this.abreviacion);
        System.out.printf("Número: %d \n", this.numero);
        System.out.printf("Masa: %.3f \n", this.masa);
        System.out.println();
    }
}
