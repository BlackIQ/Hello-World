public class Vehicle {
    void engine(){
        System.out.println("350cc");
    }
}
class honda extends Vehicle{
    void shine(){
        System.out.println("tubeless tyre");
    }
}
class hero extends honda{
    void splendor(){
        System.out.println("Best quality");
    }
}
class Inheritance{
    public static void main(String[] args) {
        hero b = new hero();
        b.splendor();
        b.shine();
        b.engine();
    }
}
