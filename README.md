# kubernetes-HPA-VPA
[![GitHub License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Dynamically scale the number of Pods and resource usage based on HPA/VPA.

## HPA (Horizontal Pod Autoscaler)
### Scaling based on Resource metrics (CPU, Memory)
Utilize Metrics Server to monitor the utilization of various resources in the Kubernetes cluster in real time, and use HPA to perform native scaling of Pods.
### Scaling based on Pods (Custom) metrics (HTTP request count, Kafka message backlog)
Use Prometheus-Adapter to convert Prometheus metrics into parameters recognizable by the Kubernetes API. HPA then identifies these parameters to scale Pods.

## VPA (Vertical Pod Autoscaler)
### Dynamic scaling of CPU/Memory based on VPA resource monitors
Implement optimal VPA scaling for CPU/Memory using ResourceQuota and LimitRange to enforce resource constraints

## Prometheus monitoring system
### Integrate kube-prometheus-stack for granular scenario monitoring
Integrate Prometheus, Grafana, and Alertmanager via the kube-prometheus-stack to implement an observable resource dashboard and establish a rapid alerting system for resource shortages.

## Security Policy
To report security vulnerabilities, please see [SECURITY.md](SECURITY.md)。

## Start
The team can refer to my code solution and make reasonable modifications based on their environmental requirements.
