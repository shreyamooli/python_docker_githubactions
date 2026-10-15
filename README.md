# gha-demo

Tiny Flask app used to practice Docker + GitHub Actions.

## Run locally

```bash
pip install -r requirements-dev.txt
pytest
python -m app.main            # http://localhost:8000/health
```

## Docker

```bash
docker build -t gha-demo .
docker run --rm -p 8000:8000 gha-demo
curl localhost:8000/add?a=2\&b=3
```

## Pipeline (`.github/workflows/ci.yml`)

`lint` + `test` (matrix 3.11/3.12) run in parallel -> `docker` job builds the image,
smoke-tests it, scans with Trivy, and pushes to `ghcr.io/<you>/<repo>` on pushes to `main`.

## Push to GitHub

```bash
git init && git add . && git commit -m "init"
git branch -M main
git remote add origin git@github.com:<you>/gha-demo.git
git push -u origin main
```
Then check the **Actions** tab. Image shows up under your profile's **Packages**.

## Things to try next

- Make a test fail on a PR and watch the `docker` job get skipped
- Set Trivy `exit-code: "1"` and see the build break
- Add a `workflow_dispatch` trigger and run it manually
- Tag releases (`v1.0.0`) and add `type=semver` to the metadata tags
- Add an environment with manual approval before the push step
