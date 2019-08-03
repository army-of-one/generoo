package {{group_id}}.{{artifact_id_periods}}.service;

{{#hibernate}}
import {{group_id}}.{{artifact_id_periods}}.repository.{{artifact_id_capitalized}}Repository;
{{/hibernate}}
import org.springframework.stereotype.Service;

@Service
public class {{artifact_id_capitalized}}Service {

  {{#hibernate}}private final {{artifact_id_capitalized}}Repository {{artifact_id_camel}}Repository;

  public {{artifact_id_capitalized}}Service({{artifact_id_capitalized}}Repository {{artifact_id_camel}}Repository) {
    this.{{artifact_id_camel}}Repository = {{artifact_id_camel}}Repository;
  }{{/hibernate}}
  {{^hibernate}}
  public {{artifact_id_capitalized}}Service() {
  }
  {{/hibernate}}
}
