package com.innovasoft.remodify.platform.project.domain.services;

import com.innovasoft.remodify.platform.project.domain.model.aggregates.Project;
import com.innovasoft.remodify.platform.project.domain.model.queries.GetAllProjects;
import com.innovasoft.remodify.platform.project.domain.model.queries.GetAllProjectsByBusinessIdQuery;
import com.innovasoft.remodify.platform.project.domain.model.queries.GetProjectByIdQuery;

import java.util.List;
import java.util.Optional;

public interface ProjectQueryService {

    List<Project> handle(GetAllProjects query);
    List<Project> handle(GetAllProjectsByBusinessIdQuery query);
    Optional<Project> handle(GetProjectByIdQuery query);
}
