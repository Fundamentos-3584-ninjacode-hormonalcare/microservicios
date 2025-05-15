package com.innovasoft.remodify.platform.projectRequest.domain.services;

import com.innovasoft.remodify.platform.projectRequest.domain.model.aggregates.ProjectRequest;
import com.innovasoft.remodify.platform.projectRequest.domain.model.queries.GetAllProjectRequestsByBusinessIdQuery;
import com.innovasoft.remodify.platform.projectRequest.domain.model.queries.GetAllProjectRequestsByContractorIdQuery;
import com.innovasoft.remodify.platform.projectRequest.domain.model.queries.GetProjectRequestByIdQuery;

import java.util.List;
import java.util.Optional;

public interface ProjectRequestQueryService {

    List<ProjectRequest> handle(GetAllProjectRequestsByBusinessIdQuery query);

    List<ProjectRequest> handle(GetAllProjectRequestsByContractorIdQuery query);

    Optional<ProjectRequest> handle(GetProjectRequestByIdQuery query);
}
