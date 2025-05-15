package com.innovasoft.remodify.platform.information.profiles.interfaces.rest.transform;


import com.innovasoft.remodify.platform.information.profiles.domain.model.commands.CreateContractorCommand;
import com.innovasoft.remodify.platform.information.profiles.interfaces.rest.resources.CreateContractorResource;

public class CreateContractorCommandFromResourceAssembler {

        public static CreateContractorCommand toCommandFromResource(CreateContractorResource resource) {
            return new CreateContractorCommand(
                    resource.description(),
                    resource.phone()
            );
        }
}
