run:
	cargo run
create-container:
	docker build -t my-redis-image .
start-container:
	docker run --name my-redis-container -p 6379:6379 -d my-redis-image