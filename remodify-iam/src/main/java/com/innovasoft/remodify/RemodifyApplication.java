package com.innovasoft.remodify;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

@EnableJpaAuditing
@SpringBootApplication
public class RemodifyApplication {

	public static void main(String[] args) {
		SpringApplication.run(RemodifyApplication.class, args);
	}

}
