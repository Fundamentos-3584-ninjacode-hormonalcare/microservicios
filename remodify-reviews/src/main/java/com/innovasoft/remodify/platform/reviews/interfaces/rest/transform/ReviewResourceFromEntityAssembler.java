package com.innovasoft.remodify.platform.reviews.interfaces.rest.transform;

import com.innovasoft.remodify.platform.reviews.domain.model.aggregates.Review;
import com.innovasoft.remodify.platform.reviews.interfaces.rest.resources.ReviewResource;

public class ReviewResourceFromEntityAssembler {
    public static ReviewResource toResourceFromEntity(Review entity){
        return new ReviewResource(
            entity.getId(),
            entity.getContractorId(),
            entity.getProjectId(),
            entity.getDuration(),
            entity.getRating(),
            entity.getComment(),
            entity.getImage());
    }
}
