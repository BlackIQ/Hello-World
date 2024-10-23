use dotenv::dotenv;
use actix_web::{web, App, HttpServer, HttpRequest, HttpResponse, Responder};
use redis::{Client, AsyncCommands};
use std::{collections::HashMap, env, sync::Arc};
use tokio::sync::Mutex;
use serde_json::json;

// Redis client handler (Arc + Mutex for shared state)
struct AppState {
    redis_client: Arc<Mutex<Client>>,
}

// A handler that accepts any request and interacts with Redis
async fn handle_request(
    req: HttpRequest, 
    body: String, 
    data: web::Data<AppState>
) -> impl Responder {
    let redis_client = data.redis_client.clone();
    let mut con = redis_client.lock().await.get_multiplexed_async_connection().await.unwrap();

    // Extract the user ip
    let user_ip = req.peer_addr().map(|addr| addr.ip().to_string()).unwrap_or_else(|| "unknown".to_string());
    // Extract method, headers, and path
    let method = req.method().to_string();
    let path = req.path().to_string();
    let headers = req.headers().clone();

    // Increment the count for the user IP
    let _: () = con.incr(user_ip.clone(), 1).await.unwrap();
    let _: () = con.expire(user_ip.clone(), 60).await.unwrap();
    let req_count: i32 = con.get(user_ip.clone()).await.unwrap_or(0);

    println!("{user_ip}: {req_count}");

    let stored_method: String = method.clone();
    let stored_path: String = path.clone();
    let stored_body: String = body.clone();

    // Convert headers to a serializable format
    let headers_map: HashMap<String, String> = headers
    .iter()
    .filter_map(|(key, value)| {
        // Convert header key and value to String, filtering out None values
        Some((key.to_string(), value.to_str().ok()?.to_string()))
    })
    .collect();

    // Return a JSON response
    let response = json!({
        "stored_method": stored_method,
        "stored_path": stored_path,
        "stored_body": stored_body,
        "headers": headers_map
    });

    HttpResponse::Ok().json(response)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // Load the .env file
    dotenv().ok();
    
    // Get the PORT from the environment variables
    let port = env::var("PORT").expect("No PORT provided in env var");

    // Initialize Redis client
    let redis_url = env::var("REDIS_URL").expect("No REDIS_URL provided in env var");
    let redis_client = redis::Client::open(redis_url).expect("Invalid REDIS_URL");
    let app_state = web::Data::new(AppState {
        redis_client: Arc::new(Mutex::new(redis_client)),
    });

    // Create Actix Web server
    HttpServer::new(move || {
        App::new()
            .app_data(app_state.clone())
            .route("/{tail:.*}", web::to(handle_request))  // Catch all requests
    })
    .bind(("127.0.0.1", port.parse::<u16>().expect("PORT must be a valid u16")))?  // Changed to u16
    .run()
    .await
}
