package {{group_id}}.{{artifact_id_periods}};

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@SpringBootApplication(scanBasePackages = {
	"{{group_id}}.{{artifact_id_periods}}"
})
@EnableSwagger2
{{#database}}
@EnableJpaRepositories(basePackages = "{{group_id}}.{{artifact_id_periods}}.repository")
{{/database}}
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}
}
