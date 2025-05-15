package com.innovasoft.remodify.platform.reviews.interfaces.rest.transform;

import com.innovasoft.remodify.platform.reviews.domain.model.commands.CreateReviewCommand;
import com.innovasoft.remodify.platform.reviews.interfaces.rest.resources.CreateReviewResource;

public class CreateReviewCommandFromResourceAssembler {
    public static CreateReviewCommand toCommandResource(CreateReviewResource resource) {
        return new CreateReviewCommand(
            resource.contractorId(),
            resource.projectId(),
            resource.duration(),
            resource.rating(),
            resource.comment(),
            resource.image()
        );
    }
}
