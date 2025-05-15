package com.innovasoft.remodify.platform.projectRequest.interfaces.rest.transform;

import com.innovasoft.remodify.platform.projectRequest.domain.model.aggregates.ProjectRequest;
import com.innovasoft.remodify.platform.projectRequest.interfaces.rest.resources.ProjectRequestResource;

public class ProjectRequestResourceFromEntityAssembler {

    public static ProjectRequestResource toResourceFromEntity(ProjectRequest entity){
        return new ProjectRequestResource(
                entity.getId(),
                entity.getName(),
                entity.getSurname(),
                entity.getEmail(),
                entity.getPhone(),
                entity.getAddress(),
                entity.getCity(),
                entity.getSummary(),
                entity.getBusinessId(),
                entity.getContractorId(),
                entity.getDeadlineDate(),
                entity.getRooms(),
                entity.getBudget()
        );
    }
}
