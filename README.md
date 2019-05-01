# Generoo

Code generation driven by templating and configuration.

## Usage

Using generoo is simple. The CLI or python script takes 3 positional arguments:

`generoo <goal> <project> <name>`

- goal - what you want generoo to do. Example: `generate`
- scope - what you want generoo to create. Example: `project`
- name - what you want to name what generoo is creating. This will be used as the root directory name. Example: `test`

Positional Arguments (in the order they appear):

#### Goal Options

| Argument | Description | Aliases |
|---|---|---|
|`generate` | Fill in templates for an archetype or custom user project.  | `gen`, `g` |


#### Scope Options

| Argument | Description | Aliases |
|---|---|---|
|`project` | Generates a new project with the given name.  | `gen`, `g` |

### Run from Sources

Clone the project. Navigate to the directory on your machine.

You can run from the python interpreter by using the following command:

```python generoo.py <goal> <scope> <name>```

### Run binary

Download the binary. Navigate to the download directory on your machine.

Run the binary using the following command:

```generoo <goal> <scope> <name>```

## Configuration

Configurations are the driving force behind Generoo's generation.

### Template Configuration

The template configuration is the most important configuration. It encompasses the following:
* the mapping from the template directory to the output directory.
* the prompts that need to be taken from the user in order to fill in the templates.
* any variables that need to be used in the mappings but not taken by the user

In pre-existing archetypes, it will always be called `template-configuration.json`.

Here is an example of a `template-configuration.json` file:

```json
{
  "variables": [
    {
      "name": "variable_name",
      "value": "variable value"
    }
  ],
  "prompts": [
    {
      "name": "name",
      "text": "Enter name",
      "options": ["Options"],
      "default": "default",
      "validations": [
        {
          "evaluation": "REGEX",
          "value": "/^\S+$/g"
        }
      ]
    }
  ],
  "transformations": [
      {
        "reference": "artifact_id",
        "name": "artifact_id_capitalized",
        "transformation": "CAPITALIZED"
      }
  ],
  "mappings": [
    {
      "template": "templates/example.txt",
      "destination": "output/{{name}}-example.txt"
    }
  ]
}
```

#### Variables

Variables are values that you would like to change in a single place in the configuration but that don't require user
input. 

#### Prompts

Prompts will capture information from the user of the tool. 

- `name` - the name of the variable that stores the value.

- `text` - the text the user will see (no need to add `:`, that will be done for you).

- `options` - a list of the accepted options for the prompt

- `default` - a default value to use if the user does not enter a new one.

- `validations` - a list of validations to perform on the user's input before continuing.

The prompts will execute in the order they appear in the list.

Evaluations will validate user input. Here are some of the types of validations that are supported.

| Evaluation Name | Description |
| --- | --- |
| REGEX | Checks that the inputted value matches the provided Regular Expression. |
| GREATER_THAN | Checks that the inputted value is greater than provided value.  |
| LESS_THAN | Checks that the inputted value is less than provided value. |

#### Transformations

Transformations are done after the prompts are entered by the user. 

Using a `"DASHES"` transformation on `tech.armyofone` yields `tech-armyofone`.

| Transformation | Example |
|---|---|
|DASHES | army-of-one  |
|SLASHES | army/of/one |
|PERIODS | army.of.one  |
|CAPITALIZED | ArmyOfOne |
|CAPITALIZED_WITH_SPACES | Army Of One |

#### Mappings

The mappings define:
* `template` - a path to a template file.
* `destination` - a path to an output file.

The `destination` string can take named variables using the mustache syntax: `{{variable_name}}. The name, in this case,
can be any of the variable names, prompt names, or transformation names.

### Run Configurations

After the first run of this project, a `.generoo` file will be created in the root directory. This `.generator` file
will contain configuration files. One of these files is the `run-configuration.json` file. This file contains the inputs
used when the project was run the first time. When subsequent generator tasks are run, this run configuration will be 
used to automatically fill out the fields in prompts. 

If you would like to proceed with the `run-configuration.json` fields without being prompted again, then you can provide
 the`-c`or `--no-config` flags in the run command: `generoo generate resource --no-config`.
 
**TODO**: 
* Add support for field references between prompts.
* Support prompt validations.
* Add template validations
* Add mapping and prompt sequencing. Example, collect prompts for sequence 1, then map sequence 1 before continuing to 2.
* Add support for recursive templating (allow templates to be in correct file structure or template dir)