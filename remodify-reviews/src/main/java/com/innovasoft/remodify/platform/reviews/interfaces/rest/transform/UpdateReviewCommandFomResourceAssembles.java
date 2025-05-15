package com.innovasoft.remodify.platform.reviews.interfaces.rest.transform;

import com.innovasoft.remodify.platform.reviews.domain.model.commands.UpdateReviewCommand;
import com.innovasoft.remodify.platform.reviews.interfaces.rest.resources.UpdateReviewResource;

public class UpdateReviewCommandFomResourceAssembles {
    public static UpdateReviewCommand toCommandFromResource(Long reviewId, UpdateReviewResource resource){
        return new UpdateReviewCommand(
            reviewId,
            resource.duration(),
            resource.comment(),
            resource.image());
    }
}
