# README

## Get started with Prefect and Codespaces

### Create an API key

Go to [Prefect Cloud](https://app.prefect.cloud/auth/sign-up) and create an account and workspace.

Once logged in, create an API key.

Navigate to the account dropdown in the top right, and select "API keys".

<img src="images/api-key.png" alt="isolated" width="200"/>

Once on the API Keys page, click the plus at the top of the page to open the "Create API Key" form. Enter a name and click "Create".

<img src="images/key-create.png" alt="isolated" width="400"/>

Copy and save your API key for later use.

### Install and log in

Connect to Codespaces and install `prefect` and `prefect-dbt`:

`pip install prefect prefect-dbt`

Once installed, log in to Prefect Cloud with your API key:

`prefect cloud login -k <your-api-key>`

Once you see the following message in your terminal, you're good to go!

`Authenticated with Prefect Cloud! Using workspace 'your-account/your-workspace'.`

## Run your first flow

### Write and execute a flow script

Clone this repository or create a file called `simple_flow.py` with the following contents:

```python
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
    simple_flow("Kevin")
```

Replace the name "Kevin" on the last line with your own name, and save the file.
Run your flow by executing `python simple_flow.py` in your terminal.

Each time a function with a `@flow` decorator is called, a flow run is created.
Cmd+Click on the link generated in your terminal, or navigate to the "Runs" page in the [Prefect Cloud UI](app.prefect.cloud) and click on the **blue, generated flow run name** to view your flow run.

<img src="images/flow-run.png" alt="isolated" width="600"/>

### Understanding the flow run graph

Each flow run has an accompanying flow run graph.

<img src="images/flow-run-graph.png" alt="isolated" width="500"/>

At the center are **task runs**, a visual representation of `@task` decorated functions displayed at the time they were executed.
Task runs that share data are connected by an arrow. Since the `message` returned by the first task was passed as a parameter to the second task, `generate_message` points to `log_message`.

The colors across the bottom, which are also lightly shaded in the background of the graph, indicate the **state** of the flow run over time. This flow run went from `Pending` to `Running`, then to `Completed`. There are many other states, like `Scheduled`, `Paused`, `Failed`, and `Crashed`, each indicated by their own color.

Finally, the purple dots are **events**, which are small pieces of data emitted during a flow run that can trigger actions in other parts of the Prefect ecosystem.

**Task runs**, **states**, and **events** can all be clicked on for additional details.