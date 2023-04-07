# Qwik
Qwik is a new kind of web framework that can deliver instant loading web applications at any size or complexity. Your sites and apps can boot with about 1kb of JS (regardless of application complexity), and achieve consistent performance at scale.

## New Approach to Performance Optimization

### Zero Loading

Qwik does not do hydration because it is resumable. Hydration can take several seconds, depending on the complexity of your application and mobile device speed. Qwik applications are instantly interactive even on slow mobile devices leading to a perfect Google PageSpeed score.


### Resumable

Qwik apps begin their life as SSR/SSG. Qwik serializes the application's state and framework state into HTML upon rendering the application. Then Qwik can resume execution where the server left off in the browser because all the data Qwik needs is in HTML. No JS needs to be downloaded or executed until it is needed to handle user interaction or rendering.


### JavaScript Streaming & Lazy Execution

Qwik introduces the concept of "JavaScript Streaming," where the page loads instantly and required JavaScript chunks are prefetched in a separate thread, similar to "buffering" in video streaming. The prefetched code only executes upon user action, and that process is called "Lazy Execution." This performance boost requires no manual effort or decision-making from the developer as this feature is built into Qwik out of the box.


### Reduced Rendering

Upon user interaction, Qwik is surgical about which components it rerenders. This is done through reactivity and allows Qwik to minimize the amount of rendering code downloaded and executed. The reactivity graph is built on the server and restored on the client without needing the application code to be present and re-run.


### Scalability

The amount of code downloaded to the client is proportional to the complexity of the user interaction, not the size of all components on the current route. Your site stays performant even as the complexity of the application grows over time.

### Code Once

Qwik has a single consistent mental model for both server and client code. The same component can begin its lifecycle on the server and process user events on the client. Setup DOM listeners on server render, have them be ready on your client interaction.﻿



## Refrences

- [Official Web](https://qwik.builder.io/)
- [Paydar Samane Blog](https://blog.paydarsamane.com/post/qwik-builder-io)
