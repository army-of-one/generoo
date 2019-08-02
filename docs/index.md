# Generoo

<img src="generoo_no_background.png" width="200" height="188" />

When we start new projects, we often go through a similar set of steps to bootstrap it. As a developer, we want to
spend time developing. That's where generoo comes in. Generoo allows developers to write a project template once and
then generate new projects from that template in seconds. Project templating without any additional coding gives time 
back to developers so they can focus on writing core business logic.

For an in-depth look at Generoo and it's use, see the [documentation](https://generoo.armyofone.tech).

## Installation

### PIP

Install the package from pip:

`pip install generoo`

Run from the module:

`python -m generoo <goal> <scope> <name>`

### Source

Clone the project. Navigate to the directory on your machine.

*Note*: Generoo must be run in Python 3.6 and above.

You can run from the python interpreter by using the following command:

```python generoo.py <goal> <scope> <name>```

## How does it work?

Generoo is simple. Create a template using [Mustache](https://mustache.github.io/)'s syntax for string replacement.

The template could be a file called `examples/hello-world/hello_world.py` that looks like:

```python
print('Hello, {{who}}')
```

Then, a template configuration file in JSON or YAML defines prompts for the user when they run Generoo. Here's an example
file called `examples/hello-world/template-config.json`:

```json
{
  "prompts": [
    {
      "name": "who",
      "text": "Enter who you want to say hello to"
    }
  ]
}
```

The text is what the user will see when the prompt is shown and the name is the template value that will be replaced.

Running `python3 generoo.py generate project hello-world --template examples/hello-world/hello_world.py --template-config examples/hello-world/template-config.json` will prompt the user:

```
$ Say hello to:
```

When user enters: `World`, then the template is filled out and written to `hello-world/hello_world.py` and looks like:

```python
print('Hello, World')
```

For more information about how the templating system works, see the [Generoo documentation](https://generoo.armyofone.tech).

## Usage

Using generoo is simple. The CLI or python script takes 3 positional arguments:

`generoo <goal> <scope> <name> [options...]`

- `goal` - what you want generoo to do. Example: `generate`
- `scope` - what you want generoo to create. Example: `project`
- `name` - what you want to name what generoo is creating. This will be used as the root directory name. Example: `example`

Positional Arguments (in the order they appear):

### Goals

| Argument | Description | Aliases |
|---|---|---|
|`generate` | Fill in templates for an archetype or custom user project.  | `gen`, `g` |

### Scopes

| Argument | Description | Aliases |
|---|---|---|
|`project` | Generates a new project with the given name.  | `project`, `proj`, `pro`, `p` |

### Options

| Option | Description |
|---|---|
|`-n`, `--no-config` | Will run generoo without a pre-existing configuration.  |
|`-a`, `--auto-config` | Will run generoo using the pre-existing configuration and only prompt for values not present in the configuration.  |
|`-c`, `--template-config` | Points to a location on the system that contains a custom template config.  |
|`-t`, `--template` | Points to a directory on the system that contains templates for a corresponding template config.  |
|`-r`, `--run-configuration` | Points to a file on the system that contains a run configuration for a corresponding template config. |

## Built-In Templates

If no `--template` or `--template-config` arguments are given, then Generoo will generate from its built-in templates. 
Check out the `archetypes` directory to see the templates yourself. Or, better yet, try generating one. 

## Contributing

Have a template that you'd like to share? Submit a PR with the template and we'll see about getting it
into the built-in templates for this project. 

Want some new functionality? Open an issue or a PR with the changes you'd like to see. 
