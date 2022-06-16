namespace Quantum.HelloWorld

{

    open Microsoft.Quantum.Canon;

    open Microsoft.Quantum.Primitive;

    operation SayHello () : Unit {

        Message("Hello Q#:)");

    }

}