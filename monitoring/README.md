# Мониторинг

Стек мониторинга развёрнут через Helm chart kube-prometheus-stack.

## Установка

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack -n monitoring --create-namespace

## Доступ к Grafana

kubectl port-forward --address 0.0.0.0 svc/monitoring-grafana 3000:80 -n monitoring

Логин: admin
Пароль: kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 -d

## Проверка сбора метрик

В Grafana Explore выполнить запрос `up` к источнику Prometheus — покажет статус всех отслеживаемых компонентов кластера.
