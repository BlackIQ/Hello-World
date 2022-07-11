// asynchronously
await Deno.writeAll(Deno.stdout, new TextEncoder().encode("hello world"));

// or, sychronously
Deno.writeAllSync(Deno.stdout, new TextEncoder().encode("hello world"));