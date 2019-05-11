package {{group_id}}.{{artifact_id_periods}}.config;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
@EnableTransactionManagement
@ConfigurationProperties(prefix = "database")
public class DataConfig {

    private String url;
    private String username;
    private String password;

}
