# {{ cookiecutter.project_name }}

## Getting Started

## Usage

1. Initialize project

   ```bash
   make init
   ```

2. Run an experiment

   ```bash
   make run
   ```

### DAG

```mermaid
flowchart TD
        node1["split"]
        node2["test"]
        node3["train"]
        node1-->node2
        node1-->node3
        node3-->node2
```

## License

Distributed under the {{ cookiecutter.open_source_license }} License. See [LICENSE](./LICENSE) for more information.

## References

- DVC: https://dvc.org/doc
- Poetry: https://python-poetry.org/docs/
- Make: https://www.gnu.org/software/make/manual/make.html
