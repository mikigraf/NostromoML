
# [WIP] NostromoML
## A self-hosted LLM fine-tuninig platform

NostromoML is a self-hosted platform for fine-tuning existing Large-Language-Models (LLMs) with private data and exposing them for inference.

### Getting started

```bash
./scripts/00-kind-local-registry.sh
go ./scripts/01-build-and-push-to-registry.go
cd deployment/helm-charts
helm install --generate-name .
# verify that it worked
kubectl get pods
kubectl logs api-gateway-559b46db4-hlpd9
```
