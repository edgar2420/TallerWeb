public class Main {
    public static void main(String[] args) {
        // Formulario base
        Formulario base = new Formulario("Laboratorios ABD", "Av. Los Pinos #123", "Corporativo");

        // Clonamos para cliente 1
        Formulario cliente1 = base.clone();
        cliente1.setNombreContacto("Carlos Pérez");
        cliente1.setTelefono("78912345");

        // Clonamos para cliente 2
        Formulario cliente2 = base.clone();
        cliente2.setNombreContacto("Lucía Gómez");
        cliente2.setTelefono("74589632");

        // Mostramos los formularios
        cliente1.mostrar();
        cliente2.mostrar();
    }
}
