package com.innovasoft.remodify.platform.iam.interfaces.rest.transform;

import com.innovasoft.remodify.platform.iam.domain.model.commands.UpdateUserCommand;
import com.innovasoft.remodify.platform.iam.interfaces.rest.resources.UpdateUserResource;

public class UpdateUserCommandFromResourceAssembler {
    public static UpdateUserCommand toCommandFromResource(Long userId, UpdateUserResource resource){
        return new UpdateUserCommand(
            userId,
            resource.email(),
            resource.description(),
            resource.phone(),
            resource.image());
    }
}
