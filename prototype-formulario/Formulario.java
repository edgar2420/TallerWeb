public class Formulario implements Cloneable {
    private String nombreEmpresa;
    private String direccion;
    private String tipoCliente;
    private String nombreContacto;
    private String telefono;

    public Formulario(String nombreEmpresa, String direccion, String tipoCliente) {
        this.nombreEmpresa = nombreEmpresa;
        this.direccion = direccion;
        this.tipoCliente = tipoCliente;
    }

    public void setNombreContacto(String nombreContacto) {
        this.nombreContacto = nombreContacto;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    @Override
    public Formulario clone() {
        try {
            return (Formulario) super.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }

    public void mostrar() {
        System.out.println("Empresa: " + nombreEmpresa);
        System.out.println("Dirección: " + direccion);
        System.out.println("Tipo Cliente: " + tipoCliente);
        System.out.println("Contacto: " + nombreContacto);
        System.out.println("Teléfono: " + telefono);
        System.out.println("-------------------------");
    }
}
