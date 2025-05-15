package com.innovasoft.remodify.platform.reviews.domain.model.queries;

import com.innovasoft.remodify.platform.reviews.domain.model.valueobjects.ContractorId;
import com.innovasoft.remodify.platform.reviews.domain.model.valueobjects.ProjectId;

public record GetReviewByContractorIdAndProjectId(ContractorId contractorId, ProjectId projectId) {

}
