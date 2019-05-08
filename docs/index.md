# What does it do?

Generoo is a tool that can be used to create customizable and reusable templates for generating anything from single
documents to complex software projects. Generoo leverages [Mustache](https://mustache.github.io/) for its simple and 
powerful templating syntax. Be sure to check out their [manual](https://mustache.github.io/mustache.5.html) for 
information on creating templates.

Unlike other popular templating frameworks, Generoo requires no additional coding to use.

Whether you want to generate a pre-configured project from the built-in Generoo archetypes, or you created your own template,
it can all be achieved through a JSON configuration file and a template folder.

See the [documentation](faq.md) for more details.

# Usage

For an in depth look at usage and examples, see the [documentation](documentation.md).

Using generoo is simple. The CLI or python script takes 3 positional arguments:

`generoo [options...] <goal> <scope> <name>`

- `goal` - what you want generoo to do. Example: `generate`
- `scope` - what you want generoo to create. Example: `project`
- `name` - what you want to name what generoo is creating. This will be used as the root directory name. Example: `test`

Positional Arguments (in the order they appear):

## Goal Options

| Argument | Description | Aliases |
|---|---|---|
|`generate` | Fill in templates for an archetype or custom user project.  | `gen`, `g` |


## Scope Options

| Argument | Description | Aliases |
|---|---|---|
|`project` | Generates a new project with the given name.  | `project`, `proj`, `pro`, `p` |

### Options

| Option | Description |
|---|---|
|`-n`, `--no-config` | Will run generoo without a pre-existing configuration.  |
|`-a`, `--auto-config` | Will run generoo using the pre-existing configuration and only prompt for values not present in the configuration.  |
|`-c`, `--template-config` | Points to a location on the system that contains a custom template config.  |
|`-t`, `--templates` | Points to a directory on the system that contains templates for a corresponding template config.  |
|`-r`, `--run-configuration` | Points to a file on the system that contains a run configuration for a corresponding template config. |