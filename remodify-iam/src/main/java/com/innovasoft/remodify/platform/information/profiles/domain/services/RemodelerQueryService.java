package com.innovasoft.remodify.platform.information.profiles.domain.services;

import com.innovasoft.remodify.platform.information.profiles.domain.model.aggregates.Remodeler;
import com.innovasoft.remodify.platform.information.profiles.domain.model.queries.GetAllRemodelerQuery;
import com.innovasoft.remodify.platform.information.profiles.domain.model.queries.GetRemodelerByIdQuery;

import java.util.List;
import java.util.Optional;


public interface RemodelerQueryService {

    Optional<Remodeler> handle(GetRemodelerByIdQuery query);
    List<Remodeler> handle(GetAllRemodelerQuery query);

}
