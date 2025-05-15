package com.innovasoft.remodify.platform.business.interfaces.rest.transform;

import com.innovasoft.remodify.platform.business.domain.model.aggregates.Business;
import com.innovasoft.remodify.platform.business.interfaces.rest.resources.BusinessResource;

public class BusinessResourceFromEntityAssembler {

    public static BusinessResource toResourceFromEntity(Business entity){
        return new BusinessResource(
                entity.getId(),
                entity.getName(),
                entity.getImage(),
                entity.getExpertise(),
                entity.getAddress(),
                entity.getCity(),
                entity.getDescription(),
                entity.getRemodelerId()
        );
    }
}
