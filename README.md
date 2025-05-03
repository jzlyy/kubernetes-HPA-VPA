# kubernetes-HPA-VPA
Dynamically scale the number of Pods and resource usage based on HPA/VPA.

## HPA (Horizontal Pod Autoscaler) for horizontal scaling
### Scaling based on Resource metrics (CPU, Memory)
Utilize Metrics Server to monitor the utilization of various resources in the Kubernetes cluster in real time, and use HPA to perform native scaling of Pods.
### Scaling based on Pods (Custom) metrics (HTTP request count, Kafka message backlog)
Use Prometheus-Adapter to convert Prometheus metrics into parameters recognizable by the Kubernetes API. HPA then identifies these parameters to scale Pods.

## VPA (Vertical Pod Autoscaler) for vertical scaling
### Dynamic scaling of CPU/Memory based on VPA resource monitors
Implement optimal VPA scaling for CPU/Memory using ResourceQuota and LimitRange to enforce resource constraints
### Integrate kube-prometheus-stack for granular scenario monitoring
Implement detailed monitoring for specific scenarios by integrating the kube-prometheus-stack.

