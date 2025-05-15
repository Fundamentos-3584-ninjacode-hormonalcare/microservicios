package com.innovasoft.remodify.platform.reviews.infrastructure.persistence.jpa.repositories;

import com.innovasoft.remodify.platform.reviews.domain.model.aggregates.Review;
import com.innovasoft.remodify.platform.reviews.domain.model.valueobjects.ContractorId;
import com.innovasoft.remodify.platform.reviews.domain.model.valueobjects.ProjectId;
import com.innovasoft.remodify.platform.reviews.domain.model.valueobjects.Rating;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface ReviewRepository extends JpaRepository<Review, Long> {
    Optional<Review> findByContractorIdAndProjectId(ContractorId contractorId, ProjectId projectId);
    Boolean existsByRating(Rating rating);
}
