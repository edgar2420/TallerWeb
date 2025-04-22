import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        ATM atm = new ATM();

        atm.cambiarEstado(new ActiveState());

        atm.registrarCliente("123", 500.0);
        atm.getBalance("123");
        atm.registerIncome("123", 200.0);
        atm.getBalance("123");
        atm.registerExpense("123", 100.0);
        atm.getBalance("123");

        atm.registrarCliente("1234", 900);
        atm.getBalance("1234");
        atm.registerIncome("1234", 300);
        atm.getBalance("1234");
        


        atm.cambiarEstado(new SuspendedState());
        atm.registerIncome("123", 50.0);
    }
}


class ATM {
    private ATMState estadoActual;
    private Map<String, Double> cuentas = new HashMap<>();

    public void cambiarEstado(ATMState nuevoEstado) {
        this.estadoActual = nuevoEstado;
        System.out.println("Estado del cajero cambiado a: " + nuevoEstado.getClass().getSimpleName());
    }

    public void registrarCliente(String idCliente, double saldoInicial) {
        cuentas.put(idCliente, saldoInicial);
        System.out.println("Cliente registrado: " + idCliente + " con saldo inicial: " + saldoInicial);
    }
    //ingreso
    public void registerIncome(String idCliente, double monto) {
        estadoActual.registerIncome(this, idCliente, monto);
    }
    //egreso
    public void registerExpense(String idCliente, double monto) {
        estadoActual.registerExpense(this, idCliente, monto);
    }

    public void getBalance(String idCliente) {
        estadoActual.getBalance(this, idCliente);
    }

    public Map<String, Double> getCuentas() {
        return cuentas;
    }
}

interface ATMState {
    void registerIncome(ATM atm, String idCliente, double monto);
    void registerExpense(ATM atm, String idCliente, double monto);
    void getBalance(ATM atm, String idCliente);
}


class ActiveState implements ATMState {
    @Override
    public void registerIncome(ATM atm, String idCliente, double monto) {
        Map<String, Double> cuentas = atm.getCuentas();
        if (cuentas.containsKey(idCliente)) {
            cuentas.put(idCliente, cuentas.get(idCliente) + monto);
            System.out.println("Ingreso registrado. Nuevo saldo: " + cuentas.get(idCliente));
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }

    @Override
    public void registerExpense(ATM atm, String idCliente, double monto) {
        Map<String, Double> cuentas = atm.getCuentas();
        if (cuentas.containsKey(idCliente)) {
            double saldoActual = cuentas.get(idCliente);
            if (saldoActual >= monto) {
                cuentas.put(idCliente, saldoActual - monto);
                System.out.println("Egreso registrado. Nuevo saldo: " + cuentas.get(idCliente));
            } else {
                System.out.println("Saldo insuficiente.");
            }
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }

    @Override
    public void getBalance(ATM atm, String idCliente) {
        Map<String, Double> cuentas = atm.getCuentas();
        if (cuentas.containsKey(idCliente)) {
            System.out.println("Cliente: " + idCliente + ", Saldo: " + cuentas.get(idCliente));
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }
}


class BalanceState implements ATMState {
    @Override
    public void registerIncome(ATM atm, String idCliente, double monto) {
        System.out.println("El cajero no puede realizar depósitos en este estado.");
    }

    @Override
    public void registerExpense(ATM atm, String idCliente, double monto) {
        System.out.println("El cajero no puede realizar egresos en este estado.");
    }

    @Override
    public void getBalance(ATM atm, String idCliente) {
        Map<String, Double> cuentas = atm.getCuentas();
        if (cuentas.containsKey(idCliente)) {
            System.out.println("Cliente: " + idCliente + ", Saldo: " + cuentas.get(idCliente));
        } else {
            System.out.println("Cliente no encontrado.");
        }
    }
}


class SuspendedState implements ATMState {
    @Override
    public void registerIncome(ATM atm, String idCliente, double monto) {
        System.out.println("Cajero inactivo. No se pueden realizar operaciones.");
    }

    @Override
    public void registerExpense(ATM atm, String idCliente, double monto) {
        System.out.println("Cajero inactivo. No se pueden realizar operaciones.");
    }

    @Override
    public void getBalance(ATM atm, String idCliente) {
        System.out.println("Cajero inactivo. No se pueden realizar operaciones.");
    }
}
