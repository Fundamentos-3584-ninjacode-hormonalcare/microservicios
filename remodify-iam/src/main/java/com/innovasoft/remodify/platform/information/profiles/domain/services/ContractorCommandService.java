package com.innovasoft.remodify.platform.information.profiles.domain.services;

import com.innovasoft.remodify.platform.information.profiles.domain.model.commands.CreateContractorCommand;


public interface ContractorCommandService {
    Long handle(CreateContractorCommand command);

}
