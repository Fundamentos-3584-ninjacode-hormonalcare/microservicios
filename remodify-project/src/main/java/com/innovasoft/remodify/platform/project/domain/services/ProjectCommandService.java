package com.innovasoft.remodify.platform.project.domain.services;

import com.innovasoft.remodify.platform.project.domain.model.aggregates.Project;
import com.innovasoft.remodify.platform.project.domain.model.commands.CreateProjectCommand;

import java.util.Optional;

public interface ProjectCommandService {

    Optional<Project> handle(CreateProjectCommand command);
}
