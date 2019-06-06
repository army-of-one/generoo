package {{group_id}}.{{artifact_id_periods}}.entity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.util.UUID;

@Entity
@Table(name = "{{artifact_id_snake}}", schema = "{{database_schema}}", catalog = "{{database_name}}")
public class {{artifact_id_capitalized}}Entity {
  private UUID {{artifact_id_camel}}Id;

  @Id
  @Column(name = "{{artifact_id_snake}}_id")
  public UUID get{{artifact_id_capitalized}}Id() {
	return {{artifact_id_camel}}Id;
  }

  public void set{{artifact_id_capitalized}}Id(UUID {{artifact_id_camel}}Id) {
	this.{{artifact_id_camel}}Id = {{artifact_id_camel}}Id;
  }

}
