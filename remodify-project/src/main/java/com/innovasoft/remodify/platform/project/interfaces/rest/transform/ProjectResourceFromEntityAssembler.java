package com.innovasoft.remodify.platform.project.interfaces.rest.transform;

import com.innovasoft.remodify.platform.project.domain.model.aggregates.Project;
import com.innovasoft.remodify.platform.project.interfaces.rest.resources.ProjectResource;

public class ProjectResourceFromEntityAssembler {

    public static ProjectResource toResourceFromEntity(Project entity){
        return new ProjectResource(
                entity.getId(),
                entity.getName(),
                entity.getDescription(),
                entity.getBusinessId(),
                entity.getContractorId(),
                entity.getStartDate(),
                entity.getFinishDate(),
                entity.getImage()
        );
    }
}
