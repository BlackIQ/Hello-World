# Vala
Vala is an object-oriented programming language with a self-hosting compiler that generates C code and uses the GObject system.

Vala is syntactically similar to C# and includes notable features such as anonymous functions, signals, properties, generics,
assisted memory management, exception handling, type inference, and foreach statements. Its developers, Jürg Billeter and Raffaele Sandrini,
wanted to bring these features to the plain C runtime with little overhead and no special runtime support by targeting the GObject object system.
Rather than compiling directly to machine code or assembly language, it compiles to a lower-level intermediate language.
It source-to-source compiles to C, which is then compiled with a C compiler for a given platform, such as GCC.

For memory management, the GObject system provides reference counting. In C, a programmer must manually manage adding and removing references,
but in Vala, managing such reference counts is automated if a programmer uses the language's built-in reference types rather than plain pointers.

Using functionality from native code libraries requires writing vapi files, defining the library interfacing.
Writing these interface definitions is well-documented for C libraries, especially when based on GObject. However,
C++ libraries are not supported. Vapi files are provided for a large portion of the GNOME platform, including GTK.

Vala was conceived by Jürg Billeter and was implemented by him and Raffaele Sandrini, finishing a self-hosting compiler in May 2006.

## References

- [Wikipedia](https://en.wikipedia.org/wiki/Vala_(programming_language))
