---
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: hello-deployment
spec:
  replicas: 1
  template:
    metadata:
      labels:
        run: hello-world
    spec:
      containers:
      - name: hello
        image: nginxdemos/hello:latest
        ports:
        - containerPort: 80

---
apiVersion: v1
kind: Service
metadata:
  name: hello-service
  labels:
    run: hello-world
spec:
  type: NodePort
  ports:
  - port: 80
    protocol: TCP
  selector:
    run: hello-world
