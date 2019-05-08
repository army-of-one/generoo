# Configuration

Configurations are the driving force behind Generoo's generation.

## Template Configuration

The template configuration is the most important configuration. It encompasses the following:
* any variables that need to be used in the mappings but not taken by the user
* the prompts that need to be taken from the user in order to fill in the templates
* the mapping from the template directory to the output directory

In pre-existing archetypes, it will always be called `<scope>-template-configuration.json`.

Here is an example of a `project-template-configuration.json` file:

```json
{
  "variables": [
    {
      "name": "group_id",
      "value": "tech.armyofone"
    }
  ],
  "prompts": [
    {
      "name": "artifact_id",
      "value": "example"
    },
    {
      "name": "guava_version",
      "text": "Enter the desired guava version",
      "options": ["19.0", "27.1-jre"],
      "default": "27.1-jre"
    },
    {
      "name": "database",
      "text": "Database?",
      "type": "BOOL",
      "default": "Yes",
      "follow_ups": [
        {
          "conditions": [
            {
              "evaluation": "BOOL",
              "value": true
            }
          ],
          "name": "database_type",
          "text": "What type of database would you like?",
          "options": ["Postgres", "Cassandra"],
          "transformations": [
            {
              "name": "database_type_capitalized",
              "transformation": "PERIODS"
            }
          ]
        }
      ]
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

### Variables

Prompts are an _optional_ field in the template configuration that allows the user to set values in the configuration 
that don't require user input. 

### Prompts

Prompts are an _optional_ field in the template configuration that allows the user to set the inputs that are captured 
when goal is being run.

Prompts will capture information from the user of the tool. 

- `name` - the name of the variable that stores the value.

- `text` - the text the user will see (no need to add `:`, that will be done for you).

- `type` - describes the type of value to capture. Defaults to `STRING`

- `options` - a list of the accepted options for the prompt

- `default` - a default value to use if the user does not enter a new one.

- `validations` - a list of validations to perform on the user's input before continuing.

- `follow_up` - a list of follow up prompts that depend on the answer for a given prompt.

The prompts will execute in the order they appear in the list.

Evaluations will validate user input. Here are some of the types of validations that are supported.

| Evaluation Name | Description |
| --- | --- |
| REGEX | Checks that the inputted value matches the provided Regular Expression. |
| GREATER_THAN | Checks that the inputted value is greater than provided value.  |
| LESS_THAN | Checks that the inputted value is less than provided value. |
| BOOL | Checks that the inputted value is equal to the provided value. |

Types

| Types | Notes |
| --- | --- |
| STRING |  DEFAULT. Captures a string value, can be evaluated against regular expressions or against provided options. |
| INT | Captures an integer value, can be evaluated against a provided integer validation or provided options. |
| BOOL | Captures a `yes` or `no` answer. The options provided will be evaluated in addition to built in yes/no options. Successfully evaluates against `yes`, `YES`, `Yes`, `y`, `Y`, `N`, `n`, `no`, `No`, `NO` |

Transformations

Each prompt and follow-up can take a list of transformations. 

```json
"transformations": [
  {
    "name": "field_capitalized",
    "transformation": "CAPITALIZED"
  },
  {
    "name": "field_slashes",
    "transformation": "SLASHES"
  },
  {
    "name": "field_periods",
    "transformation": "PERIODS"
  }
]

```

These transformations will perform casing and separator formatting.

For example:

Using a `"DASHES"` transformation on `tech.armyofone` yields `tech-armyofone`.

| Transformation | Example |
|---|---|
|SNAKE | army_of_one  |
|DASHES | army-of-one  |
|SLASHES | army/of/one |
|PERIODS | army.of.one  |
|LOWER | army of one  |
|CAMEL | armyOfOne |
|CAPITALIZED | ArmyOfOne |
|CAPITALIZED_WITH_SPACES | Army Of One |

Follow Ups

Follow up prompts are prompts with validations. Here's an example of a prompt with a follow-up:

```json
{
  "name": "steak",
  "text": "Do you want to go eat steak?",
  "type": "BOOL",
  "default": "Yes",
  "follow_ups": {
    "conditions": [
      {
        "evaluation": "BOOL",
        "value": true
      }
    ],
    "name": "time",
    "text": "What time do you want to go?"
  }
}
```

### Mappings

Mappings are an _optional_ field in the template configuration that allows for a custom destination to be set for a template. 

The mappings define:
* `template` - a path to a template file.
* `destination` - a path to an output file.

The `destination` string can take named variables using the mustache syntax: `{{variable_name}}. The name, in this case,
can be any of the variable names, prompt names, or transformation names.

If the mapping is optional, meaning that the user would need to say yes to a prompt in order to continue with filling out
the template, then mustache section syntax may be used. For example:

```json
{
  ...
  "mappings": {
    "template": "database/",
    "destination": "{{#database}}/database/{{database_type}}/{{/database}}"
  },
  ...
}
```

This mapping destination will first evaluate against the `database` value that would be collected by the prompt. If the
evaluation is true, meaning the database value was present, then the resulting destination string will be 
`/database/{{database_type}}`.

_Important Note_

If the opening tag for a section is provided, no closing tag (`{{/}}`) is required. The filesystem controller will still
treat the destination as a section and will not resolve it in the event the section conditional statement is false. This
is *not* standard behavior for `mustache`, so we're breaking the rules a little bit here. 

## Run Configurations

After the first run of this project, a `.generoo` file will be created in the root directory. This `.generator` file
will contain configuration files. One of these files is the `run-configuration.json` file. This file contains the inputs
used when the project was run the first time. When subsequent generator tasks are run, this run configuration will be 
used to automatically fill out the fields in prompts. 

If you would like to proceed with the `run-configuration.json` fields without being prompted again, then you can provide
 the`-c`or `--no-config` flags in the run command: `generoo generate resource --no-config`.