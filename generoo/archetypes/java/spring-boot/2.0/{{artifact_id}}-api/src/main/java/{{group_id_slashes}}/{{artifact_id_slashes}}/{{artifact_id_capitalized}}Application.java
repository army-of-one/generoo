package {{group_id}}.{{artifact_id_periods}};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
{{#hibernate}}
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
{{/hibernate}}
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@SpringBootApplication(scanBasePackages = {
	"{{group_id}}.{{artifact_id_periods}}"
})
@EnableSwagger2
{{#hibernate}}
@EnableJpaRepositories(basePackages = "{{group_id}}.{{artifact_id_periods}}.repository")
{{/hibernate}}
public class {{artifact_id_capitalized}}Application {

	public static void main(String[] args) {
		SpringApplication.run({{artifact_id_capitalized}}Application.class, args);
	}
}
