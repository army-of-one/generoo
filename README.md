# Generoo

This project is a generator for APIs.

There are a number of built-in generators in the 


## Creating a Generator

Generators are built on the backbone of configuration files.

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
          "evaluation": "EQUALITY",
          "values": []
        }
      ]
    }
  ],
  "mappings": [
    {
      "template": "templates/example.txt",
      "destination": "output/{}-example.txt",
      "fields": [
        {
          "name": "project",
          "transformation": "dashes"
        }
      ]
    }
  ]
}
```

#### Prompts

The prompts will execute in the order they appear in the list.

Evaluations will validate user input. Here are some of the types of validations that are supported.

| Evaluation Name | Description |
| --- | --- |
| EQUALITY | Checks that the inputted value equals any of the validation values. |
| GREATER_THAN | Checks that the inputted value is greater than provided value.  |
| LESS_THAN | Checks that the inputted value is less than provided value. |

**TODO**: 
* Add support for field references between prompts.
* Support prompt validations.
* Add template validations

#### Mappings

The mappings define:
* `template` - a path to a template file.
* `destination` - a path to an output file.
* `fields` - the variables that will be replaced in the output destination string.

The `destination` string can be a formatted string. The formatted strings use `{}` when replacing. Provide
the same number of `{}` in the destination string as you do fields in the list. The fields will be replaced in order
for the final `destination` string.

Fields have a name, which corresponds to a variable or prompt name, as well as a transformation. Transformations
will take the value provided in the prompt and perform a transformation on it to a different format. For example:

Using a `"DASHES"` transformation on `tech.armyofone` yields `tech-armyofone`.

| Transformation | Example |
|---|---|
|DASHES | army-of-one  |
|SLASHES | army/of/one |
|PERIODS | army.of.one  |
|CAPITALIZED | ArmyOfOne |
|CAPITALIZED_WITH_SPACES | Army Of One|

### Run Configurations

After the first run of this project, a `.generoo` file will be created in the root directory. This `.generator` file
will contain configuration files. One of these files is the `run-configuration.json` file. This file contains the inputs
used when the project was run the first time. When subsequent generator tasks are run, this run configuration will be 
used to automatically fill out the fields in prompts. 

If you would like to proceed with the `run-configuration.json` fields without being prompted again, then you can provide
 the`-c`or `--no-config` flags in the run command: `generoo generate resource --no-config`.