public class AdaptadorEnchufe extends EnchufeRedondo {
    private EnchufePlano enchufePlano;

    public AdaptadorEnchufe(EnchufePlano enchufePlano) {
        this.enchufePlano = enchufePlano;
    }

    @Override
    public void conectarRedondo() {
        enchufePlano.conectarPlano();
    }
}
