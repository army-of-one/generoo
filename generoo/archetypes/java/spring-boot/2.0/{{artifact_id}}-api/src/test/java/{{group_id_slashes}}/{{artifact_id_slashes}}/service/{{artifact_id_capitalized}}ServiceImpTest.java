package {{group_id}}.{{artifact_id_periods}}.service;

{{#hibernate}}
import {{group_id}}.{{artifact_id_periods}}.repository.{{artifact_id_capitalized}}Repository;
{{/hibernate}}
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
class {{artifact_id_capitalized}}ServiceImpTest {

  {{#hibernate}}
  @Mock
  private {{artifact_id_capitalized}}Repository {{artifact_id_camel}}Repository;
  {{/hibernate}}
  @InjectMocks
  private {{artifact_id_capitalized}}Service {{artifact_id_camel}}ServiceImp;

  @Test
  void create{{artifact_id_capitalized}}() {

  }

  @Test
  void create{{artifact_id_capitalized}}NullIDTest() {

  }

}