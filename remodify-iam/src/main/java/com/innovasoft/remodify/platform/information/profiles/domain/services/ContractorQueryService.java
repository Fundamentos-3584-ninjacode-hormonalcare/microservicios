package com.innovasoft.remodify.platform.information.profiles.domain.services;

import com.innovasoft.remodify.platform.information.profiles.domain.model.aggregates.Contractor;
import com.innovasoft.remodify.platform.information.profiles.domain.model.queries.GetAllContractorQuery;
import com.innovasoft.remodify.platform.information.profiles.domain.model.queries.GetContractorByIdQuery;

import java.util.List;
import java.util.Optional;

public interface ContractorQueryService {
    //boolean existsByPhone(String phone);

    List<Contractor> handle(GetAllContractorQuery query);
    Optional<Contractor> handle(GetContractorByIdQuery query);
}
