# Hello Full Stack

## Introduction and Motivations

Hello and welcome!

The primary purpose of this repository is to provide a well documented example
web application that tries to demonstrate the many elements that go into
building, deploying, and operating a full stack web application at Neural Magic.

Another purpose of this repository is to act as a template that can be forked
providing a consistent foundation for creating new full stack web applications.

# Current Structure

Currently, the general structure of a full stack web application is as follows:
- A minimal python web service built with
  - [FastAPI][fastapi-docs] for the web framework
  - [hypercorn][hypercorn-docs] for the application server
  - [service_foundation][neural-magic-nm-py-toolkit-service-foundation] for
    various application primitives and building blocks.
- A [Dockerfile][docker-getting-started] enabling a variety of container fun
- A [GitHub action][github-actions-docs] that builds the `Dockerfile` and pushes
  the resulting image to [AWS ECR][aws-ecr-dev-guide]
  - Creating the ECR repository requires one-time setup in the
    [infra repo][neural-magic-infra-repo] terraform which can be found
    [here][hello-full-stack-terraform-ecr-config].
  - Authorizing GitHub actions to access AWS resources requires one-time setup
    in the [infra repo][neural-magic-infra-repo] terraform which can be found
    [here][hello-full-stack-terraform-github-oidc-config].
    - **This should only be done for private repositories!** Otherwise, GitHub
      Actions could conceivably be used with malicious intent.
- A deployment manifest for [kubernetes][kubernetes-what-is-kubernetes] that
  describes the resources necessary to deploy the `hello-full-stack`
  application with:
  - An example [deployment][kubernetes-deployment-docs] resource.
  - An example [Nginx Ingress][kubernetes-nginx-ingress-docs] resource to allow
      ingress access to the service through an AWS Elastic Load Balancer to
      better ensure capacity and high availability.

[asyncio-docs]: https://docs.python.org/3/library/asyncio.html "asyncio — Asynchronous I/O"
[aws-ecr-dev-guide]: https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html "What is Amazon Container Registry?"
[docker-getting-started]: https://docs.docker.com/get-started/ "Docker - Get Started"
[fastapi-docs]: https://fastapi.tiangolo.com/ "FastAPI"
[github-actions-docs]: https://docs.github.com/en/actions "GitHub.com - Actions"
[hello-full-stack-terraform-ecr-config]: https://github.com/neuralmagic/infra/commit/bce8469cd118a40056e53a5ca64e6c260cd7e76e#diff-e3f88056ebd1c7b0e46a6f727e9db04bbeaafe012eee7500a178228efca098b7R242-R250 "GitHub.com - infra - AWS ECR repositories"
[hello-full-stack-terraform-github-oidc-config]: https://github.com/neuralmagic/infra/commit/bce8469cd118a40056e53a5ca64e6c260cd7e76e#diff-e3f88056ebd1c7b0e46a6f727e9db04bbeaafe012eee7500a178228efca098b7R42 "GitHub.com - infra - authorized_repositories"
[hypercorn-docs]: https://pgjones.gitlab.io/hypercorn/ "Hypercorn documentation"
[kubernetes-deployment-docs]: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ "kubernetes.io = Deployment"
[kubernetes-nginx-ingress-docs]: https://kubernetes.github.io/ingress-nginx/ "kubernetes.github.io - NGINX Ingress Controller"
[kubernetes-what-is-kubernetes]: https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/ "kubernetes.io - What is Kubernetes?"
[neural-magic-infra-repo]: https://github.com/neuralmagic/infra "GitHub.com - neuralmagic/infra"
[neural-magic-nm-py-toolkit-service-foundation]: https://github.com/neuralmagic/nm-py-toolkit/tree/main/src/nm_toolkit/service_foundation "GitHub.com - neuralmagic/nm-py-toolkit/src/service_foundation"
