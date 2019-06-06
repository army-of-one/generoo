package {{group_id}}.{{artifact_id_periods}}.api;

import {{group_id}}.{{artifact_id_periods}}.service.{{artifact_id_capitalized}}Service;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class {{artifact_id_capitalized}}Controller {

  private final {{artifact_id_capitalized}}Service {{artifact_id_camel}}Service;

  public {{artifact_id_capitalized}}Controller({{artifact_id_capitalized}}Service {{artifact_id_camel}}Service) {
	this.{{artifact_id_camel}}Service = {{artifact_id_camel}}Service;
  }
}
