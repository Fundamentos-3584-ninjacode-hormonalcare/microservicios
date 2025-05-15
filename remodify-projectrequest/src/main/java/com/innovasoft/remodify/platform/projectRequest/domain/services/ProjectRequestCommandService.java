package com.innovasoft.remodify.platform.projectRequest.domain.services;

import com.innovasoft.remodify.platform.projectRequest.domain.model.aggregates.ProjectRequest;
import com.innovasoft.remodify.platform.projectRequest.domain.model.commands.CreateProjectRequestCommand;

import java.util.Optional;

public interface ProjectRequestCommandService {
    Optional<ProjectRequest> handle(CreateProjectRequestCommand command);
}
