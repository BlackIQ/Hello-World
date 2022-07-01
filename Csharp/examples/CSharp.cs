using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            /*System.Console.WriteLine("Hello World!");
            can be used if you don't set up
            'using System;' at top of file*/

            // Include this line to keep the console from closing right after printing "Hello World!"
            Console.ReadLine();
        }
    }
}

