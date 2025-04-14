public class Main {
    public static void main(String[] args) {
        EnchufePlano plano = new EnchufePlano();
        EnchufeRedondo adaptado = new AdaptadorEnchufe(plano);

        adaptado.conectarRedondo();
    }
}
