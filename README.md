# DevOps Pet-проект: FastAPI + Kubernetes + мониторинг

Демонстрационный проект, показывающий полный DevOps-цикл: от кода до продакшена с мониторингом.

## Стек
- Python (FastAPI) — приложение
- Docker / Docker Compose — контейнеризация
- Kubernetes (minikube) + Helm — оркестрация
- GitHub Actions — CI/CD
- Ansible — автоматизация настройки сервера
- Prometheus + Grafana + Alertmanager — мониторинг

## Структура репозитория
- `app/` — исходный код приложения и Dockerfile
- `k8s/` — базовые Kubernetes-манифесты (ручной вариант)
- `helm/` — Helm chart для деплоя приложения
- `ansible/` — playbook для автоматизации настройки
- `monitoring/` — инструкции по развёртыванию мониторинга
- `.github/workflows/` — пайплайн CI/CD

## Как запустить локально

docker compose up --build

## Как развернуть в Kubernetes

minikube start
eval $(minikube docker-env)
docker build -t todo-app:latest ./app
helm install todo-app ./helm/todo-app

## Мониторинг

См. monitoring/README.md
