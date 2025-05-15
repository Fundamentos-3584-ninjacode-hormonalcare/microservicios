package com.innovasoft.remodify.platform.reviews.domain.services;

import com.innovasoft.remodify.platform.reviews.domain.model.aggregates.Review;
import com.innovasoft.remodify.platform.reviews.domain.model.commands.CreateReviewCommand;
import com.innovasoft.remodify.platform.reviews.domain.model.commands.DeleteReviewCommand;
import com.innovasoft.remodify.platform.reviews.domain.model.commands.UpdateReviewCommand;

import java.util.Optional;

public interface ReviewCommandService{
    Long handle(CreateReviewCommand command);
    Optional<Review> handle(UpdateReviewCommand command);
    Optional<Review> handle(DeleteReviewCommand command);
}
