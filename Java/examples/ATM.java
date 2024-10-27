import java.util.ArrayList;
import java.util.Scanner;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class ATM {
    private double balance;
    private final String PIN = "1234"; // In real applications, this should be securely stored
    private boolean isAuthenticated = false;
    private List<String> transactionHistory;
    private static final double MINIMUM_BALANCE = 0;
    private static final double MAXIMUM_WITHDRAWAL = 10000;
    private static final double MAXIMUM_DEPOSIT = 50000;
    
    public ATM(double initialBalance) {
        if (initialBalance < MINIMUM_BALANCE) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.balance = initialBalance;
        this.transactionHistory = new ArrayList<>();
    }

    private boolean authenticate(Scanner scanner) {
        int attempts = 3;
        while (attempts > 0) {
            System.out.print("Enter PIN (4 digits): ");
            String enteredPin = scanner.next();
            
            if (enteredPin.equals(PIN)) {
                return true;
            }
            
            attempts--;
            System.out.println("Invalid PIN. " + attempts + " attempts remaining.");
        }
        
        System.out.println("Too many failed attempts. Card blocked.");
        return false;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        try {
            validateDeposit(amount);
            balance += amount;
            recordTransaction("Deposit", amount);
            System.out.printf("Deposit successful. Current balance: $%.2f%n", balance);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void withdraw(double amount) {
        try {
            validateWithdrawal(amount);
            balance -= amount;
            recordTransaction("Withdrawal", amount);
            System.out.printf("Withdrawal successful. Current balance: $%.2f%n", balance);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    private void validateDeposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive.");
        }
        if (amount > MAXIMUM_DEPOSIT) {
            throw new IllegalArgumentException("Amount exceeds maximum deposit limit of $" + MAXIMUM_DEPOSIT);
        }
    }

    private void validateWithdrawal(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient funds.");
        }
        if (amount > MAXIMUM_WITHDRAWAL) {
            throw new IllegalArgumentException("Amount exceeds maximum withdrawal limit of $" + MAXIMUM_WITHDRAWAL);
        }
    }

    private void recordTransaction(String type, double amount) {
        LocalDateTime now = LocalDateTime.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        String transaction = String.format("%s | %s | $%.2f | Balance: $%.2f",
                                         now.format(formatter), type, amount, balance);
        transactionHistory.add(transaction);
    }

    public void displayTransactionHistory() {
        if (transactionHistory.isEmpty()) {
            System.out.println("No transactions to display.");
            return;
        }
        
        System.out.println("\nTransaction History:");
        System.out.println("----------------------------------------");
        for (String transaction : transactionHistory) {
            System.out.println(transaction);
        }
        System.out.println("----------------------------------------");
    }

    private void displayMenu() {
        System.out.println("\nATM Menu:");
        System.out.println("1. Check Balance");
        System.out.println("2. Deposit");
        System.out.println("3. Withdraw");
        System.out.println("4. Transaction History");
        System.out.println("5. Exit");
        System.out.print("Enter your choice: ");
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            ATM atm = new ATM(1000.00);
            
            System.out.println("Welcome to the ATM");
            if (!atm.authenticate(scanner)) {
                return;
            }
            
            atm.isAuthenticated = true;
            
            while (atm.isAuthenticated) {
                try {
                    atm.displayMenu();
                    int choice = scanner.nextInt();
                    
                    switch (choice) {
                        case 1:
                            System.out.printf("Current balance: $%.2f%n", atm.getBalance());
                            break;
                            
                        case 2:
                            System.out.print("Enter deposit amount: $");
                            double depositAmount = scanner.nextDouble();
                            atm.deposit(depositAmount);
                            break;
                            
                        case 3:
                            System.out.print("Enter withdrawal amount: $");
                            double withdrawalAmount = scanner.nextDouble();
                            atm.withdraw(withdrawalAmount);
                            break;
                            
                        case 4:
                            atm.displayTransactionHistory();
                            break;
                            
                        case 5:
                            System.out.println("Thank you for using our ATM. Goodbye!");
                            atm.isAuthenticated = false;
                            break;
                            
                        default:
                            System.out.println("Invalid choice. Please try again.");
                    }
                } catch (java.util.InputMismatchException e) {
                    System.out.println("Error: Please enter a valid number.");
                    scanner.nextLine(); // Clear the invalid input
                } catch (Exception e) {
                    System.out.println("An error occurred: " + e.getMessage());
                    scanner.nextLine(); // Clear any invalid input
                }
            }
        }
    }
}
