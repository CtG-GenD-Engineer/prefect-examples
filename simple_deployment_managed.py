from prefect import flow, task


@flow(log_prints=True)
def simple_flow(name: str):
    message = generate_message(name)
    log_message(message)


@task
def generate_message(name: str):
    return f"Welcome to Prefect, {name}!"


@task
def log_message(message: str):
    print(message)


if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/Generation-Data/prefect-examples.git",
        entrypoint="simple_flow.py:simple_flow",
    ).deploy(
        name="simple-flow-managed",
        work_pool_name="managed-pool",
        cron="*/5 * * * *",
        parameters={"name": "Kevin"}
    )
