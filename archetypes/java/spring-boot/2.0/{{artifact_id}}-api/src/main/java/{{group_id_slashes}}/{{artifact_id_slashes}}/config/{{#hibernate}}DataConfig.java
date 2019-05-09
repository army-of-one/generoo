package {{group_id}}.{{artifact_id_periods}}.config;

import org.apache.tomcat.jdbc.pool.PoolProperties;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;

@Configuration
@EnableTransactionManagement
@ConfigurationProperties(prefix = "database")
public class DataConfig {
    private final static Logger LOGGER = LoggerFactory.getLogger(DataConfig.class);

    private String server;

    private String port;

    private String name;

    private String schema;

    private String username;

    private String password;

    @Bean
    public DataSource dataSource() {
        String url = "jdbc:postgresql://" +
            server + ":" +
            port + "/" +
            name + "?stringtype=unspecified&defaultSchema=" +
            schema;

        LOGGER.info("Creating DataSource");
        PoolProperties p = new PoolProperties();
        p.setDriverClassName("org.postgresql.Driver");
        p.setUrl(url);
        p.setUsername(username);
        p.setPassword(password);
        p.setJmxEnabled(true);
        p.setTestWhileIdle(false);
        p.setTestOnBorrow(true);
        p.setValidationQuery("SELECT 1");
        p.setTestOnReturn(false);
        p.setValidationInterval(30000);
        p.setTimeBetweenEvictionRunsMillis(30000);
        p.setMaxActive(100);
        p.setInitialSize(10);
        p.setMaxWait(10000);
        p.setRemoveAbandonedTimeout(60);
        p.setMinEvictableIdleTimeMillis(30000);
        p.setMinIdle(10);
        p.setLogAbandoned(true);
        p.setRemoveAbandoned(true);
        p.setJdbcInterceptors(
                "org.apache.tomcat.jdbc.pool.interceptor.ConnectionState;" +
                "org.apache.tomcat.jdbc.pool.interceptor.StatementFinalizer");
        org.apache.tomcat.jdbc.pool.DataSource dataSource = new org.apache.tomcat.jdbc.pool.DataSource();
        dataSource.setPoolProperties(p);
        return dataSource;
    }

}
