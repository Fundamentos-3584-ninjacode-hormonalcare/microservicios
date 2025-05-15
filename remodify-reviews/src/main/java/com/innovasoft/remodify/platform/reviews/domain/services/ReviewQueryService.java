package com.innovasoft.remodify.platform.reviews.domain.services;

import com.innovasoft.remodify.platform.reviews.domain.model.aggregates.Review;
import com.innovasoft.remodify.platform.reviews.domain.model.queries.GetAllReviewsQuery;
import com.innovasoft.remodify.platform.reviews.domain.model.queries.GetReviewByContractorIdAndProjectId;
import com.innovasoft.remodify.platform.reviews.domain.model.queries.GetReviewByIdQuery;

import java.util.List;
import java.util.Optional;

public interface ReviewQueryService {
    Optional<Review> handle(GetReviewByIdQuery query);
    Optional<Review> handle(GetReviewByContractorIdAndProjectId query);
    List<Review> handle(GetAllReviewsQuery query);
}
