package com.innovasoft.remodify.platform.business.domain.services;

import com.innovasoft.remodify.platform.business.domain.model.aggregates.Business;
import com.innovasoft.remodify.platform.business.domain.model.commands.CreateBusinessCommand;

import java.util.Optional;

public interface BusinessCommandService {

    Optional<Business> handle(CreateBusinessCommand command);
}
